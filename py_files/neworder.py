import tkinter as tk
import  sqlite3
import tkinter.ttk as ttk
from tkinter import messagebox

global app2
orders={}
db = sqlite3.connect('Test.db')
c= db.cursor()

Total=int()
Ordered_price=[]
Orders=str()
fullform={'cb': 'Chicken Briyani ', 'vb':'Veg Briyani    ','mb': 'Mutton Briyani  ','t':'Tea            ','gt':'Green Tea      ','bt':'Black Tea      ','cof':'Coffee         ',
          'ep':'Egg Puff       ','cp':'Chicken Puff   ','vp':'Veg Puff       ','sam':'Samosa         ','rm':'Rose Milk      ','wm':'WaterMelon     ','fm':'Fruit Mix      ',
          'frooti':'Frooti         '}

Price={'cb':60,'vb':40,'mb':60,'t':15,'bt':15,'cof':15,'gt':15,'sam':12,'cp':18,'vp':10,'ep':12,'wm':20,'rm':25,'frooti':20,'fm':15}





class NeworderApp:
    def __init__(self, master=None):
        # build ui
        global Orders, Ordered_price
        self.bill=f"{'NO':<5} {'Food':<16} {'Count':^7} {'Price':<6}\n"
        self.temp=str()
        self.order_id=int()
        self.name = ' '
        self.address=' '
        self.number= ' '
        self.email=' '
        self.command= " "
        self.ordered=' '
        self.short_form=[]
        self.food = list()
        self.count = list()
        self.indprice = list()
        self.price = list()

        self.master=master
        self.neworder = tk.Frame(master)
        self.neworder_label = tk.Label(self.neworder)
        self.neworder_label.configure(background='white', font='{Timesnew} 16 {bold italic}', text='New Order')
        self.neworder_label.place(anchor='nw', x='25', y='30')
        self.firstname_label = tk.Label(self.neworder)
        self.firstname_label.configure(background='white', font='{avro} 12 {italic}', text='First Name :')
        self.firstname_label.place(anchor='nw', x='55', y='90')
        self.lastname_abel = tk.Label(self.neworder)
        self.lastname_abel.configure(background='white', font='{avro} 12 {italic}', text='Last Name :')
        self.lastname_abel.place(anchor='nw', x='55', y='140')
        self.address_label = tk.Label(self.neworder)
        self.address_label.configure(background='white', font='{avro} 12 {italic}', text='Address    :')
        self.address_label.place(anchor='nw', x='55', y='190')
        self.state_label = tk.Label(self.neworder)
        self.state_label.configure(background='white', font='{avro} 12 {italic}', text='State   :')
        self.state_label.place(anchor='nw', x='55', y='240')
        self.postal_label = tk.Label(self.neworder)
        self.postal_label.configure(background='white', font='{avro} 12 {italic}', text='Postal Code :')
        self.postal_label.place(anchor='nw', x='55', y='290')
        self.email_label = tk.Label(self.neworder)
        self.email_label.configure(background='white', font='{avro} 12 {italic}', text='Email :')
        self.email_label.place(anchor='nw', x='55', y='390')
        self.number_label = tk.Label(self.neworder)
        self.number_label.configure(background='white', font='{avro} 12 {italic}', text='Number :')
        self.number_label.place(anchor='nw', x='55', y='340')
        self.firstname_entry = tk.Entry(self.neworder)
        self.firstname_entry.configure(font='{AVRO} 12 {italic}')
        self.firstname_entry.place(anchor='nw', x='210', y='90')
        self.lastname_entry = tk.Entry(self.neworder)
        self.lastname_entry.configure(font='{AVRO} 12 {italic}')
        self.lastname_entry.place(anchor='nw', x='210', y='140')
        self.address_entry = tk.Entry(self.neworder)
        self.address_entry.configure(font='{AVRO} 12 {italic}')
        self.address_entry.place(anchor='nw', x='210', y='190')
        self.state_entry = tk.Entry(self.neworder)
        self.state_entry.configure(font='{AVRO} 12 {italic}')
        self.state_entry.place(anchor='nw', x='210', y='240')
        self.postal_entry = tk.Entry(self.neworder)
        self.postal_entry.configure(font='{AVRO} 12 {italic}')
        self.postal_entry.place(anchor='nw', x='210', y='290')
        self.number_entry = tk.Entry(self.neworder)
        self.number_entry.configure(font='{AVRO} 12 {italic}')
        self.number_entry.place(anchor='nw', x='210', y='340')
        self.email_entry = tk.Entry(self.neworder)
        self.email_entry.configure(font='{AVRO} 12 {italic}')
        self.email_entry.place(anchor='nw', x='210', y='390')
        self.back_button = tk.Button(self.neworder)
        self.back_button.configure(background='black', borderwidth='0', font='{avro} 12 {bold}', foreground='white')
        self.back_button.configure(highlightthickness='0', text='Back')
        self.back_button.place(anchor='nw', x='600', y='30')
        self.back_button.configure(command=self.back)
        self.placeorder_button = tk.Button(self.neworder)
        self.placeorder_button.configure(background='black', borderwidth='0', font='{avro} 12 {bold}', foreground='white')
        self.placeorder_button.configure(highlightthickness='0', text='Place Order')
        self.placeorder_button.place(anchor='nw', x='550', y='390')
        self.placeorder_button.configure(command=self.pace_order)
        self.ordered_label = tk.Label(self.neworder)
        self.ordered_label.configure(background='white', font='{avro} 12 {italic}', text='Ordered:')
        self.ordered_label.place(anchor='nw', x='450', y='140')
        self.ordered_text = tk.Text(self.neworder)
        self.ordered_text.configure(height='10', width=50)
        self.ordered_text.place(anchor='nw', width='250', x='450', y='160')
        self.menu_button = tk.Button(self.neworder)
        self.menu_button.configure(background='black', borderwidth='0', font='{avro} 12 {bold}', foreground='white')
        self.menu_button.configure(highlightthickness='0', text='Menu')
        self.menu_button.place(anchor='nw', x='450', y='90')
        self.menu_button.configure(command=self.open_menu)
        self.neworder.configure(background='white', height='500', width='720')
        self.neworder.pack(side='top')

        # Main widget
        self.mainwindow = self.neworder
    
    def open_menu(self):
        root3 = tk.Tk()
        root3.title('Menu')
        root3.resizable(height=False, width=False)
        app3 = MenuApp(root3)
        
        app3.run()

    def run(self):
        self.mainwindow.mainloop()


    def back(self):
        self.master.destroy()
    def insert_order(self):
        self.ordered_text.insert(1.0,f'{Orders[2:]}')

    def pace_order(self):
        self.name= f'{self.firstname_entry.get()} {self.lastname_entry.get()}'
        self.address = f'{self.address_entry.get()} {self.state_entry.get()} {self.postal_entry.get()}'
        self.email=self.email_entry.get()
        self.number= self.number_entry.get()
        self.ordered= self.ordered_text.get('1.0','end')
        if self.firstname_entry.get() == '' or self.lastname_entry.get() == "" or self.address_entry.get() =='' or self.state_entry.get() == '' or self.postal_entry.get() == '' or self.email_entry.get() == '' or self.number_entry.get() == '' or self.ordered_text.get('1.0','end') ==' ':
            messagebox.showinfo('Information', 'Make sure all the feilds are filled.\n')
        elif len(self.ordered_text.get('1.0','end')) == 1:
            messagebox.showinfo('Information','Use the menu button to open the menu.')
        else:

            for x in orders.keys():
                self.food.append(f'{fullform[x].replace(" ","")},')
                self.count.append(int(orders[x]))
                self.indprice.append(Price[x])

            print(len(self.food))
            print(len(self.count))
            print(len(self.indprice))

            '''for x in range(len(orders)):
                self.bill=self.bill + f"{x+1:<5} {self.food[x]:<16} {self.count[x]:^7} {self.count[x]*self.indprice[x]:<6} \n"'''

            for x in range(len(orders)):

                self.bill=self.bill + f'''{x+1:<5} {self.food[x]:<20} {self.count[x]:^7} {self.count[x]*self.indprice[x]:<6}\n'''
                #self.bill= self.bill + "{:<5} {:-<20} {:+<7} {:*<6}".format(x+1,self.food[x],self.count[x],self.count[x]*self.indprice)
            for x in range(len(self.count)):
                self.price.append(self.count[x]*self.indprice[x])

            self.bill =self.bill + f'\nTotal amount to be paid is {sum(self.price)}'

            print(self.bill)
            self.temp=self.ordered[:len(self.ordered)-1].replace(",",'')
            c.execute(f"insert into Project(Name,Time,Ordered,Number,Status,Earning,Email,Address) values('{self.name}',Time('now'),'{self.temp}','{self.number}','Completed','{sum(Ordered_price)}','{self.email}','{self.address}');")

            c.execute(f'select Order_ID from Project where Name="{self.name}";')
            for x in c:
                self.order_id = x[0]

            messagebox.showinfo('Info', f'Details Added {self.name} And your Order Id is {self.order_id}\t\t\t\t\t\t\n\nYour Bill is \n{self.bill}')

            self.firstname_entry.delete(0, 'end')
            self.lastname_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.postal_entry.delete(0, 'end')
            self.state_entry.delete(0, 'end')
            self.number_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.ordered_text.delete(1.0, 'end')
            c.execute('commit;')

class MenuApp(NeworderApp):
    def __init__(self, master):
        # build ui
        global orders, Orders, app2
        app2.ordered_text.delete('1.0','end')

        self.master = master
        self.main = tk.Frame(master)
        self.menu_label = ttk.Label(self.main)
        self.menu_label.configure(background='white', font='{Avro} 24 {italic}', text='Menu')
        self.menu_label.place(anchor='nw', x='15', y='10')
        self.back_button = tk.Button(self.main)
        self.back_button.configure(background='black', font='{avro} 12 {bold italic}', foreground='white', text='Back')
        self.back_button.place(anchor='nw', x='575', y='10')
        self.back_button.configure(command=self.back)
        self.Lunch_label = ttk.Label(self.main)
        self.Lunch_label.configure(background='white', font='{Avro} 20 {italic}', text='Lunch')
        self.Lunch_label.place(anchor='nw', x='35', y='70')
        self.snacks_label = ttk.Label(self.main)
        self.snacks_label.configure(background='white', font='{Avro} 20 {italic}', text='Snacks')
        self.snacks_label.place(anchor='nw', x='375', y='70')
        self.beverages_label = ttk.Label(self.main)
        self.beverages_label.configure(background='white', font='{Avro} 20 {italic}', text='Beverages')
        self.beverages_label.place(anchor='nw', x='35', y='265')
        self.juice_label = ttk.Label(self.main)
        self.juice_label.configure(background='white', font='{Avro} 20 {italic}', text='Juice')
        self.juice_label.place(anchor='nw', x='375', y='265')
        self.vb_price = tk.Label(self.main)
        self.vb_price.configure(background='white', font='{avro} 12 {italic}', text='40 RS')
        self.vb_price.place(anchor='nw', x='245', y='110')
        self.cb_price = tk.Label(self.main)
        self.cb_price.configure(background='white', font='{avro} 12 {italic}', text='60 RS')
        self.cb_price.place(anchor='nw', x='245', y='150')
        self.mb_price = tk.Label(self.main)
        self.mb_price.configure(background='white', font='{avro} 12 {italic}', text='60 RS')
        self.mb_price.place(anchor='nw', x='245', y='190')
        self.bt_price = tk.Label(self.main)
        self.bt_price.configure(background='white', font='{avro} 12 {italic}', text='15 RS')
        self.bt_price.place(anchor='nw', x='245', y='320')
        self.cof_price = tk.Label(self.main)
        self.cof_price.configure(background='white', font='{avro} 12 {italic}', text='15 RS')
        self.cof_price.place(anchor='nw', x='245', y='360')
        self.t_price = tk.Label(self.main)
        self.t_price.configure(background='white', font='{avro} 12 {italic}', text='15 RS')
        self.t_price.place(anchor='nw', x='245', y='400')
        self.gt_price = tk.Label(self.main)
        self.gt_price.configure(background='white', font='{avro} 12 {italic}', text='15 RS')
        self.gt_price.place(anchor='nw', x='245', y='440')
        self.cp_price = tk.Label(self.main)
        self.cp_price.configure(background='white', font='{avro} 12 {italic}', text='18 RS')
        self.cp_price.place(anchor='nw', x='600', y='110')
        self.vp_price = tk.Label(self.main)
        self.vp_price.configure(background='white', font='{avro} 12 {italic}', text='10 RS')
        self.vp_price.place(anchor='nw', x='600', y='150')
        self.eg_price = tk.Label(self.main)
        self.eg_price.configure(background='white', font='{avro} 12 {italic}', text='12 RS')
        self.eg_price.place(anchor='nw', x='600', y='190')
        self.sam_price = tk.Label(self.main)
        self.sam_price.configure(background='white', font='{avro} 12 {italic}', text='12 RS')
        self.sam_price.place(anchor='nw', x='600', y='230')
        self.wm_price = tk.Label(self.main)
        self.wm_price.configure(background='white', font='{avro} 12 {italic}', text='20 RS')
        self.wm_price.place(anchor='nw', x='600', y='320')
        self.rm_price = tk.Label(self.main)
        self.rm_price.configure(background='white', font='{avro} 12 {italic}', text='15 RS')
        self.rm_price.place(anchor='nw', x='600', y='360')
        self.frooti_price = tk.Label(self.main)
        self.frooti_price.configure(background='white', font='{avro} 12 {italic}', text='20 RS')
        self.frooti_price.place(anchor='nw', x='600', y='400')
        self.fm_price = tk.Label(self.main)
        self.fm_price.configure(background='white', font='{avro} 12 {italic}', text='20 RS')
        self.fm_price.place(anchor='nw', x='600', y='440')
        self.ok_button = tk.Button(self.main)
        self.ok_button.configure(background='black', font='{avro} 12 {}', foreground='white', highlightthickness='0')
        self.ok_button.configure(text='   OK   ')
        self.ok_button.place(anchor='nw', x='660', y='480')
        self.ok_button.configure(command=self.ok)
        self.vb_spinbox = tk.Spinbox(self.main)
        self.vb_spinbox.configure(from_=0, increment=1, to=99, width=5)
        self.vb_spinbox.place(anchor='nw', x='300', y='110')
        self.cb_spinbox = tk.Spinbox(self.main)
        self.cb_spinbox.configure(from_=0, to=99, width=5)
        self.cb_spinbox.place(anchor='nw', x='300', y='150')
        self.mb_spinbox = tk.Spinbox(self.main)
        self.mb_spinbox.configure(from_=0, to=99, width=5)
        self.mb_spinbox.place(anchor='nw', x='300', y='190')
        self.bt_spinbox = tk.Spinbox(self.main)
        self.bt_spinbox.configure(from_=0, to=99, width=5)
        self.bt_spinbox.place(anchor='nw', x='300', y='320')
        self.cof_spinbox = tk.Spinbox(self.main)
        self.cof_spinbox.configure(from_=0, increment=1, to=99, width=5)
        self.cof_spinbox.place(anchor='nw', x='300', y='360')
        self.t_spinbox = tk.Spinbox(self.main)
        self.t_spinbox.configure(from_=0, increment=1, to=99, width=5)
        self.t_spinbox.place(anchor='nw', x='300', y='400')
        self.gt_spinbox = tk.Spinbox(self.main)
        self.gt_spinbox.configure(from_=0, increment=1, to=99, width=5)
        self.gt_spinbox.place(anchor='nw', x='300', y='440')
        self.fm_spinbox = tk.Spinbox(self.main)
        self.fm_spinbox.configure(from_=0, to=99, width=5)
        self.fm_spinbox.place(anchor='nw', x='670', y='440')
        self.frooti_spinbox = tk.Spinbox(self.main)
        self.frooti_spinbox.configure(from_=0, to=99, width=5)
        self.frooti_spinbox.place(anchor='nw', x='670', y='400')
        self.rm_spinbox = tk.Spinbox(self.main)
        self.rm_spinbox.configure(from_=0, to=99, width=5)
        self.rm_spinbox.place(anchor='nw', x='670', y='360')
        self.wm_spinbox = tk.Spinbox(self.main)
        self.wm_spinbox.configure(from_=0, to=99, width=5)
        self.wm_spinbox.place(anchor='nw', x='670', y='320')
        self.sam_spinbox = tk.Spinbox(self.main)
        self.sam_spinbox.configure(from_=0, to=99, width=5)
        self.sam_spinbox.place(anchor='nw', x='670', y='230')
        self.ep_spinbox = tk.Spinbox(self.main)
        self.ep_spinbox.configure(from_=0, to=99, width=5)
        self.ep_spinbox.place(anchor='nw', x='670', y='190')
        self.vp_spinbox = tk.Spinbox(self.main)
        self.vp_spinbox.configure(from_=0, increment=1, to=99, width=5)
        self.vp_spinbox.place(anchor='nw', x='670', y='150')
        self.cp_spinbox = tk.Spinbox(self.main)
        self.cp_spinbox.configure(from_=0, to=99, width=5)
        self.cp_spinbox.place(anchor='nw', x='670', y='110')
        self.vb_label = tk.Label(self.main)
        self.vb_label.configure(background='white', font='{avro} 14 {italic}', text='Veg Briyani')
        self.vb_label.place(anchor='nw', x='50', y='110')
        self.cb_label = tk.Label(self.main)
        self.cb_label.configure(background='white', font='{avro} 14 {italic}', text='Chicken Briyani')
        self.cb_label.place(anchor='nw', x='50', y='150')
        self.mb_label = tk.Label(self.main)
        self.mb_label.configure(background='white', font='{avro} 14 {italic}', text='Mutton Briyani')
        self.mb_label.place(anchor='nw', x='50', y='190')
        self.bt_label = tk.Label(self.main)
        self.bt_label.configure(background='white', font='{avro} 14 {italic}', text='Black Tea')
        self.bt_label.place(anchor='nw', x='50', y='320')
        self.cof_label = tk.Label(self.main)
        self.cof_label.configure(background='white', font='{avro} 14 {italic}', text='Coffee')
        self.cof_label.place(anchor='nw', x='50', y='360')
        self.t_label = tk.Label(self.main)
        self.t_label.configure(background='white', font='{avro} 14 {italic}', text='Tea')
        self.t_label.place(anchor='nw', x='50', y='400')
        self.gt_label = tk.Label(self.main)
        self.gt_label.configure(background='white', font='{avro} 14 {italic}', text='Green Tea')
        self.gt_label.place(anchor='nw', x='50', y='440')
        self.cp_label = tk.Label(self.main)
        self.cp_label.configure(background='white', font='{avro} 14 {italic}', text='Chicken Puffs')
        self.cp_label.place(anchor='nw', x='400', y='110')
        self.vp_label = tk.Label(self.main)
        self.vp_label.configure(background='white', font='{avro} 14 {italic}', text='Veg Puffs')
        self.vp_label.place(anchor='nw', x='400', y='150')
        self.eg_label = tk.Label(self.main)
        self.eg_label.configure(background='white', font='{avro} 14 {italic}', text='Egg Puffs')
        self.eg_label.place(anchor='nw', x='400', y='190')
        self.sam_label = tk.Label(self.main)
        self.sam_label.configure(background='white', font='{avro} 14 {italic}', text='Samosa')
        self.sam_label.place(anchor='nw', x='400', y='230')
        self.wm_label = tk.Label(self.main)
        self.wm_label.configure(background='white', font='{avro} 14 {italic}', text='Watermelon')
        self.wm_label.place(anchor='nw', x='400', y='320')
        self.rm_label = tk.Label(self.main)
        self.rm_label.configure(background='white', font='{avro} 14 {italic}', text='Rose Milk')
        self.rm_label.place(anchor='nw', x='400', y='360')
        self.frooti_label = tk.Label(self.main)
        self.frooti_label.configure(background='white', font='{avro} 14 {italic}', text='Frooti')
        self.frooti_label.place(anchor='nw', x='400', y='400')
        self.fm_label = tk.Label(self.main)
        self.fm_label.configure(background='white', font='{avro} 14 {italic}', text='Fruit Mix')
        self.fm_label.place(anchor='nw', x='400', y='440')
        self.main.configure(background='white', height='520', width='750')
        self.main.pack(side='top')

        # Main widget
        self.mainwindow = self.main

    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        self.master.destroy()


    def ok(self):
        global Orders , app2,Ordered_price
        
        try:
            if self.cb_spinbox.get() != '0':
                orders['cb'] = self.cb_spinbox.get()
                Ordered_price.append(Price['cb']* int(orders['cb']))

            if self.vb_spinbox.get() != '0':
                orders['vb'] = self.vb_spinbox.get()
                Ordered_price.append(Price['vb'] * int(orders['vb']))

            if self.mb_spinbox.get() != '0':
                orders['mb'] = self.mb_spinbox.get()
                Ordered_price.append(Price['mb'] * int(orders['mb']))

            if self.bt_spinbox.get() != '0':
                orders['bt'] = self.bt_spinbox.get()
                Ordered_price.append(Price['bt'] * int(orders['bt']))

            if self.t_spinbox.get() != "0":
                orders['t'] = self.t_spinbox.get()
                Ordered_price.append(Price['t'] * int(orders['t']))

            if self.cof_spinbox.get() != '0':
                orders['cof'] = self.cof_spinbox.get()
                Ordered_price.append(Price['cof'] * int(orders['cof']))

            if self.gt_spinbox.get() != '0':
                orders['gt'] = self.gt_spinbox.get()
                Ordered_price.append(Price['gt'] * int(orders['gt']))

            if self.cp_spinbox.get() != "0":
                orders['cp'] = self.cp_spinbox.get()
                Ordered_price.append(Price['cp'] * int(orders['cp']))

            if self.ep_spinbox.get() != '0':
                orders['ep'] = self.ep_spinbox.get()
                Ordered_price.append(Price['ep'] * int(orders['ep']))

            if self.vp_spinbox.get() != '0':
                orders['vp'] = self.vp_spinbox.get()
                Ordered_price.append(Price['vp'] * int(orders['vp']))

            if self.sam_spinbox.get() != '0':
                orders['sam'] = self.sam_spinbox.get()
                Ordered_price.append(Price['sam'] * int(orders['sam']))

            if self.rm_spinbox.get() != '0':
                orders['rm'] = self.rm_spinbox.get()
                Ordered_price.append(Price['rm'] * int(orders['rm']))

            if self.wm_spinbox.get() != '0':
                orders['wm'] = self.wm_spinbox.get()
                Ordered_price.append(Price['wm'] * int(orders['wm']))

            if self.fm_spinbox.get() != "0":
                orders['fm'] = self.fm_spinbox.get()
                Ordered_price.append(Price['fm'] * int(orders['fm']))

            if self.frooti_spinbox.get() != '0':
                orders['frooti'] = self.frooti_spinbox.get()
                Ordered_price.append(Price['frooti'] * int(orders['frooti']))
            

            print(orders)
            for x in orders.keys():
                Orders = f'{Orders}, {fullform[x].replace(" ","")}'

            app2.insert_order()
            app2.bill=''
            self.master.destroy()
        except ValueError:
                messagebox.showerror('Error','Please Make sure that all the entry are filled if no enter 0.')
                self.master.destroy()
        except:
            messagebox.showerror('Error','Unknown Error Happended')







def run():
    global app2
    root2 = tk.Tk()
    root2.title('Order Food')
    root2.resizable(height=False, width=False)
    app2 = NeworderApp(root2)
    app2.run()





'''if __name__ =='__main__':
    root = tk.Tk()
    app = MenuApp(root)
    app.run()'''
