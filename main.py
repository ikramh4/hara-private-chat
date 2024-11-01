import customtkinter as ctk
from app_ui import AppUI

class App:
    def __init__(self):
        # Set up the appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("AI Chat Assistant")
        self.root.geometry("1100x700")
        
        # Make window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Initialize UI
        self.app_ui = AppUI(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run() 