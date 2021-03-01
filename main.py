from tkinter import*

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=10, pady=10)

def miles_to_km():
    mile = entry.get()
    km = float(mile) * 1.609
    answer_label.config(text=f"{km}")

entry = Entry(width=20)
entry.insert(END, "0")
entry.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)
mile_label.config(padx=3, pady=3)

equal_label = Label(text="is equals to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=3, pady=3)

answer_label = Label(text="0", font=("Arial", 12, "bold"))
answer_label.grid(column=1, row=1)
answer_label.config(padx=3, pady=3)

km_label = Label(text="KM", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=3, pady=3)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)
button.config(padx=3, pady=3)


window.mainloop()