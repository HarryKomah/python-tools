import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Create the main application window
root = tk.Tk()
root.title("Tkinter with Matplotlib")

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine Wave')

# Create a canvas widget to display the Matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter event loop
root.mainloop()

