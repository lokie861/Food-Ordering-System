import tkinter as tk
import sqlite3
from tkinter import messagebox

db = sqlite3.connect('Test.db')
c= db.cursor()

class CancelApp:
    def __init__(self, master):
        # build ui
        self.x=int()
        self.master = master
        self.cancel_frame = tk.Frame(master)
        self.label1 = tk.Label(self.cancel_frame)
        self.label1.configure(background='white', font='{avro} 20 {bold italic}', text='Cancel Order')
        self.label1.place(anchor='nw', x='30', y='45')
        self.orderid_label = tk.Label(self.cancel_frame)
        self.orderid_label.configure(background='white', font='{avro} 16 {italic}', text='Enter Order ID: ')
        self.orderid_label.place(anchor='nw', x='30', y='150')
        self.order_id_tobe_cancel_entry = tk.Entry(self.cancel_frame)
        self.order_id_tobe_cancel_entry.configure(font='{avro} 16 {}')
        self.order_id_tobe_cancel_entry.place(anchor='nw', x='250', y='150')
        self.cancel_order_botton = tk.Button(self.cancel_frame)
        self.cancel_order_botton.configure(background='black', font='{avro} 12 {italic}', foreground='white', text='Cancel Order')
        self.cancel_order_botton.place(anchor='nw', x='500', y='300')
        self.cancel_order_botton.configure(command=self.cancel_order)
        self.label3 = tk.Label(self.cancel_frame)
        self.label3.configure(background='white', font='{avro} 12 {italic}', text='Note :')
        self.label3.place(anchor='nw', x='30', y='350')
        self.label4 = tk.Label(self.cancel_frame)
        self.label4.configure(background='white', font='{avro} 12 {italic}', text='Once the order cancelled can not be replaced ')
        self.label4.place(anchor='nw', x='60', y='390')
        self.back_button = tk.Button(self.cancel_frame)
        self.back_button.configure(background='black', font='{avro} 12 {italic}', foreground='white', text='Back')
        self.back_button.place(anchor='nw', x='590', y='15')
        self.back_button.configure(command=self.back)
        self.cancel_frame.configure(background='white', height='500', width='700')
        self.cancel_frame.pack(side='top')

        # Main widget
        self.mainwindow = self.cancel_frame
    
    def run(self):
        self.mainwindow.mainloop()

    def cancel_order(self):
        try:
            self.x=self.order_id_tobe_cancel_entry.get()
            _=messagebox.askokcancel('Warning','Once Deleted cannot be restored..\t\n')
            if _:
                c.execute(f'update Project set Status="Canceled" where Order_ID={self.x};')
                c.execute('commit;')
                self.order_id_tobe_cancel_entry.delete(0,'end')

        except Exception as e:
            messagebox.showwarning('Warning',f'No such Order ID Please an valid Order Id.\n{e}')
            self.order_id_tobe_cancel_entry.delete(0,'end')
            print(e)

    def back(self):
        self.master.destroy()

def run_cancel():
    root4 = tk.Tk()
    root4.title('Cancel Order')
    root4.resizable(height=False, width=False)
    app4 = CancelApp(root4)
    app4.run()

