from tkinter import *


def mile_to_kilometer():
    kilometer_result_label.config(text=round(float(miles_input.get()) * 1.609, 1))


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)

kilo_label = Label(text="Kilometers")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_kilometer)
calculate_button.grid(column=1, row=2)


# This keeps the window open
window.mainloop()