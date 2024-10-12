import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistant")
        self.root.geometry("300x300")
        self.root.config(bg="white")

        # Load the GIF
        self.gif_image = Image.open("assistant.gif")  # Replace with your GIF path

        # Convert GIF frames into a list of PhotoImage objects
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.gif_image)]

        # Create a label to display the GIF frames
        self.label = tk.Label(self.root, bg="white")
        self.label.pack()

        # Start the GIF animation
        self.animate(0)

        # Bind the label to make it clickable
        self.label.bind("<Button-1>", self.on_click)

    def animate(self, index):
        frame = self.frames[index]
        self.label.config(image=frame)
        index = (index + 1) % len(self.frames)  # Loop through the frames
        self.root.after(100, self.animate, index)  # Adjust delay as needed (in milliseconds)

    def on_click(self, event):
        # This function will be called when the assistant is clicked
        messagebox.showinfo("Hello!", "How can I assist you today?")

# Initialize the main application window
root = tk.Tk()
app = AssistantApp(root)
root.mainloop()
