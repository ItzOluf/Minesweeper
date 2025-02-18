import tkinter as tk

root = tk.Tk()
root.geometry("40x40")

frame = tk.Frame(root, width=40, height=40)
frame.pack_propagate(False)  # Verhindert automatische Größenanpassung
frame.pack(pady=20)

btn = tk.Button(frame, text="OK")
btn.pack(fill="both", expand=True)  # Nimmt gesamte Frame-Größe ein

root.mainloop()
