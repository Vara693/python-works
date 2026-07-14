"""
main.py

Entry point for the Mouse Dynamics Authentication app.

Features:
- Tkinter-based polished login / register UI (nice layout + colors)
- Integrates with a UserManager (users.json) to register/login users and track completed sessions
- Calls `run_session(user, session_id)` (from game_runner.py) to launch the pygame session runner
- After the session ends the app shows a post-session menu: Next Session / Logout / Exit

Notes:
- This file expects `user_manager.py` and `game_runner.py` to exist in the same project.
- If `game_runner` is not available, a built-in lightweight simulator will run so you can test the GUI.
- Requirements: `pygame` (for the actual games). Install via: pip install pygame

Run:
    python main.py

"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import os
import sys
import json



# Try to import project modules. If they are not yet present, provide fallbacks so the UI can be tested.
try:
    from user_manager import UserManager
except Exception:
    # fallback simple UserManager implementation (compatible with the project's API)
    class UserManager:
        def __init__(self, db_file="users.json"):
            self.db_file = db_file
            if not os.path.exists(db_file):
                with open(db_file, "w") as f:
                    json.dump({}, f)
            with open(db_file, "r") as f:
                self.users = json.load(f)

        def register(self, user, pwd):
            if user in self.users:
                return False
            self.users[user] = {"password": pwd, "sessions": 0}
            self._save()
            return True

        def login(self, user, pwd):
            return user in self.users and self.users[user]["password"] == pwd

        def next_session(self, user):
            self.users[user]["sessions"] += 1
            self._save()
            return self.users[user]["sessions"]

        def get_sessions(self, user):
            return self.users.get(user, {}).get("sessions", 0)

        def _save(self):
            with open(self.db_file, "w") as f:
                json.dump(self.users, f, indent=4)

try:
    from game_runner import run_session
except Exception:
    # fallback run_session simulator: creates a dummy CSV and sleeps for a few seconds
    import csv
    def run_session(user, session_id):
        # create data folder and dummy csv event file to simulate the session
        os.makedirs(f"data/{user}", exist_ok=True)
        filepath = f"data/{user}/session{session_id}.csv"
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp","x","y","event","game","session_id","user_id"])
            # produce some fake events
            t0 = time.time()
            for i in range(200):
                writer.writerow([round(time.time()-t0, 3), 100+i, 150+(i%30), "move", "SimGame", session_id, user])
                time.sleep(0.01)
        # small pause to emulate running time
        time.sleep(0.5)
        return


# ---------- Helper functions ----------

def center_window(win, width=900, height=600):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


# ---------- Main Application ----------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Dynamics Auth — Data Collector")
        center_window(self.root, 1000, 650)
        self.um = UserManager()
        self.current_user = None

        # ---------- Styling ----------
        self.primary = "#2E86AB"   # blue
        self.accent = "#F6AE2D"    # orange
        self.bg = "#F4F7FA"        # very light
        self.card = "#FFFFFF"
        self.root.configure(bg=self.bg)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=self.bg)
        style.configure('Card.TFrame', background=self.card, relief='flat')
        style.configure('Title.TLabel', font=('Segoe UI', 20, 'bold'), background=self.bg, foreground=self.primary)
        style.configure('Subtitle.TLabel', font=('Segoe UI', 10), background=self.bg, foreground='#333')
        style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'), background=self.card)
        style.configure('TButton', font=('Segoe UI', 11, 'bold'))
        style.configure('Accent.TButton', background=self.accent, foreground='black')

        # ---------- Layout ----------
        self.container = ttk.Frame(self.root)
        self.container.pack(fill='both', expand=True, padx=20, pady=20)

        # Left Branding Panel
        self.left = ttk.Frame(self.container, width=340, style='Card.TFrame')
        self.left.pack(side='left', fill='y', padx=(0,20))
        self.left.pack_propagate(False)
        self._build_left()

        # Right Main Panel
        self.right = ttk.Frame(self.container, style='Card.TFrame')
        self.right.pack(side='right', fill='both', expand=True)
        self._build_right()

    # ---------- Left panel UI ----------
    def _build_left(self):
        logo = tk.Canvas(self.left, width=300, height=200, bg=self.card, highlightthickness=0)
        logo.pack(pady=(30,10))
        # draw simple emblem
        logo.create_oval(30, 20, 270, 260, fill=self.primary, outline='')
        logo.create_text(150, 120, text='MOUSE-AUTH', fill='white', font=('Segoe UI', 20, 'bold'))

        ttk.Label(self.left, text='Mouse Dynamics Authentication', style='Subtitle.TLabel', wraplength=260).pack(pady=(10,20))

        info = ttk.Frame(self.left, style='Card.TFrame')
        info.pack(padx=15, pady=10, fill='x')
        ttk.Label(info, text='How it works:', style='Header.TLabel').pack(anchor='w', pady=(6,4))
        bullets = [
            'Register and login',
            'Play a short session (4 games)',
            'Data is recorded per session',
            'Repeat for 6 sessions per user'
        ]
        for b in bullets:
            ttk.Label(info, text='• ' + b, background=self.card).pack(anchor='w', padx=8)

        ttk.Label(self.left, text='Status', style='Header.TLabel').pack(anchor='w', pady=(12,4), padx=15)
        self.status_var = tk.StringVar(value='Idle')
        ttk.Label(self.left, textvariable=self.status_var, background=self.card).pack(anchor='w', padx=15)

    # ---------- Right panel (login/register + controls) ----------
    def _build_right(self):
        pad = 12
        header = ttk.Label(self.right, text='Welcome — Please Login or Register', style='Title.TLabel')
        header.pack(pady=(20,5))

        sub = ttk.Label(self.right, text='Your privacy is respected — data stored locally', style='Subtitle.TLabel')
        sub.pack(pady=(0,12))

        # Notebook for Login / Register
        notebook = ttk.Notebook(self.right)
        notebook.pack(padx=20, pady=10, fill='x')

        # Login Tab
        login_frame = ttk.Frame(notebook, padding=20)
        notebook.add(login_frame, text='Login')

        ttk.Label(login_frame, text='Username:').grid(row=0, column=0, sticky='e')
        ttk.Label(login_frame, text='Password:').grid(row=1, column=0, sticky='e')

        self.login_user = tk.Entry(login_frame, font=('Segoe UI', 11))
        self.login_pwd = tk.Entry(login_frame, show='*', font=('Segoe UI', 11))
        self.login_user.grid(row=0, column=1, padx=8, pady=6)
        self.login_pwd.grid(row=1, column=1, padx=8, pady=6)

        self.login_btn = ttk.Button(login_frame, text='Login', command=self.on_login)
        self.login_btn.grid(row=2, column=0, columnspan=2, pady=(8,0))

        # Register Tab
        reg_frame = ttk.Frame(notebook, padding=20)
        notebook.add(reg_frame, text='Register')

        ttk.Label(reg_frame, text='Choose a username:').grid(row=0, column=0, sticky='e')
        ttk.Label(reg_frame, text='Choose a password:').grid(row=1, column=0, sticky='e')

        self.reg_user = tk.Entry(reg_frame, font=('Segoe UI', 11))
        self.reg_pwd = tk.Entry(reg_frame, show='*', font=('Segoe UI', 11))
        self.reg_user.grid(row=0, column=1, padx=8, pady=6)
        self.reg_pwd.grid(row=1, column=1, padx=8, pady=6)

        self.reg_btn = ttk.Button(reg_frame, text='Register & Start', command=self.on_register)
        self.reg_btn.grid(row=2, column=0, columnspan=2, pady=(8,0))

        # Footer / User Dashboard (hidden until login)
        self.dashboard = ttk.Frame(self.right, padding=16, style='Card.TFrame')
        self.dashboard.pack(padx=20, pady=18, fill='x')
        self.dashboard.pack_forget()

        self.welcome_lbl = ttk.Label(self.dashboard, text='', font=('Segoe UI', 14, 'bold'), background=self.card)
        self.welcome_lbl.pack(anchor='w')

        self.session_info = tk.StringVar()
        ttk.Label(self.dashboard, textvariable=self.session_info, background=self.card).pack(anchor='w', pady=(6,4))

        btn_frame = ttk.Frame(self.dashboard, style='Card.TFrame')
        btn_frame.pack(anchor='w', pady=(8,0))
        self.start_btn = ttk.Button(btn_frame, text='Start Session', command=self.start_session, style='Accent.TButton')
        self.start_btn.grid(row=0, column=0, padx=(0,8))
        self.logout_btn = ttk.Button(btn_frame, text='Logout', command=self.logout)
        self.logout_btn.grid(row=0, column=1)

        # Help / About
        foot = ttk.Frame(self.right)
        foot.pack(side='bottom', fill='x', padx=20, pady=12)
        ttk.Button(foot, text='Help', command=self.show_help).pack(side='left')
        ttk.Button(foot, text='Open Data Folder', command=self.open_data_folder).pack(side='right')

    # ---------- Callbacks ----------
    def on_login(self):
        user = self.login_user.get().strip()
        pwd = self.login_pwd.get().strip()
        if not user or not pwd:
            messagebox.showwarning('Missing', 'Please enter username and password')
            return
        if self.um.login(user, pwd):
            self.current_user = user
            sessions = getattr(self.um, 'get_sessions', lambda u: self.um.users[u]['sessions'])(user)
            self.show_dashboard(user, sessions)
            self.status_var.set(f'Logged in as {user}')
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password')

    def on_register(self):
        user = self.reg_user.get().strip()
        pwd = self.reg_pwd.get().strip()
        if not user or not pwd:
            messagebox.showwarning('Missing', 'Please enter username and password')
            return
        if self.um.register(user, pwd):
            self.current_user = user
            # do not increment session until the user clicks Start Session
            self.show_dashboard(user, 0)
            messagebox.showinfo('Welcome', f'Registered {user} — ready to start your first session')
            self.status_var.set(f'Registered {user}')
        else:
            messagebox.showerror('Register Failed', 'Username already taken')

    def show_dashboard(self, user, sessions_completed):
        self.welcome_lbl.configure(text=f'Hello, {user}!')
        self.session_info.set(f'Sessions completed: {sessions_completed} (you will start session {sessions_completed + 1})')
        self.dashboard.pack(padx=20, pady=18, fill='x')

    def start_session(self):
        if not self.current_user:
            messagebox.showwarning('Not logged in', 'Please login or register first')
            return
        # increment session count and get new session id
        session_id = self.um.next_session(self.current_user)
        self.status_var.set(f'Running session {session_id} for {self.current_user}...')

        # hide main window while pygame runs (run_session is blocking)
        self.root.withdraw()

        try:
            run_session(self.current_user, session_id)
        except Exception as e:
            # show error and return to UI
            messagebox.showerror('Session Error', f'An error occurred while running the session:\n{e}')
        finally:
            # restore UI
            self.root.deiconify()
            self.status_var.set('Idle')
            # show post-session options
            self.post_session_menu()

    def post_session_menu(self):
        # custom modal with 3 choices: Next Session / Logout / Exit
        dlg = tk.Toplevel(self.root)
        dlg.title('Session Completed')
        center_window(dlg, 420, 180)
        dlg.transient(self.root)
        dlg.grab_set()

        ttk.Label(dlg, text='Session finished!', style='Title.TLabel').pack(pady=(10,6))
        ttk.Label(dlg, text='What would you like to do next?', style='Subtitle.TLabel').pack(pady=(0,12))

        frame = ttk.Frame(dlg)
        frame.pack(pady=6)

        def do_next():
            dlg.destroy()
            # start next session immediately
            session_id = self.um.next_session(self.current_user)
            self.root.withdraw()
            try:
                run_session(self.current_user, session_id)
            except Exception as e:
                messagebox.showerror('Session Error', f'An error occurred while running the session:\n{e}')
            finally:
                self.root.deiconify()
                self.post_session_menu()

        def do_logout():
            dlg.destroy()
            self.logout()

        def do_exit():
            dlg.destroy()
            self.root.quit()

        ttk.Button(frame, text='Next Session', command=do_next).grid(row=0, column=0, padx=8)
        ttk.Button(frame, text='Logout', command=do_logout).grid(row=0, column=1, padx=8)
        ttk.Button(frame, text='Exit App', command=do_exit).grid(row=0, column=2, padx=8)

    def logout(self):
        self.current_user = None
        self.dashboard.pack_forget()
        self.login_user.delete(0, 'end')
        self.login_pwd.delete(0, 'end')
        self.reg_user.delete(0, 'end')
        self.reg_pwd.delete(0, 'end')
        self.status_var.set('Logged out')

    def show_help(self):
        messagebox.showinfo('How to use', '1) Register or Login\n2) Press Start Session to begin\n3) Play through the mini-games (they will switch automatically)\n4) At session end choose Next / Logout / Exit')

    def open_data_folder(self):
        path = os.path.abspath('data')
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        try:
            if sys.platform == 'win32':
                os.startfile(path)
            elif sys.platform == 'darwin':
                os.system(f'open "{path}"')
            else:
                os.system(f'xdg-open "{path}"')
        except Exception:
            messagebox.showinfo('Data folder', f'Data is stored in: {path}')


# ---------- Run app ----------
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
