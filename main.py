import tkinter as tk
from tkinter import messagebox

NOTE_FILE = "notes.txt"

def save_notes():
    try:
        with open(NOTE_FILE, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", "Notes saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save notes:\n{e}")

def load_notes():
    try:
        with open(NOTE_FILE, "r") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
    except FileNotFoundError:
        pass  # No notes yet
    except Exception as e:
        messagebox.showerror("Error", f"Could not load notes:\n{e}")

# Setup window
root = tk.Tk()
root.title("Simple Note App")
root.geometry("500x400")

# Text area
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_notes, width=10)
save_button.pack(side="left", padx=10)

load_button = tk.Button(button_frame, text="Load", command=load_notes, width=10)
load_button.pack(side="left", padx=10)

# Auto-load notes on start
load_notes()

root.mainloop()
