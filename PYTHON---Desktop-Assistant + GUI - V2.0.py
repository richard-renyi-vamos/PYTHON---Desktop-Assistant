import tkinter as tk
from tkinter import messagebox, Entry, Button, Label, Text, Scrollbar
from PIL import Image, ImageTk, ImageSequence

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistant")
        self.root.geometry("400x500")
        self.root.config(bg="white")

        # Load the GIF
        try:
            self.gif_image = Image.open("assistant.gif")  # Replace with your GIF path
            self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.gif_image)]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load GIF: {e}")
            self.frames = []

        # GIF Label
        self.label = tk.Label(self.root, bg="white")
        self.label.pack(pady=10)

        if self.frames:
            self.animate(0)

        # Chat display area
        self.chat_display = Text(self.root, height=15, width=45, wrap="word", state="disabled", bg="lightgrey")
        self.chat_display.pack(pady=10)
        scrollbar = Scrollbar(self.root, command=self.chat_display.yview)
        scrollbar.pack(side="right", fill="y")
        self.chat_display.config(yscrollcommand=scrollbar.set)

        # User input field
        self.user_input = Entry(self.root, width=40, bg="white")
        self.user_input.pack(pady=5)

        # Send button
        self.send_button = Button(self.root, text="Send", command=self.send_message, bg="blue", fg="white")
        self.send_button.pack(pady=5)

        # Clickable GIF event
        self.label.bind("<Button-1>", self.on_click)

    def animate(self, index):
        frame = self.frames[index]
        self.label.config(image=frame)
        index = (index + 1) % len(self.frames)
        self.root.after(100, self.animate, index)

    def on_click(self, event):
        self.display_message("Assistant: How can I assist you today?")

    def send_message(self):
        user_text = self.user_input.get()
        if user_text.strip():
            self.display_message(f"You: {user_text}")
            self.user_input.delete(0, tk.END)
            self.respond(user_text)

    def display_message(self, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)

    def respond(self, user_text):
        response = "I'm just a simple assistant for now!"
        self.display_message(f"Assistant: {response}")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantApp(root)
    root.mainloop()
