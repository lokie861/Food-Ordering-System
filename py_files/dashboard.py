import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

db = sqlite3.connect('Test.db')
c= db.cursor()


class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.total_order=0
        self.totalcanceled_order=0
        self. totalcompleted_order=0
        self.temp=[]
        self.totaleraning=0

        self.frame1 = tk.Frame(master)
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(background='white', font='{avro} 16 {bold italic}', text='Admin Dashboard')
        self.label1.place(anchor='nw', x='20', y='20')

        self.pink_frame = tk.Frame(self.frame1)
        self.total_order_label = ttk.Label(self.pink_frame)
        self.total_order_label.configure(background='#fe5f77', font='{timesnew} 14 {bold italic}', foreground='white', text='Total Order')
        self.total_order_label.place(anchor='nw', x='30', y='10')
        self.total_order_number_label = ttk.Label(self.pink_frame)
        self.total_order_number_label.configure(background='#fe5f77', font='{timesnew} 20 {bold italic}', foreground='white', text='0')
        self.total_order_number_label.place(anchor='nw', x='80', y='55')
        self.pink_frame.configure(background='#fe5f77', height='120', width='200')
        self.pink_frame.place(anchor='nw', x='10', y='65')

        self.yellow_frame = tk.Frame(self.frame1)
        self.completed_order_label = ttk.Label(self.yellow_frame)
        self.completed_order_label.configure(background='#feb54d', font='{Timesnew} 14 {bold italic}', foreground='white', text='Completed Order')
        self.completed_order_label.place(anchor='nw', x='10', y='10')
        self.completed_order_number = ttk.Label(self.yellow_frame)
        self.completed_order_number.configure(background='#feb54d', font='{Timesnew} 20 {bold italic}', foreground='white', text='0')
        self.completed_order_number.place(anchor='nw', x='80', y='55')
        self.yellow_frame.configure(background='#feb54d', height='120', width='200')
        self.yellow_frame.place(anchor='nw', x='225', y='65')

        self.blue_frame = tk.Frame(self.frame1)
        self.canceled_order_label = ttk.Label(self.blue_frame)
        self.canceled_order_label.configure(background='#4099ff', font='{timesnew} 14 {bold italic}', foreground='white', text='Canceled Order ')
        self.canceled_order_label.place(anchor='nw', x='15', y='10')
        self.cancaled_number_label = ttk.Label(self.blue_frame)
        self.cancaled_number_label.configure(background='#4099ff', font='{timesnew} 20 {bold italic}', foreground='white', text='0 ')
        self.cancaled_number_label.place(anchor='nw', x='80', y='55')
        self.blue_frame.configure(background='#4099ff', height='120', width='200')
        self.blue_frame.place(anchor='nw', x='455', y='65')

        self.green_frame = tk.Frame(self.frame1)
        self.earning_label = ttk.Label(self.green_frame)
        self.earning_label.configure(background='#34eb3a', font='{timesnew} 14 {bold italic}', foreground='white',text='Total Earning ')
        self.earning_label.place(anchor='nw', x='15', y='10')
        self.earning_number_label = ttk.Label(self.green_frame)
        self.earning_number_label.configure(background='#34eb3a', font='{timesnew} 20 {bold italic}',foreground='white', text='0 ')
        self.earning_number_label.place(anchor='nw', x='80', y='55')
        self.green_frame.configure(background='#34eb3a', height='120', width='200')
        self.green_frame.place(anchor='nw', x='675', y='65')

        s=ttk.Style()
    


        self.details_treeview = ttk.Treeview(self.frame1)
        self.details_treeview['columns']=( 'Order ID','Name','Time','Ordered','Number','Status','Earning')
        self.details_treeview.place(anchor='nw', height='260', width='880', x='10', y='230')

        
        self.details_treeview.column('# 0',anchor='center',width=0,stretch=False)
        self.details_treeview.heading('# 0')
        self.details_treeview.column('# 1', anchor='center', width=35)
        self.details_treeview.heading('# 1', text='Order ID')
        self.details_treeview.column('# 2' , anchor='center',width=80) 
        self.details_treeview.heading('# 2', text='Name')
        self.details_treeview.column('# 3', anchor='center',width=45)
        self.details_treeview.heading('# 3', text='Time')
        self.details_treeview.column('# 4', anchor='center',width=325)
        self.details_treeview.heading('# 4', text='Ordered')
        self.details_treeview.column('# 5', anchor='center',width=75)
        self.details_treeview.heading('# 5', text='Number')
        self.details_treeview.column('# 6', anchor='center',width=60)
        self.details_treeview.heading('# 6', text='Status')
        self.details_treeview.column('# 7', anchor='center',width=45)
        self.details_treeview.heading('# 7',text='Earning')

        self.back_button = tk.Button(self.frame1)
        self.back_button.configure(background='black', borderwidth='0', font='{avro} 12 {italic}', foreground='white')
        self.back_button.configure(highlightthickness='0', text='Back')
        self.back_button.place(anchor='nw', x='810', y='15')
        self.back_button.configure(command=self.back)
        self.frame1.configure(background='white', height='500', width='900')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1
        #Calculation for the total number of orders

        c.execute('select Order_ID from Project;')
        for _ in c:
            self.total_order +=1

        self.total_order_number_label.config(text=f'{self.total_order}')

        #calculation for the order cancelled
        c.execute('select * from Project where Status="Canceled";')
        for _ in c :
            self.totalcanceled_order +=1
        self.cancaled_number_label.config(text=f'{self.totalcanceled_order}')

        #calculation for the number of completed order
        c.execute('select * from Project where Status="Completed";')
        for _ in c:
            self.totalcompleted_order +=1

        self.completed_order_number.config(text=f'{self.totalcompleted_order}')

        #Calculation for the total earning
        c.execute('select Earning from Project where Status="Completed"')

        for x in c:
            self.temp.append(int(x[0]))

        self.earning_number_label.config(text=f'{sum(self.temp)}')

        self.total_order=0
        self.totalcompleted_order=0
        self.totalcanceled_order=0

        c.execute('select Order_ID,Name,Time,Ordered,Number,Status,Earning from Project;')
        n=1
        for x in c:
            self.details_treeview.insert('','end',values=x)
            n= n+1

    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        self.master.destroy()


def run_dashboard():
    root1 = tk.Tk()
    root1.title('Dashboard')
    root1.resizable(height=False, width=False)
    app1 = DashboardApp(root1)
    app1.run()

