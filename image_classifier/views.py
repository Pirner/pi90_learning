from __future__ import unicode_literals
import os
from enum import Enum


from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, Checkbutton, IntVar, Text, TOP, X, N, W, E, filedialog
from tkinter import *
from tkinter.ttk import Frame, Button, Style, Label, Entry

# move to views
viewSettings = {
    'window_height': 500,
    'window_width': 500,
    'button_edge_distance': 50,
    'quit_button_x': 10,
    'file_dialog_error_message': 'No File selected - Goodbye World'
}


class NetworkChoice(Enum):
    DNN = 0,
    CNN = 1


# stores data from the mainview
class MainViewData(object):
    image_path = ''
    train_list_path = ''
    model_path = ''
    network_type = NetworkChoice.DNN



class MainView(Frame):
    def __init__(self):
        super().__init__()

        self.data = MainViewData()

        self.initUI()

    def initUI(self):
        # self.master.title("Buttons")
        # self.style = Style()
        # self.style.theme_use("default")
        # frame = Frame(self, relief=RAISED, borderwidth=1)
        # frame.pack(fill=BOTH, expand=True)
        # self.pack(fill=BOTH, expand=True)
        # simple quit button
        # closeButton = Button(self, text="Close", command=self.quit)
        # closeButton.pack(side=RIGHT, padx=5, pady=5)
        # starts prediction process with given parameters
        # okButton = Button(self, text="OK")
        # okButton.pack(side=RIGHT)
        # self.master.title("Review")
        # self.pack(fill=BOTH, expand=True)
        # var1 = IntVar()
        # Checkbutton(self, text="Deep Neural Network (3 - Layers)", variable=var1).pack(side=LEFT, padx=5, pady=5)
        # var2 = IntVar()
        # Checkbutton(self, text="Convolutional Neural Network (Not implemented)", variable=var2).pack(side=LEFT, padx=5, pady=5)

        self.master.title("Package Detector Prototype")

        Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        # self.rowconfigure(3, pad=3)
        # self.rowconfigure(4, pad=3)

        # entry = Entry(self)
        # entry.grid(row=0, columnspan=4, sticky=W+E)

        self.image_path = Button(self, text="Image", command=self.set_image_path)
        self.image_path.grid(row=0, column=1)

        self.image_path = Button(self, text="Model", command=self.set_model_path)
        self.image_path.grid(row=0, column=2)

        # now some description boxes:

        self.image_path_label = Label(self, text='not - set', anchor='w')
        self.image_path_label.grid(row=1, column=1)

        self.model_path_label = Label(self, text='not - set', anchor='w')
        self.model_path_label.grid(row=1, column=2)

        # select network
        self.network_enum = StringVar(self)
        network_types = {'DNN', 'CNN'}
        self.network_enum.set('DNN')  # set the default option


        network_selector = OptionMenu(self, self.network_enum, *network_types)
        network_selector.grid(row=2, columnspan=3)
        self.network_enum.trace('w', self.change_dropdown)

        # row 3
        self.train_list_path = Button(self, text="train-list", command=self.set_train_list_path)
        self.train_list_path.grid(row=3, column=0)

        self.valid_list_path = Button(self, text="valid-list", command=self.set_valid_list_path)
        self.valid_list_path.grid(row=3, column=1)

        # row 4
        self.train_list_path_label = Label(self, text='not - set', anchor='w')
        self.train_list_path_label.grid(row=4, column=0)

        self.valid_list_path_label = Label(self, text='not - set', anchor='w')
        self.valid_list_path_label.grid(row=4, column=1)

        # row 5
        train_button = Button(self, text="create new model", command=self.model_creation_wrapper)
        train_button.grid(row=5, column=0)

        # self.valid_list_path = Button(self, text="train-list", command=self.set_train_list_path)
        # self.valid_list_path.grid(row=0, column=0)

        # row 7
        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.grid(row=7, column=2)

        # starts prediction process with given parameters
        okButton = Button(self, text="OK")
        okButton.grid(row=7, column=0)



        self.pack()

    def change_dropdown(self, *args):
        print('network - type: ', self.network_enum.get())
        if self.network_enum.get() == 'DNN':
            print('DNN network - set locked.')
            self.data.network_type = NetworkChoice.DNN
        elif self.network_enum.get() == 'CNN':
            print('CNN network - set locked')
            self.data.network_type == NetworkChoice.CNN
        else:
            print('Invalid Network Architecture or not implemented yet')


    def set_train_list_path(self):
        # filename = filedialog.askopenfilename(filetypes=(("XML files", "*.xml")))
        try:
            filename = filedialog.askopenfilename()
            self.data.train_list_path = filename
            # show only file the label
            tail = os.path.split(filename)
            print('selected list: ', tail)
            count = len(tail)
            self.train_list_path_label.config(text=tail[count - 1])
        except IOError:
            print('IOError')
        else:
            print(viewSettings['file_dialog_error_message'])

    def set_valid_list_path(self):
        # filename = filedialog.askopenfilename(filetypes=(("XML files", "*.xml")))
        try:
            filename = filedialog.askopenfilename()
            self.data.valid_list_path = filename
            # show only file the label
            tail = os.path.split(filename)
            print('selected list: ', tail)
            count = len(tail)
            self.valid_list_path_label.config(text=tail[count - 1])
        except IOError:
            print('IOError')
        else:
            print(viewSettings['file_dialog_error_message'])

    def set_image_path(self):
        try:
            filename = filedialog.askopenfilename()
            self.data.image_path = filename
            # show only file the label
            tail = os.path.split(filename)
            print('selected image: ', tail)
            count = len(tail)
            self.image_path_label.config(text=tail[count - 1])
        except IOError:
            print('IOError')
        else:
            print(viewSettings['file_dialog_error_message'])

    def set_model_path(self):
        try:
            filename = filedialog.askopenfilename()
            self.data.model_path = filename
            # show only file the label
            tail = os.path.split(filename)
            print('selected model: ', tail)
            count = len(tail)
            self.model_path_label.config(text=tail[count - 1])
        except IOError:
            print('IOError')
        else:
            print(viewSettings['file_dialog_error_message'])

    def model_creation_wrapper(self):
        if self.network_enum.get() == 'DNN':
            print('DNN architecture will be created...')

        elif self.network_enum.get() == 'CNN':
            print('CNN architecture will be created...')

        else:
            print('no valid option: ', self.network_enum.get())

def main():
    root = Tk()
    root.geometry("{}x{}+1800+300".format(viewSettings['window_height'], viewSettings['window_width']))
    app = MainView()
    root.mainloop()


if __name__ == '__main__':
    main()