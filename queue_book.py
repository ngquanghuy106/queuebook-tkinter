# IMPORT
import tkinter as tk
from tkinter import ttk

# CONSTANTS
WIDTH = 1200
HEIGHT = 900
X_OFFSET = 50
Y_OFFSET = 50
GREEN = "#29de19"
BLUE = "#0034c4"
WHITE = "#f0f0f0"
BLACK = "#000000"

INSTRUCTION = """
Add Customer button: Add new customer with information entered in the Customer's Name box and Device's Name box

Next Customer button: Remove the oldest customer from the list
"""

# CLASSES
class QueueBook:
    def __init__(self):
            self.root = tk.Tk()
            self.root.geometry(f"{WIDTH}x{HEIGHT}+{X_OFFSET}+{Y_OFFSET}")
            self.root.title("Customer Queue Book v1.0b")

            self.customer_table = ttk.Treeview(self.root, columns=("Position", "Customer", "Device"), show="headings", height=40)

            self.customer_table.heading("Position", text="Position")
            self.customer_table.heading("Customer", text="Customer")
            self.customer_table.heading("Device", text="Device")

            self.customer_table.column("Position", width=60)
            self.customer_table.column("Customer", width=250)
            self.customer_table.column("Device", width=250)

            self.customer_table.place(x=20, y=20)

            self.queue = []

            self.queue_count_txtvar = tk.StringVar()
            self.queue_count_txtvar.set(f"Customer Waiting: {len(self.queue)}")
            self.queue_count_label = tk.Label(self.root, textvariable=self.queue_count_txtvar, font=("Arial", 24), fg=BLACK, height=1)
            self.queue_count_label.place(x=600, y=250)

            self.add_button = tk.Button(self.root, text="Add Customer", font=("Arial", 24), fg=WHITE, bg=GREEN, width=12, height=1, command=self.add_customer)
            self.add_button.place(x=600, y=20)

            self.next_button = tk.Button(self.root, text="Next Customer", font=("Arial", 24), fg=WHITE, bg=BLUE, width=12, height=1, command=self.next_customer)
            self.next_button.place(x=900, y=20)

            self.name_label = tk.Label(self.root, text="Customer's Name", font=("Arial", 24), fg=BLACK, height=1)
            self.name_label.place(x=600, y=100)
            self.name_input = tk.Entry(self.root, font=("Arial", 24), width=15)
            self.name_input.place(x=600, y=150)

            self.device_label = tk.Label(self.root, text="Device's Name", font=("Arial", 24), fg=BLACK, height=1)
            self.device_label.place(x=900, y=100)
            self.device_input = tk.Entry(self.root, font=("Arial", 24), width=15)
            self.device_input.place(x=900, y=150)

            self.error_txtvar = tk.StringVar()
            self.error_label = tk.Label(self.root, textvariable=self.error_txtvar, font=("Arial", 24), fg=BLACK, width=30, height=2, wraplength=600, justify="left", anchor="nw")
            self.error_label.place(x=600, y=800)

            self.instruction_label = tk.Label(self.root, text=INSTRUCTION, font=("Arial", 24), fg=BLACK, wraplength=600, justify="left", anchor="nw")
            self.instruction_label.place(x=600, y=350, width=600)

    def refresh_table(self):
        self.customer_table.delete(*self.customer_table.get_children())

        for customer in self.queue:
            self.customer_table.insert("", tk.END, values=customer)

        self.queue_count_txtvar.set(f"Customer Waiting: {len(self.customer_table)}")

    def add_customer(self):
        name = self.name_input.get()
        device = self.device_input.get()

        if not name.strip() or not device.strip():
            self.error_txtvar.set("ERROR!: No data in the Customer's Name or Device's Name")
            return

        if self.queue:
            last_id = self.queue[-1][0]
            current_id = last_id + 1
        else:
            current_id = 1
        
        self.queue.append((current_id, name, device))

        self.refresh_table()

        self.name_input.delete(0, tk.END)
        self.device_input.delete(0, tk.END)

        self.error_txtvar.set("")

    def next_customer(self):
        if self.queue:
            self.queue.pop(0)
        else:
            self.error_txtvar.set("ERROR!: No customers in the book")
            return

        self.refresh_table()

    def run(self):
         self.root.mainloop()

# MAIN
app = QueueBook()
app.run()