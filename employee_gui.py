from datetime import datetime
from Tkinter import *
from tkMessageBox import *
import sqlite3, sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# map classes to tables through Base Class
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    address = Column(String(250))
    city = Column(String(10))
    state = Column(String(2))
    zip = Column(Integer)
    ssn = Column(String(12))
    phone = Column(String(12))
    cell = Column(String(12))

# create engine for Session connection
engine = create_engine('sqlite:///employee.db')

# create all tables in engine ('CREATE TABLE' in raw SQL)
Base.metadata.create_all(engine)

# create configured 'Session' class
Session = sessionmaker(bind=engine)

# create session
session = Session()


class GUI:
    def __init__(self, parent):
        self.parent = parent

        # create top frame
        frame = Frame(parent)
        frame.pack(expand=YES, fill=BOTH, padx=5, pady=5)

        # create bottom frame
        btm_frame = Frame(parent, relief=SUNKEN, borderwidth=1)
        btm_frame.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=5, pady=5)

        # create datetime object
        d = datetime.today()
        date = d.strftime("%Y-%m-%d")
        

#------------------------Create Labels-------------------------------#
        

        # label to display date
        date_label = Label(btm_frame, text=date)
        date_label.pack(side=LEFT)

        # name label
        name_label = Label(frame, text="Enter Name:")
        name_label.grid(row=0, sticky=W)

        # age label
        age_label = Label(frame, text="Enter Age:")
        age_label.grid(row=1, sticky=W)

        # address label
        addr_label = Label(frame, text="Enter Address:")
        addr_label.grid(row=2, sticky=W)

        # city label
        city_label = Label(frame, text="Enter City:")
        city_label.grid(row=3, sticky=W)

        # state label
        state_label = Label(frame, text="Enter State:")
        state_label.grid(row=4, sticky=W)

        # zip code label
        zip_label = Label(frame, text="Enter Zip Code:")
        zip_label.grid(row=5, sticky=W)

        # ssn label
        ssn_label = Label(frame, text="Enter Social Security #:")
        ssn_label.grid(row=6, sticky=W)

        # phone label
        phone_label = Label(frame, text="Enter Phone #:")
        phone_label.grid(row=7, sticky=W)

        # cell label
        cell_label = Label(frame, text="Enter Cell #:")
        cell_label.grid(row=8, sticky=W)
        

#----------------------Create Vars and Entry-------------------------#
        
            
        # name variable and entry
        self.name_var = StringVar()
        self.e1 = Entry(frame, textvariable=self.name_var)
        self.e1.grid(row=0, column=1)
         
        # age variable and entry
        self.age_var =  IntVar()
        self.e2 = Entry(frame, textvariable=self.age_var)
        self.e2.grid(row=1, column=1)

        # address variable and entry
        self.address_var = StringVar()
        self.e3 = Entry(frame, textvariable=self.address_var)
        self.e3.grid(row=2, column=1)

        # city variable and entry
        self.city_var = StringVar()
        self.e4 = Entry(frame, textvariable=self.city_var)
        self.e4.insert(0, "Roanoke")        # insert default value
        self.e4.grid(row=3, column=1)

        # state variable and entry
        self.state_var = StringVar()
        self.e5 = Entry(frame, textvariable=self.state_var)
        self.e5.insert(0, "VA")             # insert default value
        self.e5.grid(row=4, column=1)

        # zip code variable and entry
        self.zip_var = IntVar()
        self.e6 = Entry(frame, textvariable=self.zip_var)
        self.e6.grid(row=5, column=1)

        # s.s.n variable and entry
        self.ssn_var = StringVar()
        self.e7 = Entry(frame, textvariable=self.ssn_var)
        self.e7.grid(row=6, column=1)

        # phone variable and entry
        self.phone_var = StringVar()
        self.e8 = Entry(frame, textvariable=self.phone_var)
        self.e8.grid(row=7, column=1)

        # cell variable and entry
        self.cell_var = StringVar()
        self.e9 = Entry(frame, textvariable=self.cell_var)
        self.e9.grid(row=8, column=1)

        # quit, search, clear, add, delete buttons
        quit_button = Button(btm_frame, text="Quit", relief=GROOVE, command=parent.destroy)
        quit_button.pack(side=RIGHT)        

        search_button = Button(btm_frame, text="Search", relief=GROOVE, command=self.search)
        search_button.pack(side=RIGHT, padx=1, pady=1)

        clear_button = Button(btm_frame, text="Clear", relief=GROOVE, command=self.clear_entries)
        clear_button.pack(side=RIGHT, padx=1, pady=1)        

        del_button = Button(btm_frame, text="Delete", relief=GROOVE, command=self.del_employee)
        del_button.pack(side=RIGHT, padx=1, pady=1)

        add_button = Button(btm_frame, text="Add", relief=GROOVE, command=self.add_data)
        add_button.pack(side=RIGHT, padx=1, pady=1)
        

    def add_data(self):        
        name = self.name_var.get()
        age = self.age_var.get()
        addr = self.address_var.get()
        city = self.city_var.get()
        state = self.state_var.get()
        zip = self.zip_var.get()
        ssn = self.ssn_var.get()
        phone = self.phone_var.get()
        cell = self.cell_var.get()
        new_person = Employee(name=name, age=age, address=addr, city=city, state=state, zip=zip, ssn=ssn, phone=phone, cell=cell)
        session.add(new_person)
        session.commit()
        session.close()
        self.callback()
        return        

    def callback(self):        
        showinfo("New Employee", "Data Added")
        self.clear_entries()
        return        

    def clear_entries(self):
        entries = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9]
        for entry in entries:
            entry.delete(0, END)
        return            

    def search(self):
        search_win = Toplevel()
        search_win.title("Employee Search")

        # add Labels for employee attributes
        id_label = Label(search_win, text="Id")
        id_label.grid(row=0, column=0, padx=2, pady=2)

        name_label = Label(search_win, text="Name")
        name_label.grid(row=0, column=1, padx=2, pady=2)

        addr_label = Label(search_win, text="Address")
        addr_label.grid(row=0, column=2, padx=2, pady=2)

        city_label = Label(search_win, text="City")
        city_label.grid(row=0, column=3, padx=2, pady=2)

        state_label = Label(search_win, text="State")
        state_label.grid(row=0, column=4, padx=2, pady=2)

        zip_label = Label(search_win, text="Zip")
        zip_label.grid(row=0, column=5, padx=2, pady=2)

        ssn_label = Label(search_win, text="SSN")
        ssn_label.grid(row=0, column=6, padx=2, pady=2)

        cell_label = Label(search_win, text="Cell")
        cell_label.grid(row=0, column=7, padx=2, pady=2)

        phone_label = Label(search_win, text="Phone")
        phone_label.grid(row=0, column=8, padx=2, pady=2)

        # search all employees, put each emp. in Entry Widget with For Loop
        res = session.query(Employee).all()
        row = 1
        column = 0
        for employee in res:
            txt = [employee.id, employee.name, employee.address, employee.city, employee.state, employee.zip, employee.ssn, employee.phone, employee.cell]
            for t in txt:
                ent = Entry(search_win, relief=RIDGE, width=19)
                ent.grid(row=row, column=column, sticky=W, padx=1, pady=1)
                ent.insert(0, t)
                column += 1
            row += 1
            column = 0
        return

    def del_employee(self):
        del_win = Toplevel()
        del_win.title("Delete Employee")

        id_label = Label(del_win, text="Enter Employee Id:")
        id_label.grid(row=0, column=0, padx=5, pady=5)

        self.employee_id = IntVar()
        self.e10 = Entry(del_win, textvariable=self.employee_id)
        self.e10.grid(row=0, column=1, padx=5, pady=5)

        del_button = Button(del_win, text="Delete Employee", relief=GROOVE, command=self.erase)
        del_button.grid(row=0, column=2, padx=5, pady=5)
        return

    def erase(self):
        emp_id = self.employee_id.get()
        res = session.query(Employee).filter(Employee.id==emp_id).first()
        session.delete(res)
        session.commit()
        showinfo("Employee", "Data Deleted")
        return
        
        

if __name__ == '__main__':
    root = Tk()
    root.geometry("310x270")
    root.title("Employee Info")
    mygui = GUI(root)
    root.mainloop()


##def search(self):
##        search_win = Toplevel()
##        search_win.title("Employee Search")
##
##        # create labels for each employee attribute
##        attr = ["Id","Name","Address","City","State","Zip","SSN","Cell","Phone"]
##        column = 0
##        for a in attr:
##                Label(search_win, text=a).grid(row=0,column=column,padx=2, pady=2)
##                column += 1
##
##        # search all employees, put each emp. in Entry Widget with For Loop
##        res = session.query(Employee).all()
##        row = 1
##        column = 0
##        for employee in res:
##            txt = [employee.id, employee.name, employee.address, employee.city, employee.state, employee.zip, employee.ssn, employee.phone, employee.cell]
##            for t in txt:
##                ent = Entry(search_win, relief=RIDGE, width=19)
##                ent.grid(row=row, column=column, sticky=W, padx=1, pady=1)
##                ent.insert(0, t)
##                column += 1
##            row += 1
##            column = 0
##        return



## old search method
##def search(self):
##        search_win = Toplevel()
##        search_win.title("Employee Search")        
##
##        # search all employees, put each emp. in label with For Loop
##        res = session.query(Employee).all()
##        row = 0
##        for employee in res:
##            txt = "{0}) - Name: {1}, Address: {2}, City: {3}, State: {4}, Zip: {5}, SSN: {6}, Phone: {7}, Cell: {8}".format(employee.id, employee.name,employee.address,employee.city,employee.state, employee.zip, employee.ssn, employee.phone, employee.cell)
##            ent = Entry(search_win, relief=RIDGE, width=150)
##            ent.grid(row=row, column=0, columnspan=2, sticky=W, padx=5, pady=5)
##            ent.insert(0, txt)
##            row += 1
##        return
