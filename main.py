from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as mysql


class Retailstore:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)
        self.root.title("Retail Store Management System")
        p1 = PhotoImage(file='monitor.png')
        self.root.iconphoto(False,p1)


    def mainWindow(self):
        self.mainFrame = Frame()
        self.mainFrame.place(x=0, y=0, width=1350, height=700)

        self.mainFrame.config(bg="ghostwhite")

        title = Label(self.mainFrame, text="THE GADGET STORE",
                      font=("Roboto", 26, "bold"), bg="#003366",fg="white")
        title.pack(side=TOP, fill=X)

        frame1 = Frame(self.mainFrame, bd=4, relief=RIDGE, bg="aliceblue")
        frame1.place(x=30, y=75, width=450, height=600)

        frame2 = Frame(self.mainFrame, bd=4, relief=RIDGE, bg="aliceblue")
        frame2.place(x=520, y=75, width=795, height=600)

        heading = Label(frame1, text="INVOICE", font=(
            "Roboto", 20, "bold"), bg="aliceblue")
        # heading.pack(side=TOP,fill=X,pady=20)
        heading.grid(row=0, columnspan=2, pady=20)


# ====================left frame========

        self.customer_id = StringVar()
        self.customer_name = StringVar()
        self.product_type = StringVar()
        self.product_name = StringVar()
        self.price = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

        cust_id = Label(frame1, text="Customer ID:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        cust_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        input_cust_id = Entry(frame1, textvariable=self.customer_id, font=(
            "Roboto", 13), bd=4, relief=GROOVE)
        input_cust_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        cust_name = Label(frame1, text="Customer Name:",
                          font=("Roboto", 13, "bold"), bg="aliceblue")
        cust_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        input_cust_name = Entry(frame1, textvariable=self.customer_name, font=(
            "Roboto", 13), bd=4, relief=GROOVE)
        input_cust_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")



        product_name = Label(frame1, text="Product Name:",
                             font=("Arial", 13, "bold"), bg="aliceblue")
        product_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        input_prod_name = Entry(frame1, textvariable=self.product_name, font=(
            "Roboto", 13), bd=4, relief=GROOVE)
        input_prod_name.grid(row=3, column=1, pady=10, padx=20, sticky="w")



        product_id = Label(frame1, text="Product Type:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        product_id.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        # input_prod_id = Entry(frame1, textvariable=self.product_id, font=(
        #     "Arial", 13), bd=4, relief=GROOVE)
        # input_prod_id.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        input_prod_id = ttk.Combobox(frame1,textvariable=self.product_type,state="readonly",font=("Roboto", 11))
        input_prod_id['values']=("Mobile Devices", "Wearables", "Laptops/Computers", "TV/Monitors", "Appliances/White goods")
        input_prod_id.grid(row=4,column=1, pady=10, padx=20,sticky="w")

        price = Label(frame1, text="Price:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        price.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        input_price = Entry(frame1, textvariable=self.price,
                            font=("Roboto", 13), bd=4, relief=GROOVE)
        input_price.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        address = Label(frame1, text="Address:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.input_address = Text(frame1, font=(
            "Roboto", 13), bd=4, relief=GROOVE, width=20, height=4)
        self.input_address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        phone = Label(frame1, text="Phone No.:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        phone.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        input_phone = Entry(frame1, textvariable=self.phone,
                            font=("Roboto", 13), bd=4, relief=GROOVE)
        input_phone.grid(row=7, column=1, pady=10, padx=20, sticky="w")

    # -----------Buttons Left Frame-----------------
        btn_frame = Frame(self.root)
        btn_frame.config(bg="aliceblue")
        btn_frame.place(x=50, y=580, width=400)

        submit_btn = Button(btn_frame, text="SUBMIT", command=self.insert, width=10, height=2, font=("Roboto", 9, "bold"), bg="#003366", fg="white")
        submit_btn.grid(row=0, column=0, padx=10, pady=10)

        upate_btn = Button(btn_frame, text="UPDATE", command=self.update,
                          font=("Roboto", 9, "bold"), width=10, height=2, bg="#003366", fg="white")
        upate_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text="DELETE", command=self.delete,
                            font=("Roboto", 9, "bold"),width=10, height=2, bg="#FF0000", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        clear_btn = Button(btn_frame, text="CLEAR",
                          font=("Roboto", 9, "bold"), command=self.clear, width=10, height=2, bg="#fffff0")
        clear_btn.grid(row=0, column=3, padx=10, pady=10)

# ====================right frame===========

        search = Label(frame2, text="Search By:", font=(
            "Roboto", 13, "bold"), bg="aliceblue")
        search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        search_combo = ttk.Combobox(frame2, width=15, textvariable=self.search_by, font=(
            "Roboto", 13), state="readonly")
        search_combo['values'] = (
            "customer_id", "customer_name", "product_name")
        search_combo.grid(row=0, column=1, padx=5, pady=10)

        txt_search = Entry(frame2, font=("Roboto", 13),
                           textvariable=self.search_text, bd=4, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=5, sticky="w")

        search_btn = Button(frame2, text="SEARCH", command=self.search, font=(
            "Roboto", 9,"bold"), width=10, height=2, bg="#fffff0")
        search_btn.grid(row=0, column=3, padx=6, pady=10)

        showall_btn = Button(frame2, text="VIEW ALL", command=self.fetch, font=(
            "Roboto", 9,"bold"), width=10, height=2, bg="#fffff0")
        showall_btn.grid(row=0, column=4, padx=6, pady=10)

        logou_btn = Button(frame2, text="LOG OUT", command=self.loginWindow, font=(
            "Roboto", 9,"bold"), width=10, height=2, bg="black", fg="white")
        logou_btn.grid(row=0, column=5, padx=6, pady=10)

        # --------------Table Frame----------
        table_frame = Frame(frame2, bd=4, relief=RIDGE)
        table_frame.place(x=15, y=75, width=755, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.details_table = ttk.Treeview(table_frame, columns=("customerId", "customer_name", "product_name",
                                                                "product_type", "price", "address", "phone_no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("customerId", text="CUSTOMER ID")
        self.details_table.heading("customer_name", text="NAME")
        self.details_table.heading("product_name", text="PRODUCT")
        self.details_table.heading("product_type", text="PRODUCT TYPE")
        self.details_table.heading("price", text="PRICE")
        self.details_table.heading("address", text="ADDRESS")
        self.details_table.heading("phone_no", text="PHONE NO.")
        self.details_table['show'] = 'headings'

        self.details_table.column("customerId", width=90)
        self.details_table.column("customer_name", width=130)
        self.details_table.column("product_name", width=130)
        self.details_table.column("product_type", width=100)
        self.details_table.column("price", width=100)
        self.details_table.column("address", width=148)
        self.details_table.column("phone_no", width=148)
        self.details_table.bind("<ButtonRelease>", self.cursor_point)
        self.details_table.pack(fill=BOTH, expand=1)

        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="retailstore"

        )

        self.cursObj = self.mydb.cursor()

    def insert(self):
        if self.customer_id.get() == "" and self.customer_name.get() == "" and self.product_name.get() == "" and self.product_type.get() == "" and self.price.get() == "" and self.address.get() == "" and self.phone.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursObj.execute("""insert into customer_details(customer_id,customer_name,product_name,product_type,
                price,address,phone)values(%s,%s,%s,%s,%s,%s,%s);""", (self.customer_id.get(),
                                                                       self.customer_name.get(),
                                                                       self.product_name.get(),
                                                                       self.product_type.get(),
                                                                       self.price.get(),
                                                                       self.input_address.get(
                                                                           "1.0", END),
                                                                       self.phone.get()
                                                                       ))

                self.mydb.commit()

                messagebox.showinfo("Success", "Entry added Successfully")
                self.fetch()
                self.clear()
            except:
                messagebox.showerror(
                    "Error", "Something went wrong. Please Try Again")

    def fetch(self):
        self.cursObj.execute(
            "select customer_id,customer_name,product_name,product_type,price,address,phone from customer_details")
        rows = self.cursObj.fetchall()
        if len(rows) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for row in rows:
                self.details_table.insert('', END, values=row)
            self.mydb.commit()

    def clear(self):
        self.customer_id.set(""),
        self.customer_name.set(""),
        self.product_name.set(""),
        self.product_type.set(""),
        self.price.set(""),
        self.input_address.delete("1.0", END),
        self.phone.set("")

    def cursor_point(self, event):
        cursor_row = self.details_table.focus()
        self.contents = self.details_table.item(cursor_row)
        row = self.contents['values']
        self.customer_id.set(row[0]),
        self.customer_name.set(row[1]),
        self.product_name.set(row[2]),
        self.product_type.set(row[3]),
        self.price.set(row[4]),
        self.input_address.delete("1.0", END),
        self.input_address.insert(END, row[5]),
        self.phone.set(row[6])

    def update(self):
        if not (self.details_table.focus() and self.contents['values']):
            messagebox.showerror("Error", "No entry selected")
        else:
            self.cursObj.execute("""update customer_details set customer_name=%s,product_name=%s,
            product_type=%s,price=%s,address=%s,phone=%s where customer_id=%s""", (
                self.customer_name.get(),
                self.product_name.get(),
                self.product_type.get(),
                self.price.get(),
                self.input_address.get("1.0", END),
                self.phone.get(),
                self.customer_id.get()))
            self.mydb.commit()
            messagebox.showinfo("Success", "Entry Updated Successfully")
            self.fetch()
            self.clear()

    def delete(self):
        if not (self.details_table.focus()):
            messagebox.showerror("Error", "No entry selected")
        else:
            self.cursObj.execute(
                "delete from customer_details where customer_id = %s", (self.customer_id.get(),))
            res = messagebox.askquestion(
                "Entry Delete", "Are you sure you want to delete this Entry?")
            if res == "yes":
                self.mydb.commit()
                self.fetch()
                self.clear()

    def search(self):
        if (self.search_by.get() == "" and self.search_text.get() == "") or (self.search_by.get() != "" and self.search_text.get() == "") or (self.search_by.get() == "" and self.search_text.get() != ""):
            messagebox.showerror("Error", "Select correct options")
        else:
            self.cursObj.execute("select customer_id,customer_name,product_name,product_type,price,address,phone from customer_details where " +
                                str(self.search_by.get())+" like '%"+str(self.search_text.get())+"%'")
            rows = self.cursObj.fetchall()
            if len(rows) != 0:
                self.details_table.delete(*self.details_table.get_children())
                for row in rows:
                    self.details_table.insert('', END, values=row)
                self.mydb.commit()

    def loginWindow(self):
        f1 = Frame(self.root)
        f1.place(x=0, y=0, width=1350, height=700)
        self.data = StringVar()
        self.data_password = StringVar()

        # BACKGROUND IMAGE
        img_label = Label(f1)
        img_label.image = PhotoImage(file="Frame2.png")
        img_label['image'] = img_label.image
        
        # img_label.pack()
        img_label.place(x=0, y=0, width=1350, height=700)
        store_title = Label(text="THE GADGET STORE",font=(
            "Roboto", 40, "bold"), bg="#181B23", fg="white")
        store_title.pack(side=TOP,fill=X)

        username = Label(text="Username:", font=(
            "Roboto", 12, "bold"), bg="#181B1F", fg="white")
        username.place(x=600, y=270)
        username_input = Entry(textvariable=self.data,
                               font=("Roboto", 10, "bold"))
        username_input.place(x=600, y=300, width=200, height=25)

        password = Label(text="Password:", font=(
            "Roboto", 12, "bold"), bg="#181B1F", fg="white")
        password.place(x=600, y=340)
        password_input = Entry(
            textvariable=self.data_password, show="*", font=("Arial", 10, "bold"))
        password_input.place(x=600, y=370, width=200, height=25)

        loginButton = Button(text="SIGN IN", command=self.validate,
                             bg="#246bfa", fg="white", font=("Roboto", 9, "bold"))
        loginButton.place(x=600, y=430, width=100, height=40)

    def validate(self):
        loginData = self.data.get()
        loginDataPassword = self.data_password.get()

        if loginData == 'admin' and loginDataPassword == 'admin':
            messagebox.showinfo("Success", "Successfully Logged-in")
            self.mainWindow()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


root = Tk()
obj = Retailstore(root)
obj.loginWindow()
root.mainloop()
