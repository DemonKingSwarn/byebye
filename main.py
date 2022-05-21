#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
from os.path import expanduser
from pathlib import Path

home = expanduser("~")
user = os.getlogin()

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="ByeBye")

        self.set_border_width(10)
        self.set_default_size(750, 225)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        frame1 = Gtk.Frame(label=None)

        grid1 = Gtk.Grid(row_spacing = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        #img = Gtk.Image()
        #img.set_from_file("./img/logout.png")

        img1 = Gtk.Image()
        img1.set_from_file("./img/cancel.png")
        img2 = Gtk.Image()
        img2.set_from_file("./img/logout.png")
        img3 = Gtk.Image()
        img3.set_from_file("./img/reboot.png")
        img4 = Gtk.Image()
        img4.set_from_file("./img/shutdown.png")
        img5 = Gtk.Image()
        img5.set_from_file("./img/suspend.png")
        img6 = Gtk.Image()
        img6.set_from_file("./img/hibernate.png")
        img7 = Gtk.Image()
        img7.set_from_file("./img/lock.png")

        label1 = Gtk.Label(label="Cancel")
        label1.set_hexpand(True)

        label2 = Gtk.Label(label="Logout")
        label2.set_hexpand(True)

        label3 = Gtk.Label(label="Reboot")
        label3.set_hexpand(True)

        label4 = Gtk.Label(label="Shutdown")
        label4.set_hexpand(True)

        label5 = Gtk.Label(label="Suspend")
        label5.set_hexpand(True)

        label6 = Gtk.Label(label="Hibernate")
        label6.set_hexpand(True)

        label7 = Gtk.Label(label="Lock")
        label7.set_hexpand(True)

        btn1 = Gtk.Button(label=None)
        btn1.set_hexpand(True)
        btn1.connect("clicked", self.on_btn1_clicked)
        btn1.set_image(img1)
        #btn1.set_relief(Gtk.RELIEF_NONE)

        btn2 = Gtk.Button(label=None)
        btn2.set_hexpand(True)
        btn2.connect("clicked", self.on_btn2_clicked)
        btn2.set_image(img2)
        #btn2.set_relief(Gtk.RELIEF_NONE)

        btn3 = Gtk.Button(label=None)
        btn3.set_hexpand(True)
        btn3.connect("clicked", self.on_btn3_clicked)
        btn3.set_image(img3)
        #btn3.set_relief(Gtk.RELIEF_NONE)

        btn4 = Gtk.Button(label=None)
        btn4.set_hexpand(True)
        btn4.connect("clicked", self.on_btn4_clicked)
        btn4.set_image(img4)
        #btn4.set_relief(Gtk.RELIEF_NONE)

        btn5 = Gtk.Button(label=None)
        btn5.set_hexpand(True)
        btn5.connect("clicked", self.on_btn5_clicked)
        btn5.set_image(img5)
        #btn5.set_relief(Gtk.RELIEF_NONE)

        btn6 = Gtk.Button(label=None)
        btn6.set_hexpand(True)
        btn6.connect("clicked", self.on_btn6_clicked)
        btn6.set_image(img6)
        #btn6.set_relief(Gtk.RELIEF_NONE)

        btn7 = Gtk.Button(label=None)
        btn7.set_hexpand(True)
        btn7.connect("clicked", self.on_btn7_clicked)
        btn7.set_image(img7)
        #btn7.set_relief(Gtk.RELIEF_NONE)
        
        grid1.attach(btn1, 0,0,1,1)
        grid1.attach(label1, 0,1,1,1)
        grid1.attach(btn2, 1,0,1,1)
        grid1.attach(label2, 1,1,1,1)
        grid1.attach(btn3, 2,0,1,1)
        grid1.attach(label3, 2,1,1,1)
        grid1.attach(btn4, 3,0,1,1)
        grid1.attach(label4, 3,1,1,1)
        grid1.attach(btn5, 4,0,1,1)
        grid1.attach(label5, 4,1,1,1)
        grid1.attach(btn6, 5,0,1,1)
        grid1.attach(label6, 5,1,1,1)
        grid1.attach(btn7, 6,0,1,1)
        grid1.attach(label7, 6,1,1,1)

        self.add(frame1)
        frame1.add(grid1)

    def on_btn1_clicked(self, widget):
        print("User chose: Cancel")
        self.destroy()

    def on_btn2_clicked(self, widget):
        print("User chose: Logout")
        os.system("pkill -u " + user)

    def on_btn3_clicked(self, widget):
        print("User chose: Reboot")
        os.system(f"systemctl reboot")

    def on_btn4_clicked(self, widget):
        print("User chose: Shutdown")
        os.system(f"systemctl poweroff")

    def on_btn5_clicked(self, widget):
        print("User chose: Suspend")
        os.system(f"systemctl suspend")

    def on_btn6_clicked(self, widget):
        print("User chose: Hibernate")
        os.system(f"systemctl hibernate")

    def on_btn7_clicked(self, widget):
        print("User chose: Lock")
        os.system(f"/home/demonkingswarn/.scripts/system/lock.sh")

win = MyWindow()

win.connect("destroy", Gtk.main_quit)

win.show_all()
Gtk.main()