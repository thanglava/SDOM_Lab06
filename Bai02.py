import tkinter as tk
from tkinter import ttk

class AntiVirusApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AtarBals Modern Antivirus")
        self.geometry("800x500")
        
        # Sidebar
        self.sidebar = tk.Frame(self, bg="#4A90E2", width=200)
        self.sidebar.pack(side="left", fill="y")

        sections = ["AtarBals Modern Antivirus", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for section in sections:
            label = tk.Label(self.sidebar, text=section, bg="#4A90E2", fg="white", font=("Arial", 14))
            label.pack(pady=10)

        scan_now_button = tk.Button(self.sidebar, text="Scan Now", bg="#32CD32", fg="white", font=("Arial", 14))
        scan_now_button.pack(pady=20, fill="x")
        
        # Main Content
        self.main_content = tk.Frame(self, bg="white")
        self.main_content.pack(side="left", fill="both", expand=True)

        title_label = tk.Label(self.main_content, text="Scan", font=("Arial", 24), bg="white")
        title_label.pack(pady=20)

        subtitle_label = tk.Label(self.main_content, text="Premium will be free forever. You just need to click button.", bg="white")
        subtitle_label.pack(pady=5)

        buttons_frame = tk.Frame(self.main_content, bg="white")
        buttons_frame.pack(pady=20)

        buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
        for i, button in enumerate(buttons):
            tk.Button(buttons_frame, text=button, bg="#FF00FF", fg="white", font=("Arial", 14), width=15).grid(row=i//2, column=i%2, padx=10, pady=5)

        premium_label = tk.Label(self.main_content, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", bg="white", fg="#FF00FF", font=("Arial", 12))
        premium_label.pack(pady=20)

if __name__ == "__main__":
    app = AntiVirusApp()
    app.mainloop()