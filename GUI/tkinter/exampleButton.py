import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Tkinter Example")

# Set the dimensions of the window (width x height)
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 24))

# Pack the label widget into the window
label.pack(pady=50)

# Create a button widget
button = tk.Button(root, text="Click Me!", command=lambda: label.config(text="Button Clicked!"))

# Pack the button widget into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()

