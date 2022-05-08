import tkinter as tk
# begin a windows
window = tk.Tk()
greeting = tk.Label(text="Hello World!")
label = tk.Label(
  text="Hello bro, from ra1n :>>",
  foreground="#BDD1D9", # set text color to white
  background="#0D1117", # set background color to black
  width="10",
  height="10"

)
button = tk.Button(
  text="click me now!",
  width="5",
  height="5",
  bg="#30363D",
  fg="#BDD1D9"

)

greeting.pack()
window.mainloop()


