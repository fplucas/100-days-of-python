from tkinter import *

FONT = ("Arial", 14, "bold")

window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=20)

distance_in_miles = Entry(width=10)
distance_in_miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

distance_in_kms = Label(text="0", font=FONT)
distance_in_kms.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)


def miles_to_kms():
    distance_in_kms.config(text=float(distance_in_miles.get()) * 1.609)


calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(column=1, row=2)


window.mainloop()
