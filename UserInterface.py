"""    Created by Monim on 9/14/2018.    """
from tkinter import *

from SVMAlgorithm import SVMAlgorithm


def ok_button_click():
    try:
        clump = int(clump_text.get().strip())
        cell_size = int(size_text.get().strip())
        cell_shape = int(shape_text.get().strip())
        marginal = int(marginal_text.get().strip())
        epithelial = int(epithelial_text.get().strip())
        bare = int(bare_text.get().strip())
        chromatin = int(chromatin_text.get().strip())
        nucleoli = int(nucleoli_text.get().strip())
        mitoses = int(mitoses_text.get().strip())

        if clump < 0 or cell_size < 0 or cell_shape < 0 or marginal < 0 or epithelial < 0 or bare < 0 or chromatin < 0 or nucleoli < 0 or mitoses < 0:
            result = 'Fill up all options with valid values...'
        elif (clump + cell_size + cell_shape + marginal + epithelial + bare + chromatin + nucleoli + mitoses) < 1:
            result = 'You are completely healthy!'
        else:
            array = [clump, cell_size, cell_shape, marginal, epithelial, bare, chromatin, nucleoli, mitoses]
            input_array = [array]
            print(input_array)
            algorithm = SVMAlgorithm()
            answer = algorithm.get_result(input_array)
            if answer == 2:
                result = "You have Benign Tumor! Consult a doctor..."
            else:
                result = "You have Malignant Cancer! Consult a doctor as soon as possible...."

        result_label.config(text=result)
    except:
        result_label.config(text='Fill up all options with valid values!')


# Set window in the center of screen
def center_of_screen(win):
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    x = (width / 2) - 400
    y = (height / 2) - 300
    win.geometry('%dx%d+%d+%d' % (800, 450, x, y))


# Main Window
window = Tk()

# Make window Size fixed
window.resizable(width=False, height=False)

# Set Title
window.title("Breast Cancer Prediction")

# Set Window Background
window.configure(background="white")

center_of_screen(window)

# Set text label of title
title_label = Label(window, text="Breast Cancer Prediction (SVM)", bg="#ffffff", fg="#311B92", font="none 24 bold")
title_label.pack(fill=X)

# Create Label text
Label(window, text="Fill up the options", bg="#ffffff", fg="#1B5E20", font="none 12 bold").pack(pady=10)

# Create input field
frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Clump Thickness', width=30).pack(padx=2, pady=1, side=LEFT)
clump_text = Entry(frame, width=10)
clump_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Uniformity of Cell Size', width=30).pack(padx=2, pady=1, side=LEFT)
size_text = Entry(frame, width=10)
size_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Uniformity of Cell Shape', width=30).pack(padx=2, pady=1, side=LEFT)
shape_text = Entry(frame, width=10)
shape_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Marginal Adhesion', width=30).pack(padx=2, pady=1, side=LEFT)
marginal_text = Entry(frame, width=10)
marginal_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Single Epithelial Cell Size', width=30).pack(padx=2, pady=1, side=LEFT)
epithelial_text = Entry(frame, width=10)
epithelial_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Bare Nuclei', width=30).pack(padx=2, pady=1, side=LEFT)
bare_text = Entry(frame, width=10)
bare_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Bland Chromatin', width=30).pack(padx=2, pady=1, side=LEFT)
chromatin_text = Entry(frame, width=10)
chromatin_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Normal Nucleoli', width=30).pack(padx=2, pady=1, side=LEFT)
nucleoli_text = Entry(frame, width=10)
nucleoli_text.pack(padx=5, side=LEFT)

frame = Frame(window, bg='#9FA8DA')
frame.pack()
Label(frame, bg='#ffffff', text='Mitoses', width=30).pack(padx=2, pady=1, side=LEFT)
mitoses_text = Entry(frame, width=10)
mitoses_text.pack(padx=5, side=LEFT)

# Create Check Button
Button(window, text="Check", width=8, command=ok_button_click, bg="#00838F", fg="#ffffff", font="none 12 bold") \
    .pack(pady=10, side=TOP)

# Create Result Label
result_label = Label(window, bg="#ffffff", fg="#D50000", font="none 12 bold")
result_label.pack(pady=10)

# Show Window
window.mainloop()
