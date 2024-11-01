import customtkinter as ctk

class AppUI:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Create main container
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_rowconfigure(1, weight=1)

        # Create title
        self.title_label = ctk.CTkLabel(
            self.main_container,
            text="AI Chat Assistant",
            font=("Arial", 24, "bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create sidebar
        self.setup_sidebar()

        # Create main chat area
        self.setup_chat_area()

    def setup_sidebar(self):
        # Sidebar container
        self.sidebar = ctk.CTkFrame(self.main_container, width=200)
        self.sidebar.grid(row=1, column=0, sticky="nsw", padx=(0, 10))
        
        # Prevent sidebar from shrinking
        self.sidebar.grid_propagate(False)

        # Sidebar elements
        self.new_chat_btn = ctk.CTkButton(
            self.sidebar,
            text="New Chat",
            command=self.new_chat
        )
        self.new_chat_btn.pack(pady=10, padx=10)

        # Settings button at bottom of sidebar
        self.settings_btn = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            command=self.open_settings
        )
        self.settings_btn.pack(pady=10, padx=10, side="bottom")

    def setup_chat_area(self):
        # Chat container
        self.chat_container = ctk.CTkFrame(self.main_container)
        self.chat_container.grid(row=1, column=1, sticky="nsew")
        self.chat_container.grid_rowconfigure(0, weight=1)
        self.chat_container.grid_columnconfigure(0, weight=1)

        # Create scrollable frame for messages
        self.chat_frame = ctk.CTkScrollableFrame(self.chat_container)
        self.chat_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # Input area
        self.input_frame = ctk.CTkFrame(self.chat_container)
        self.input_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.input_textbox = ctk.CTkTextbox(
            self.input_frame,
            height=80,
            wrap="word"
        )
        self.input_textbox.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.send_btn = ctk.CTkButton(
            self.input_frame,
            text="Send",
            width=100,
            command=self.send_message
        )
        self.send_btn.grid(row=0, column=1)

    def new_chat(self):
        # Placeholder for new chat functionality
        pass

    def open_settings(self):
        # Placeholder for settings functionality
        pass

    def send_message(self):
        # Placeholder for send message functionality
        pass 