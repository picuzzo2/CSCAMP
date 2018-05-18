from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import string
import csv
import Regression 

############################## Root of Program ###############################

root = Tk()
root.title("Wine Quality")

##############################################################################

############################# Variable Font BG ################################

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()

root.option_add("*Font", "candara 16")

load = Image.open("BG.png")
rende = ImageTk.PhotoImage(load)
img = Label(root, image=rende)
img.image = rende   
img.pack()

icon = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

################################################################################

############################ Label ##############################################

Label(root, text="Fixed Acidity",bg="#d6dde7",font=('candara',16,)).place(x=50,y=55)
Label(root, text="Volatile Acidity",bg="#d6dde7",font=('candara',16,)).place(x=50,y=95)
Label(root, text="Citric Acid",bg="#d6dde7",font=('candara',16,)).place(x=50,y=135)
Label(root, text="Residual Sugar",bg="#d6dde7",font=('candara',16,)).place(x=50,y=175)
Label(root, text="Chlorides",bg="#d6dde7",font=('candara',16,)).place(x=50,y=215)
Label(root, text="Free Sulfur Dioxide",bg="#d6dde7",font=('candara',16,)).place(x=50,y=255)
Label(root, text="Total Sulfur Dioxide",bg="#d6dde7",font=('candara',16,)).place(x=50,y=295)
Label(root, text="Sulphates",bg="#d6dde7",font=('candara',16,)).place(x=50,y=335)
Label(root, text="Alcohol",bg="#d6dde7",font=('candara',16,)).place(x=50,y=375)

Label(root, text="Wine Quality",bg="#d6dde7",font=('candara',20,'bold')).place(x=200,y=10)

e1 = Entry(root, textvariable=var1).place(x=260,y=55)
e2 = Entry(root,textvariable=var2).place(x=260,y=95)
e3 = Entry(root,textvariable=var3).place(x=260,y=135)
e4 = Entry(root,textvariable=var4).place(x=260,y=175)
e5 = Entry(root,textvariable=var5).place(x=260,y=215)
e6 = Entry(root,textvariable=var6).place(x=260,y=255)
e7 = Entry(root,textvariable=var7).place(x=260,y=295)
e8 = Entry(root,textvariable=var8).place(x=260,y=335)
e9 = Entry(root,textvariable=var9).place(x=260,y=375)

##################################################################################

################################# Function #######################################

def is_float(input):
  try:
    num = float(input)
  except ValueError:
    return False
  return True

def on_click():
    fixed_acidity = var1.get()
    volatile_acidity = var2.get()
    citric_acid = var3.get()
    residual_sugar = var4.get()
    chlorides = var5.get()
    free_sulfur_dioxide = var6.get()
    total_sulfur_dioxide = var7.get()
    sulphates = var8.get()
    alcohol = var9.get()

    if is_float(fixed_acidity) != True or is_float(volatile_acidity) != True  or is_float(citric_acid) != True or is_float(residual_sugar) != True or is_float(chlorides) != True or is_float(free_sulfur_dioxide) != True or is_float(total_sulfur_dioxide) != True or is_float(sulphates) != True or is_float( alcohol) != True :
        messagebox.showerror("Error", "Float or Integer only")
    else :
        data = [float(fixed_acidity),float(volatile_acidity),float(citric_acid),float(residual_sugar),float(chlorides),float(free_sulfur_dioxide),float(total_sulfur_dioxide),float(sulphates),float(alcohol)]
        with open('collectedData.csv','w',newline='') as f:
            #fieldnames = ['colum1','colum3','colum2']  
            thewriter = csv.writer(f)
            thewriter.writerow(['fixed acidity', 'volatile acidity', 'citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','sulphates','alcohol'])
            thewriter.writerow(data)
        predicted = Regression.predicted()
       # print(predicted)
        messagebox.showinfo("Quality:",predicted[0])
        
def question():
    text="""Fixed_acidity : 1.00 - 20.00 \nVolatile_acidity : 0.00 - 2.00\nCitric acid : 0 - 1 \nResidual sugar : 0 - 20 \nChlorides : 0.000 - 1.000\nfree sulfur dioxide : 0.00 - 100.00\nFree sulfur dioxide 3 - 300\nalcohol:0 - 20"""
    messagebox.showinfo("Detail",text)

###################################################################################

############################## Button and ETC. ####################################

q_img = Image.open("questionicon.png")
img = ImageTk.PhotoImage(q_img)
x = Button(root,image=img,bg="#d6dde7",command=question,bd=0)
x.place(x=460,y=430)
but = Button(root,text="predict",command= on_click)
but.place(x=230,y=430)

###################################################################################

################################# Main loop #######################################

root.geometry("550x500")
root.resizable(False, False)
root.mainloop()

###################################################################################