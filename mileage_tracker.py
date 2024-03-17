"""
> Logic + tkinter_Gui  done!.
"""
from tkinter import *


# ---------------- METHODS ----------------------------------------------------------------------
def calculate():
    """
    calculate necessary fields and show them to the user
    :return: None
    """
    x = litre_entry.get()
    y = car_mileage_entry.get()
    a = petrol_price_entry.get()
    b = money_entry.get()
    try:
        if len(money_entry.get()) == 0 and len(litre_entry.get()) == 0:
            display_label.config(text="Please enter\n'Money given' OR\n'Litres shown'")
        elif len(money_entry.get()) == 0:
            z1 = (float(x) * float(y))
            z1 = str(z1)
            z3 = round(float(a) * float(x))
            z3 = str(z3)
            display_label.config(text=("Will go : " + z1 + " KM\nMoney given : " + z3 + " rs"))
        elif len(litre_entry.get()) == 0:
            z2 = ((float(y) / float(a)) * float(b))
            z2 = "{0:.2f}".format(z2)
            z2 = str(z2)
            z4 = (1 / float(a)) * float(b)
            z4 = "{0:.2f}".format(z4)
            z4 = str(z4)
            display_label.config(text=("Will go : " + z2 + " KM\nLitres shown : " + z4 + " L"))
        elif len(money_entry.get()) != 0 and len(litre_entry.get()) != 0:
            z1 = round(float(x) * float(y))
            z1 = str(z1)
            z5 = (float(b) / float(x))
            z5 = "{0:.2f}".format(z5)
            z5 = str(z5)
            display_label.config(text=("Will go : " + z1 + " KM\nPetrol price(approx) : " + z5 + " rs"))
        else:
            print("something went wrong!")
    except ValueError:
        display_label.config(text="Please fill any 3 columns in 'Digits'!")


# ---------------- END METHODS -----------------------------------------------------------------

# ================== MAIN WINDOW ===================================================

window = Tk()
window.title("Mileage Tracker")
window.config(bg="Black")
window.resizable(False, False)

BigFrame = Frame(window, bd=2, relief=SUNKEN)
BigFrame.pack()

frame = Frame(BigFrame)
frame.pack()
frame2 = Frame(BigFrame)
frame2.pack()

car_mileage_label = Label(frame, text="Car Mileage*  : ", font=("Arial", 15, "bold"))
car_mileage_label.grid(row=0, column=0)
car_mileage_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
car_mileage_entry.grid(row=0, column=1)

petrol_price_label = Label(frame, text="Petrol Price   : ", font=("Arial", 15, "bold"))
petrol_price_label.grid(row=1, column=0)
petrol_price_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
petrol_price_entry.grid(row=1, column=1)

money_label = Label(frame, text="Money given  : ", font=("Arial", 15, "bold"))
money_label.grid(row=2, column=0)
money_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
money_entry.grid(row=2, column=1)

litre_label = Label(frame, text="Litres shown  : ", font=("Arial", 15, "bold"))
litre_label.grid(row=3, column=0)
litre_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
litre_entry.grid(row=3, column=1)

car_mileage_entry.insert(0, "15")
petrol_price_entry.insert(0, "106.14")

Button(frame2, text="Enter", font=("Consoles", 10, "bold italic"), command=calculate, width=38).pack(pady=2)

display_label = Label(frame2, font=("Arial", 13, "bold"), bg="White", width=30, height=3, bd=5, relief=RAISED)
display_label.pack()

window.mainloop()

# ================== END MAIN WINDOW ===============================================
