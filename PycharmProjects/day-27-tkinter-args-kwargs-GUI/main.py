from tkinter import *

def button_clicked():
    my_label.config(text=f"{input.get()}")


window = Tk()
window.title("My first GUI Program.")
window.minsize(width=500, height= 300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# This is going to place the label on the screen (.pack()), it will not show unless this is called
my_label.grid(column=0, row=0)


# how to change parts of the label
my_label['text'] = "New Text"
# or
#

# Entry - effectively an input
input = Entry(width=25)
input.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=3, row=2)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)



# Layout manager options
# pack - puts it on the screen in a vaguly logical manner
# place - puts it on the screen wherever you specify (x,y)
# grid - puts in on the screen based on a grid



# This keeps the window open
window.mainloop()