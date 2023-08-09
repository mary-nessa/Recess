from fpdf import FPDF
from tkinter import messagebox, filedialog
import tkinter as tk
from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __show(self):
        print("I am SuperClass")


class car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        print("I am subclass")


mycar = car("Honda", "Brown", 4)

mycar._Vehicle__show()

# I did Polymorphism with this next example
# Exercise


class Shape:
    def display(self):
        print("I am SUperclass")


class Rectangle(Shape):
    def __init__(self, lside, s_side):
        self.lside = lside
        self.s_side = s_side

    def rperimeter(self):
        Perimeter = (2 * self.lside) + (2 * self.s_side)
        print("Perimeter of Rect:", Perimeter)

    def display(self):
        print("I am 1st subclass")


R1 = Rectangle(7, 4)
# R1.rperimeter()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = 2 * 3.14 * (self.radius * self.radius)
        print("The Area:", area)

    def display(self):
        print("I am 2nd subclass")


C1 = Circle(10)
rmp = Shape()


def copy(Shape):
    Shape.display()


copy(C1)
copy(R1)

# C1.Area()
# multiple inheritance


class Animal:
    def _init_(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dom(Animal):
    def _init_(self, name):
        super()._init_(name)

    def eat_plants(self):
        print(f"{self.name} lives at home.")


class wild(Animal):
    def _init_(self, name):
        super()._init_(name)

    def eat_meat(self):
        print(f"{self.name} lives in the bush.")


# eagle = wild("Eagle")
# eagle.eat()

# "Method overridding"
"""
    Method overriding occurs when a subclass provides its own 
    implementation of a method that is already defined in its superclass.
    This allows objects of different classes to have different behaviors 
    while being treated uniformly based on their common superclass.
"""


"""
class Worker:
    def __init__(self, name):
        self.name = name

    def postion(self):
        print()
"""

# Abstraction


class Library(ABC):
    @abstractmethod
    def detail(self):
        pass


class Book(Library):
    def __init__(self, bname, bauthor):
        self.bname = bname
        self.bauthor = bauthor

    def detail(self):
        print(f"Book Title: {self.bname} and author: {self.bauthor}")


b1 = Book("Weep Not Child", "Mary Vanessa")
b1.detail()


#  --------------------------------Assignment------------------------------------------------
"""
    Create a receipt printing program with GUI interface.
    A more advanced detail wins more points.
"""

# Create the main window
root = tk.Tk()
root.title("Mary Vanessa Nansumba Receipt Printing")
root.geometry("600x600")

# Function to add an item to the list


def add_item():
    item = item_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if item and quantity and price:
        items_listbox.insert(
            tk.END, f"{item} - Quantity: {quantity} - Price: ${price}")
        item_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Information",
                               "Please enter item details.")

# Function to remove an item from the list


def remove_item():
    selected_index = items_listbox.curselection()
    if selected_index:
        items_listbox.delete(selected_index)


# Function to generate the receipt preview
def generate_preview():
    receipt_text = ""
    receipt_text += "<b>Date: " + get_current_date() + "</b>\n\n"
    receipt_text += "<b>Seller:</b>\n" + seller_name_entry.get() + "\n" + \
        seller_address_entry.get("1.0", tk.END) + "\n\n"
    receipt_text += "<b>Buyer:</b>\n" + buyer_name_entry.get() + "\n" + \
        buyer_address_entry.get("1.0", tk.END) + "\n\n"
    receipt_text += "<b>Items:</b>\n"

    for i in range(items_listbox.size()):
        receipt_text += items_listbox.get(i) + "\n"

    receipt_text += "\n<b>Subtotal:</b> $" + str(get_subtotal()) + "\n"
    receipt_text += "<b>Tax:</b> $" + str(get_tax(get_subtotal())) + "\n"
    receipt_text += "<b>Total:</b> $" + \
        str(get_subtotal() + get_tax(get_subtotal()))

    preview_dialog = tk.Toplevel(root)
    preview_dialog.title("Receipt Preview")

    receipt_preview = tk.Label(
        preview_dialog, text=receipt_text, font=("Arial", 12))
    receipt_preview.pack(padx=20, pady=20)


# Function to generate the PDF
def generate_pdf():
    file_path = filedialog.asksaveasfilename(
        initialdir=".",
        title="Save Receipt as PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        if not file_path.endswith(".pdf"):
            file_path += ".pdf"

        c = FPDF()
        c.add_page()
        c.set_font("Arial", "B", 12)
        c.cell(0, 10, "Receipt", ln=True, align="C")
        c.ln(10)

        receipt_text = ""
        receipt_text += "Date: " + get_current_date() + "\n\n"
        receipt_text += "Seller:\n" + seller_name_entry.get() + "\n" + \
            seller_address_entry.get("1.0", tk.END) + "\n\n"
        receipt_text += "Buyer:\n" + buyer_name_entry.get() + "\n" + \
            buyer_address_entry.get("1.0", tk.END) + "\n\n"
        receipt_text += "Items:\n"

        for i in range(items_listbox.size()):
            receipt_text += items_listbox.get(i) + "\n"

        receipt_text += "\nSubtotal: $" + str(get_subtotal()) + "\n"
        receipt_text += "Tax: $" + str(get_tax(get_subtotal())) + "\n"
        receipt_text += "Total: $" + \
            str(get_subtotal() + get_tax(get_subtotal()))

        c.set_font("Arial", "", 10)
        c.multi_cell(0, 10, receipt_text)

        try:
            c.output(file_path)
            messagebox.showinfo(
                "PDF Generated", "Receipt saved as PDF successfully!")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the PDF: {str(e)}")

# Helper function to get the current date


def get_current_date():
    import datetime
    return datetime.date.today().strftime("%Y-%m-%d")

# Helper function to calculate the subtotal


def get_subtotal():
    subtotal = 0.0
    for i in range(items_listbox.size()):
        item_info = items_listbox.get(i)
        price_start_index = item_info.rfind("$") + 1
        price = float(item_info[price_start_index:])
        subtotal += price
    return subtotal

# Helper function to calculate the tax


def get_tax(amount):
    tax_rate = 0.07
    return amount * tax_rate


# Create the seller section
seller_frame = tk.Frame(root)
seller_frame.pack(pady=10)

seller_name_label = tk.Label(seller_frame, text="Seller Name:")
seller_name_label.pack(side=tk.LEFT)

seller_name_entry = tk.Entry(seller_frame)
seller_name_entry.pack(side=tk.LEFT, padx=10)

seller_address_label = tk.Label(seller_frame, text="Seller Address:")
seller_address_label.pack(side=tk.LEFT)

seller_address_entry = tk.Text(seller_frame, height=3, width=40)
seller_address_entry.pack(side=tk.LEFT, padx=10)

# Create the buyer section
buyer_frame = tk.Frame(root)
buyer_frame.pack(pady=10)

buyer_name_label = tk.Label(buyer_frame, text="Buyer Name:")
buyer_name_label.pack(side=tk.LEFT)

buyer_name_entry = tk.Entry(buyer_frame)
buyer_name_entry.pack(side=tk.LEFT, padx=10)

buyer_address_label = tk.Label(buyer_frame, text="Buyer Address:")
buyer_address_label.pack(side=tk.LEFT)

buyer_address_entry = tk.Text(buyer_frame, height=3, width=40)
buyer_address_entry.pack(side=tk.LEFT, padx=10)


# Create the items section
items_frame = tk.Frame(root)
items_frame.pack(pady=10)

items_label = tk.Label(items_frame, text="Items")
items_label.pack()

item_frame = tk.Frame(items_frame)
item_frame.pack()

item_label = tk.Label(item_frame, text="Item:")
item_label.pack(side=tk.LEFT)

item_entry = tk.Entry(item_frame)
item_entry.pack(side=tk.LEFT, padx=10)

quantity_label = tk.Label(item_frame, text="Quantity:")
quantity_label.pack(side=tk.LEFT)

quantity_entry = tk.Entry(item_frame, width=10)
quantity_entry.pack(side=tk.LEFT, padx=10)

price_label = tk.Label(item_frame, text="Price:")
price_label.pack(side=tk.LEFT)

price_entry = tk.Entry(item_frame, width=10)
price_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(items_frame, text="Add Item", command=add_item)
add_button.pack(pady=10)

items_listbox = tk.Listbox(items_frame, height=10, width=60)
items_listbox.pack(pady=10)

remove_button = tk.Button(items_frame, text="Remove Item", command=remove_item)
remove_button.pack(pady=10)

# Create the receipt preview frame
receipt_preview_frame = tk.Frame(root)
receipt_preview_frame.pack(pady=10)

receipt_preview_button = tk.Button(
    receipt_preview_frame, text="Preview Receipt", command=generate_preview)
receipt_preview_button.pack(side=tk.LEFT, padx=10)

generate_pdf_button = tk.Button(
    receipt_preview_frame, text="Generate PDF", command=generate_pdf)
generate_pdf_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
