import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import os
import sys
import threading
import urllib.request
import zipfile
import shutil

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KS O&M Apps Installer & Launcher")
        self.root.geometry("900x500")
        
        self.zip_url = "https://github.com/fabiomatricardi/KSAPPs/raw/main/KS_OandM_APPS.zip"
        self.zip_filename = "KS_OandM_APPS.zip"
        self.running_processes = {}
        
        # Fix: Get actual working directory (not PyInstaller temp folder)
        if getattr(sys, 'frozen', False):
            self.base_path = os.path.dirname(sys.executable)
        else:
            self.base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Change to base_path so all operations happen where the .exe is
        os.chdir(self.base_path)
        
        self.create_widgets()
        
    def create_widgets(self):
        title_label = tk.Label(self.root, text="KS O&M Apps Manager", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        log_frame = tk.LabelFrame(self.root, text="Installation Log", padx=10, pady=10)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, state='disabled', bg="#f0f0f0")
        self.log_text.pack(fill="both", expand=True)
        
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="indeterminate")
        self.progress.pack(pady=10)
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        self.install_btn = tk.Button(btn_frame, text="Install / Setup", command=self.start_installation, 
                                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.install_btn.pack(side="left", padx=10)
        
        ttk.Separator(btn_frame, orient='vertical').pack(side="left", fill='y', padx=20)
        
        self.app_buttons = {}
        apps = [
            ("Dashboard", "dashboard", "app.py"),
            ("Maintenance", "MAINTENANCE", "maintenance.py"),
            ("SDLOG", "BPO_app_NGUYA", "app.py"),
            ("PTW", "ptw", "app.py")
        ]
        
        for text, folder, script in apps:
            frame = tk.Frame(btn_frame)
            frame.pack(side="left", padx=5)
            
            launch_btn = tk.Button(frame, text=f"▶ {text}", command=lambda f=folder, s=script, t=text: self.launch_app(f, s, t), 
                                   bg="#2196F3", fg="white", font=("Arial", 9, "bold"), width=12, state="disabled")
            launch_btn.pack(side="top", padx=2)
            
            stop_btn = tk.Button(frame, text=f"⏹ Stop", command=lambda f=folder, t=text: self.stop_app(f, t), 
                                 bg="#f44336", fg="white", font=("Arial", 9, "bold"), width=12, state="disabled")
            stop_btn.pack(side="top", padx=2, pady=2)
            
            status_label = tk.Label(frame, text="● Stopped", fg="gray", font=("Arial", 8))
            status_label.pack(side="top", padx=2)
            
            self.app_buttons[folder] = {
                'launch': launch_btn,
                'stop': stop_btn,
                'status': status_label,
                'process': None,
                'script': script
            }
            
    def log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        
    def start_installation(self):
        self.install_btn.config(state="disabled")
        self.progress.start()
        thread = threading.Thread(target=self.run_installation_logic)
        thread.daemon = True
        thread.start()
        
    def run_installation_logic(self):
        try:
            self.log("▄▄▄   ▄▄▄  ▄▄▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄     ▄▄▄      ▄▄▄")
            self.log("Starting Installation Process...")
            self.log(f"Working Directory: {os.getcwd()}")
            
            # 1. Download Zip
            self.log("Downloading the python app folders Archive...")
            if os.path.exists(self.zip_filename):
                os.remove(self.zip_filename)
            urllib.request.urlretrieve(self.zip_url, self.zip_filename)
            self.log("Download complete.")
            
            # 2. Unzip
            self.log("Unzipping the python app folders...")
            if os.path.exists(self.zip_filename):
                with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
                    zip_ref.extractall(".")
                os.remove(self.zip_filename)
            self.log("Unzip complete.")
            
            # 3. NO VENV - Install dependencies directly to system Python
            self.log("Installing dependencies (system Python)...")
            req_path = os.path.join(".", "requirements.txt")
            
            if os.path.exists(req_path):
                # Use 'python' command (system Python) not sys.executable (which is the temp exe)
                subprocess.run(["python", "-m", "pip", "install", "-r", req_path, "--user"], check=True)
                self.log("Dependencies installed.")
            else:
                self.log("Warning: requirements.txt not found.")
            
            self.log("Installation Complete!")
            
            for folder, buttons in self.app_buttons.items():
                buttons['launch'].config(state="normal")
                
        except Exception as e:
            self.log(f"ERROR: {str(e)}")
            messagebox.showerror("Installation Failed", str(e))
        finally:
            self.progress.stop()
            self.install_btn.config(state="normal")
            
    def launch_app(self, folder, script, app_name):
        if folder in self.running_processes and self.running_processes[folder].poll() is None:
            messagebox.showwarning("Warning", f"{app_name} is already running!")
            return
            
        if not os.path.exists(folder):
            messagebox.showerror("Error", f"Folder '{folder}' not found. Please run Installation first.")
            return

        script_path = os.path.join(folder, script)
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"{script} not found in '{folder}'")
            return
            
        # Use system Python (not the installer exe)
        python_cmd = "python"
            
        self.log(f"Starting {app_name} ({script})...")
        
        try:
            process = subprocess.Popen([python_cmd, script], cwd=folder)
            self.running_processes[folder] = process
            
            self.app_buttons[folder]['launch'].config(state="disabled", bg="gray")
            self.app_buttons[folder]['stop'].config(state="normal")
            self.app_buttons[folder]['status'].config(text="● Running", fg="green")
            
            self.log(f"{app_name} started successfully (PID: {process.pid})")
            
            thread = threading.Thread(target=self.monitor_process, args=(folder, app_name))
            thread.daemon = True
            thread.start()
            
        except Exception as e:
            self.log(f"ERROR starting {app_name}: {str(e)}")
            messagebox.showerror("Launch Failed", f"Could not start {app_name}: {str(e)}")
            
    def stop_app(self, folder, app_name):
        if folder not in self.running_processes:
            self.log(f"{app_name} is not running.")
            return
            
        process = self.running_processes[folder]
        
        if process.poll() is None:
            try:
                process.terminate()
                process.wait(timeout=5)
                self.log(f"{app_name} stopped successfully.")
            except subprocess.TimeoutExpired:
                process.kill()
                self.log(f"{app_name} force killed.")
            except Exception as e:
                self.log(f"ERROR stopping {app_name}: {str(e)}")
        else:
            self.log(f"{app_name} was already stopped.")
            
        self.running_processes.pop(folder, None)
        self.app_buttons[folder]['launch'].config(state="normal", bg="#2196F3")
        self.app_buttons[folder]['stop'].config(state="disabled")
        self.app_buttons[folder]['status'].config(text="● Stopped", fg="gray")
        
    def monitor_process(self, folder, app_name):
        import time
        while folder in self.running_processes:
            process = self.running_processes.get(folder)
            if process is None or process.poll() is not None:
                self.root.after(0, lambda: self.process_ended(folder, app_name))
                break
            time.sleep(1)
            
    def process_ended(self, folder, app_name):
        if folder in self.app_buttons:
            self.running_processes.pop(folder, None)
            self.app_buttons[folder]['launch'].config(state="normal", bg="#2196F3")
            self.app_buttons[folder]['stop'].config(state="disabled")
            self.app_buttons[folder]['status'].config(text="● Stopped", fg="gray")
            self.log(f"{app_name} process ended.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()