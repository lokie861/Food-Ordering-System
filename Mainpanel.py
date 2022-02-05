import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import os

from py_files.neworder import run
from py_files.dashboard import run_dashboard
from py_files.cancel_order import run_cancel

#SETTING THE IMAGE LOCATION
location=os.getcwd()
location=f'{location}/images/'
print(location)
#DATABASE CONNECTIONS
db = sqlite3.connect('Test.db')
#MAKING THE CURSOR TO EXECUTE THE  SQL COMMANDS
c= db.cursor()

#CREATING THE DATABASE FOR STORING THINGS
#EXECUTE THIS ONLY ONCE AT THE INSTALLATION STEP
#c.execute('create table Project(Order_ID INTEGER primary key autoincrement , Name varchar(50), Time timestamp ,Ordered varchar(700),Number varchar(13),Status varchar(10), Earning varchar(6), Email varchar(50),Address varchar(80));')


class MainPanelApp:
    def __init__(self, master):
        # build ui
        global location

        self.frame1 = tk.Frame(master)
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(background='white', font='{avro} 20 {bold italic}', text='Food Ordering System')
        self.label1.place(anchor='nw', x='30', y='15')
        self.dash_button = tk.Button(self.frame1)
        self.img_dash = tk.PhotoImage(file=f'{location}dash.png')
        self.dash_button.configure(borderwidth='0', highlightthickness='0', image=self.img_dash)
        self.dash_button.place(anchor='nw', x='50', y='120')
        self.dash_button.configure(command=self.call_dashboard)
        self.cancel_button = tk.Button(self.frame1)
        self.img_cancel = tk.PhotoImage(file=f'{location}cancel.png')
        self.cancel_button.configure(borderwidth='0', highlightthickness='0', image=self.img_cancel)
        self.cancel_button.place(anchor='nw', x='495', y='120')
        self.cancel_button.configure(command=self.call_cancelorder)
        self.neworder_button = tk.Button(self.frame1)
        self.img_new = tk.PhotoImage(file=f'{location}new.png')
        self.neworder_button.configure(borderwidth='0', highlightthickness='0', image=self.img_new)
        self.neworder_button.place(anchor='nw', x='275', y='120')
        self.neworder_button.configure(command=self.call_neworder)
        self.dash_label = ttk.Label(self.frame1)
        self.dash_label.configure(background='white', font='{avro} 12 {italic}', text='Admin Dashboard')
        self.dash_label.place(anchor='nw', x='55', y='300')
        self.new_label = ttk.Label(self.frame1)
        self.new_label.configure(background='white', font='{avro} 12 {italic}', text='New Order')
        self.new_label.place(anchor='nw', x='310', y='300')
        self.cancel_label = ttk.Label(self.frame1)
        self.cancel_label.configure(background='white', font='{avro} 12 {italic}', text='Cancel Order')
        self.cancel_label.place(anchor='nw', x='525', y='300')
        self.label5 = ttk.Label(self.frame1)
        self.label5.configure(background='white', text='Note:')
        self.label5.place(anchor='nw', x='10', y='400')
        self.label6 = ttk.Label(self.frame1)
        self.label6.configure(background='white', text='> Only Authorised can access the Adim Dashboard')
        self.label6.place(anchor='nw', x='35', y='425')
        self.label7 = ttk.Label(self.frame1)
        self.label7.configure(background='white', text='> To order food use new order')
        self.label7.place(anchor='nw', x='35', y='450')
        self.label8 = ttk.Label(self.frame1)
        self.label8.configure(background='white', text='> To cancel the placed order use cancel order')
        self.label8.place(anchor='nw', x='35', y='475')
        self.frame1.configure(background='white', height='500', width='700')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1
    
    def run(self):
        self.mainwindow.mainloop()

    @staticmethod
    def call_dashboard():
        run_dashboard()

    @staticmethod
    def call_cancelorder():
        run_cancel()

    @staticmethod
    def call_neworder():
        run()

'''def run_mainpanel():
    root = tk.Tk()
    app = MainPanelApp(root)
    app.run()'''


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Main Page')
    root.resizable(height=False, width=False)
    app = MainPanelApp(root)
    app.run()

