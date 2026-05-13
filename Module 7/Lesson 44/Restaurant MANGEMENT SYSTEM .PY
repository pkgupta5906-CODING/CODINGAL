# 1) Import tkinter modules:
#    a) Import `tkinter as tk` to create the GUI window and canvas.
#    b) Import `ttk` for styled widgets like Frame, Label, Button, Combobox.
#    c) Import `messagebox` to show popup messages.
import tkinter as tk
from tkinter import ttk,messagebox

# 2) Create a class `RestaurantOrderManagement` to build and run the application.
class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title="Restaurant Management App"

# 3) Define the constructor `__init__(self, root)`:
#    a) Store the main window in `self.root`.
#    b) Set the window title to "Restaurant Management App".

# 4) Create a dictionary `self.menu_items` to store menu item names and their prices (in USD).
        self.menu_items={"Burger":5,"pizza":8,"pasta":6,"sandwich":4,"cofee":3}

# 5) Set an exchange rate `self.exchange_rate = 82`
#    to convert USD prices into INR when required.
        self.exchange_rate=82

# 6) Call `self.setup_background(root)` to load and display a background image.
        self.setup_background(root)

# 7) Create a `ttk.Frame` and place it at the center of the window:
#    (This frame holds all the order widgets.)
        self.main_frame=ttk.Frame(root,padding=20)
        self.main_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

# 8) Add a heading label "Restaurant Order Management" using `ttk.Label(...)`.
        heading=ttk.Label(self.main_frame,text="Resaturant Order Management",font=("Arial,18"))
        heading.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

# 9) Create two empty dictionaries:
#    a) `self.menu_labels` to store label widgets for each menu item.
#    b) `self.menu_quantities` to store entry widgets for quantities.
        self.menu_labels={}
        self.menu_quantities={}

# 10) Use a loop to create menu item rows:
#     a) For each item and price in `self.menu_items`:
#        i) Create a label showing item name and price.
#        ii) Create an entry box to input quantity.
#        iii) Store label references in `self.menu_labels`.
#        iv) Store entry references in `self.menu_quantities`.
        row_num=1
        for item,price in self.menu_items.items():
            label=ttk.Label(self.main_frame,text=f"{item}-${price}")
            label.grid(row=row_num,column=0,padx=10,pady=10)
            entry=ttk.Entry(self.main_frame,width=10)
            entry.grid(row=row_num,column=1,padx=10,pady=10)
            self.menu_labels[item]=label
            self.menu_quantities[item]=entry
            row_num+=1

# 11) Create a currency selection section:
#     a) Create a `StringVar` called `self.currency_var`.
#     b) Add a "Currency:" label.
#     c) Add a dropdown (`ttk.Combobox`) with options "USD" and "INR".
#     d) Set default selection to "USD".
#     e) Attach a trace to `self.currency_var` so when currency changes,
#        it automatically calls `self.update_menu_prices`.
        self.currency_var=tk.StringVar()
        currency_label=ttk.Label(self.main_frame,text="currency:")
        currency_label.grid(row=row_num,column=0,padx=10,pady=10,sticky="w")
        currency_dropdown=ttk.Combobox(self.main_frame,textvariable=self.currency_var,values=["USD","INR"],state="readonly",width=10)
        currency_dropdown.grid(row=row_num,column=1,padx=10,pady=10)
        self.currency_var.set("USD")
        self.currency_var.trace_add("write",self.update_menu_price)
        row_num+=1


# 12) Add a "Place Order" button:
#     a) When clicked, it runs `self.place_order()`.
        Order_button=ttk.Button(self.main_frame,text="Place order",command=self.place_order)
        Order_button.grid(row=row_num,column=0,columnspan=3,padx=10,pady=10)


# 13) Define `setup_background(self, root)`:
#     a) Create a Canvas of size 800x600.
#     b) Load the background image file `background.png` using `tk.PhotoImage`.
#     c) Resize it approximately using `.subsample(...)`.
#     d) Place the image on the canvas using `create_image(...)`.
#     e) Store the image reference (`canvas.image`) to prevent garbage collection.
    def setup_background(self,root):
        self.Canvas=tk.Canvas(root,width=800,height=600)
        self.Canvas.pack(fill="both",expand=True)
        bg_image=tk.PhotoImage(file="BACKGRND.png")
        bgimg=bg_image.subsample(bg_image.width(),bg_image.height())
        self.Canvas.create_image(0,0,image=bgimg,anchor="nw")
        self.Canvas.image=bgimg

# 14) Define `update_menu_prices(self, *args)`:
#     a) Read the selected currency from `self.currency_var`.
#     b) Set currency symbol:
#        - INR -> "₹"
#        - USD -> "$"
#     c) Set conversion rate:
#        - INR -> exchange rate
#        - USD -> 1
#     d) Update every menu label text to show the converted price.
    def update_menu_price(self,*args):
        currency=self.currency_var.get()
        if currency=="INR":
            symbol="₹"
        else:
            symbol="$"
        if currency=="INR":
            rate=self.exchange_rate
        else:
            rate=1
        for item,usd_price in self.menu_items.items():
            converted_price=usd_price*rate
            self.menu_labels[item].config(text=f"{item}-{symbol}{converted_price}")


# 15) Define `place_order(self)`:
#     a) Initialize `total_cost = 0` and `order_summary` message text.
#     b) Determine currency symbol and conversion rate (same as above).
#     c) Loop through each menu item entry:
#        i) Read quantity using `entry.get()`.
#        ii) If quantity is a digit, convert it to int.
#        iii) Compute price (converted), item cost, and add to total.
#        iv) If quantity > 0, add line details to `order_summary`.
#     d) If `total_cost > 0`, show the order summary in a messagebox.
#     e) Else, show an error message asking the user to order at least one item.
    def place_order(self):
        total_cost=0
        order_summary="Your Order:\n"
        currency=self.currency_var.get()
        if currency=="INR":
            symbol="₹"
            rate=self.exchange_rate
        else:
            symbol="$"
            rate=1
        for item,entry in self.menu_quantities.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.menu_items[item]*rate
                item_total=price*quantity
                total_cost+=item_total
                if quantity>0:
                    order_summary+=(f"{item}:{price}x{quantity}="
                                    f"{symbol}{item_total}\n")
            # order_summary+=f"\nTotal Cost:{symbol}{total_cost}"
        if total_cost>0:
            order_summary+=f"\nTotal Cost:{symbol}{total_cost}"
            messagebox.showinfo("Order Summary",order_summary)
            
        else:
            messagebox.showerror("Error","Pls order atleast oen item !")
# 16) In the main block (`if __name__ == "__main__":`):
#     a) Create the main window using `root = tk.Tk()`.
#     b) Create the app object `app = RestaurantOrderManagement(root)`.
#     c) Set the window size to 800x600.
#     d) Start the GUI loop using `root.mainloop()`
if __name__=="__main__":
    root=tk.Tk()
    app=RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()