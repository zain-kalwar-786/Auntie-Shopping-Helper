from tkinter import *

root = Tk()
root.title("Auntie Shopping Helper")
root.geometry("500x400")

total = 0

def add_item():
    global total

    item = item_entry.get()
    price = price_entry.get()

    if item != "" and price != "":
        price = float(price)

        listbox.insert(END, f"{item} - Rs.{price}")
        total += price

        total_label.config(text=f"Total: Rs.{total}")

        item_entry.delete(0, END)
        price_entry.delete(0, END)

# Heading
Label(root, text="Auntie Shopping Helper",
      font=("Arial", 16, "bold")).pack(pady=10)

# Item Name
Label(root, text="Item Name").pack()
item_entry = Entry(root, width=30)
item_entry.pack()

# Price
Label(root, text="Price").pack()
price_entry = Entry(root, width=30)
price_entry.pack()

# Add Button
Button(root, text="Add Item",
       command=add_item).pack(pady=10)

# List of items
listbox = Listbox(root, width=50, height=10)
listbox.pack()

# Total
total_label = Label(root, text="Total: Rs.0",
                    font=("Arial", 12, "bold"))
total_label.pack(pady=10)

root.mainloop()