import random
import tkinter as tk
from tkinter import ttk, BooleanVar
from turtle import window_height, window_width
from PIL import Image, ImageTk

window_width = 800
window_height = 400

img_w = 300
img_h = 400

_7seg_dict = {}
_7seg_dict['NIL'] = [False, False, False, False, False, False, False]
_7seg_dict['0'] = [True, True, True, False, True, True, True]
_7seg_dict['1'] = [False, False, True, False, False, True, False]
_7seg_dict['2'] = [True, False, True, True, True, False, True]
_7seg_dict['3'] = [True, False, True, True, False, True, True]
_7seg_dict['4'] = [False, True, True, True, False, True, False]
_7seg_dict['5'] = [True, True, False, True, False, True, True]
_7seg_dict['6'] = [True, True, False, True, True, True, True]
_7seg_dict['7'] = [True, False, True, False, False, True, False]
_7seg_dict['8'] = [True, True, True, True, True, True, True]
_7seg_dict['9'] = [True, True, True, True, False, True, True]
_7seg_dict['A'] = [True, True, True, True, True, True, False]
_7seg_dict['b'] = [False, True, False, True, True, True, True]
_7seg_dict['C'] = [True, True, False, False, True, False, True]
_7seg_dict['d'] = [False, False, True, True, True, True, True]
_7seg_dict['E'] = [True, True, False, True, True, False, True]
_7seg_dict['F'] = [True, True, False, True, True, False, False]
dict_letters = list(_7seg_dict.keys())

_7seg_var = {}
_7seg_var[0] = ['NIL', '1']
_7seg_var[1] = ['2', '6']
_7seg_var[2] = ['1', '3']
_7seg_var[3] = ['NIL', 'b']
_7seg_var[4] = ['4','8']
_7seg_var[5] = ['6', '1']
_7seg_var[6] = ['9', '7']
_7seg_var[7] = ['6', '0']
_7seg_var[8] = ['2', '4']
_7seg_var[9] = ['A', '5']
_7seg_var[10] = ['NIL', '0']
_7seg_var[11] = ['2', '5']
_7seg_var[12] = ['2', '1']
_7seg_var[13] = ['7', '3']
_7seg_var[14] = ['E', '4']
_7seg_var[15] = ['E', '8']
_7seg_var[20] = ['2', '1']
_7seg_var[21] = ['1', '8']
_7seg_var[22] = ['2', '5']
_7seg_var[23] = ['1', '6']
_7seg_var[28] = ['3', '0']
_7seg_var[30] = ['3', '8']
_7seg_var[42] = ['6', '0']
_7seg_var[48] = ['3', '4']
_7seg_var[54] = ['2', '2']
_7seg_var[55] = ['1', '9']
dict_var = list(_7seg_var.keys())

class Application(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry(str(window_width) + 'x' + str(window_height))
        self.img_7seg_left = {}
        self.img_7seg_right = {}
        self.img_switch = {}
        self.switch_status = []
        for i in range(6):
            self.switch_status.append(BooleanVar())
            self.switch_status[i].set(False)

        self.image_root_open()
        self.image_7seg_left_open()
        self.image_7seg_right_open()
        self.image_switch_open()
        self.draw_material()
        self.draw_switch()

    def image_root_open(self):
        self.img_root = Image.open('bentobako_root.png')
        w = self.img_root.width
        h = self.img_root.height
        self.img_magnification = 1.0
        if(img_w/w < img_h/h):
            self.img_magnification = img_w / w
        else:
            self.img_magnification = img_h / h
        self.img_root = self.img_root.resize(
            ((int(w * self.img_magnification)), (int(h * self.img_magnification))))
        self.img_root = ImageTk.PhotoImage(self.img_root)
        self.canvas_root_create()

    def image_7seg_left_open(self):
        for i in range(7):
            self.img_7seg_left[i] = Image.open('bentobako_7seg_left_' + str(i) + '.png').convert('RGBA')
            w = self.img_7seg_left[i].width
            h = self.img_7seg_left[i].height
            self.img_7seg_left[i] = self.img_7seg_left[i].resize(((int(w * self.img_magnification)), (int(h * self.img_magnification))))
            self.img_7seg_left[i] = ImageTk.PhotoImage(self.img_7seg_left[i])

    def image_7seg_right_open(self):
        for i in range(7):
            self.img_7seg_right[i] = Image.open('bentobako_7seg_right_' + str(i) + '.png').convert('RGBA')
            w = self.img_7seg_right[i].width
            h = self.img_7seg_right[i].height
            self.img_7seg_right[i] = self.img_7seg_right[i].resize(((int(w * self.img_magnification)), (int(h * self.img_magnification))))
            self.img_7seg_right[i] = ImageTk.PhotoImage(self.img_7seg_right[i])
        
    def image_switch_open(self):
        for i in range(6):
            self.img_switch[i] = Image.open('bentobako_switch_' + str(i) + '.png').convert('RGBA')
            w = self.img_switch[i].width
            h = self.img_switch[i].height
            self.img_switch[i] = self.img_switch[i].resize(((int(w * self.img_magnification)), (int(h * self.img_magnification))))
            self.img_switch[i] = ImageTk.PhotoImage(self.img_switch[i])

    def canvas_root_create(self):
        self.canvas_root = tk.Canvas(width=img_w, height=img_h)
        self.canvas_root.place(x=0, y=0)

    def canvas_draw_parts(self, img):
        self.canvas_root.create_image(0, 0, image=img, anchor=tk.NW)

    def draw_material(self):
        self.canvas_root.delete('all')
        self.canvas_draw_parts(self.img_root)
        switch_var = 0

        for i in range(6):
            if(self.switch_status[i].get()):
                self.canvas_draw_parts(self.img_switch[i])
                switch_var += 2 ** i
        
        if(switch_var in dict_var):
            left_letter = _7seg_var[switch_var][0]
            right_letter = _7seg_var[switch_var][1]
        else:
            left_letter = 'NIL'
            right_letter = 'NIL'

        for i in range(7):
            if(_7seg_dict[left_letter][i]):
                self.canvas_draw_parts(self.img_7seg_left[i])
        for i in range(7):
            if(_7seg_dict[right_letter][i]):
                self.canvas_draw_parts(self.img_7seg_right[i])
        

    def draw_switch(self):
        self.switch_frame = tk.Frame(self.master)
        self.switch_frame.place(x=img_w, y=0)
        label_1 = tk.Label(self.switch_frame, text='Switch')
        label_2 = tk.Label(self.switch_frame, text='ON')
        label_3 = tk.Label(self.switch_frame, text='OFF')
        label_4 = tk.Label(self.switch_frame, text='1')
        label_5 = tk.Label(self.switch_frame, text='2')
        label_6 = tk.Label(self.switch_frame, text='3')
        label_7 = tk.Label(self.switch_frame, text='4')
        label_8 = tk.Label(self.switch_frame, text='5')
        label_9 = tk.Label(self.switch_frame, text='6')
        label_1.grid(row=0, column=0, padx=10, pady=10)
        label_2.grid(row=1, column=0, padx=10, pady=10)
        label_3.grid(row=2, column=0, padx=10, pady=10)
        label_4.grid(row=0, column=1, padx=10, pady=10)
        label_5.grid(row=0, column=2, padx=10, pady=10)
        label_6.grid(row=0, column=3, padx=10, pady=10)
        label_7.grid(row=0, column=4, padx=10, pady=10)
        label_8.grid(row=0, column=5, padx=10, pady=10)
        label_9.grid(row=0, column=6, padx=10, pady=10)

        radio_1_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[0], value=True)
        radio_1_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[0], value=False)
        radio_2_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[1], value=True)
        radio_2_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[1], value=False)
        radio_3_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[2], value=True)
        radio_3_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[2], value=False)
        radio_4_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[3], value=True)
        radio_4_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[3], value=False)
        radio_5_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[4], value=True)
        radio_5_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[4], value=False)
        radio_6_T = tk.Radiobutton(self.switch_frame, variable=self.switch_status[5], value=True)
        radio_6_F = tk.Radiobutton(self.switch_frame, variable=self.switch_status[5], value=False)
        radio_1_T.grid(row=1, column=1, padx=10, pady=10)
        radio_1_F.grid(row=2, column=1, padx=10, pady=10)
        radio_2_T.grid(row=1, column=2, padx=10, pady=10)
        radio_2_F.grid(row=2, column=2, padx=10, pady=10)
        radio_3_T.grid(row=1, column=3, padx=10, pady=10)
        radio_3_F.grid(row=2, column=3, padx=10, pady=10)
        radio_4_T.grid(row=1, column=4, padx=10, pady=10)
        radio_4_F.grid(row=2, column=4, padx=10, pady=10)
        radio_5_T.grid(row=1, column=5, padx=10, pady=10)
        radio_5_F.grid(row=2, column=5, padx=10, pady=10)
        radio_6_T.grid(row=1, column=6, padx=10, pady=10)
        radio_6_F.grid(row=2, column=6, padx=10, pady=10)

        button_1 = tk.Button(self.switch_frame, text='状況更新', command=self.status_renew)
        button_1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def status_renew(self):
        self.draw_material()


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
