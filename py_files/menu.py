import tkinter as tk
import tkinter.ttk as ttk

orders={}

class MenuApp:
    def __init__(self, master):
        # build ui
        global orders
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
        self.wm_price.configure(background='white', font='{avro} 12 {italic}', text='40 RS')
        self.wm_price.place(anchor='nw', x='600', y='320')
        self.rm_price = tk.Label(self.main)
        self.rm_price.configure(background='white', font='{avro} 12 {italic}', text='40 RS')
        self.rm_price.place(anchor='nw', x='600', y='360')
        self.frooti_price = tk.Label(self.main)
        self.frooti_price.configure(background='white', font='{avro} 12 {italic}', text='40 RS')
        self.frooti_price.place(anchor='nw', x='600', y='400')
        self.fm_price = tk.Label(self.main)
        self.fm_price.configure(background='white', font='{avro} 12 {italic}', text='40 RS')
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
        self.cb_spinbox.configure(from_=0, to=99,width=5)
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
        if self.cb_spinbox.get() !='0':
            orders['cb']=self.cb_spinbox.get()

        if self.vb_spinbox.get() !='0':
            orders['vb']=self.vb_spinbox.get()
        if self.mb_spinbox.get() !='0':
            orders['mb']=self.mb_spinbox.get()
        if self.bt_spinbox.get() !='0':
            orders['bt']=self.bt_spinbox.get()
        if self.t_spinbox.get() !="0":
            orders['t']=self.t_spinbox.get()
        if self.cof_spinbox.get() !='0':
            orders['cof']=self.cof_spinbox.get()
        if self.gt_spinbox.get() !='0':
            orders['gt']=self.gt_spinbox.get()
        if self.cp_spinbox.get() !="0":
            orders['cp']=self.cp_spinbox.get()
        if self.ep_spinbox.get() !='0':
            orders['ep']=self.ep_spinbox.get()
        if self.vp_spinbox.get() !='0':
            orders['vp']=self.vp_spinbox.get()
        if self.sam_spinbox.get() !='0':
            orders['sam']=self.sam_spinbox.get()
        if self.rm_spinbox.get() !='0':
            orders['rm']=self.rm_spinbox.get()
        if self.wm_spinbox.get() !='0':
            orders['wm']=self.wm_spinbox.get()
        if self.fm_spinbox.get() !="0":
            orders['fm']=self.fm_spinbox.get()
        if self.frooti_spinbox.get() !='0':
            orders['frooti']=self.frooti_spinbox.get()

        print(orders)
        return orders


def run_menu():
    root1 = tk.Tk()
    root1.title('Menu')
    root1.resizable(height=False, width=False)
    app1 = MenuApp(root1)
    app1.run()
    return orders

'''if __name__ =='__main__':
    root = tk.Tk()
    app = MenuApp(root)
    app.run()'''
