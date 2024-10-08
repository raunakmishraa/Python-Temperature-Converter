#Import Modules
import time
from tkinter import *
import webbrowser
#Functions
#Open my Website in Browser
def openWebsite(url):
    webbrowser.open_new(url)
#Variables
units=["C","K","F"]
#Conversion Algorithm
def convert():
    givenTemp=float(temp_entry.get())
    fromunit=fromClicked.get()
    tounit=toClicked.get()
    if str(fromunit)==str(tounit):
        lhs=str(givenTemp)+"°"+str(fromunit)+" ="
        rhs=str(givenTemp)+"°"+str(tounit)
        givenLabel.configure(text=lhs)
        resultLabel.configure(text=rhs)
    if str(fromunit)!=str(tounit):
        if str(fromunit)=='C':
            if str(tounit)=='F':
                giventemp=givenTemp
                convertedTemp=(giventemp*9/5)+32
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
            if str(tounit)=='K':
                giventemp=givenTemp
                convertedTemp=giventemp+273.15
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
        if str(fromunit)=='K':
            if str(tounit)=='C':
                giventemp=givenTemp
                convertedTemp=giventemp-273.15
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
            if str(tounit)=='F':
                giventemp=givenTemp
                convertedTemp=((giventemp-273.15)*9/5)+32
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
        if str(fromunit)=='F':
            if str(tounit)=='C':
                giventemp=givenTemp
                convertedTemp=(giventemp-32)*5/9
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
            if str(tounit)=='K':
                giventemp=givenTemp
                convertedTemp=((giventemp-32)*5/9)+273.15
                lhs=str(givenTemp)+"°"+str(fromunit)+" ="
                rhs=str(convertedTemp)+"°"+str(tounit)
                givenLabel.configure(text=lhs)
                resultLabel.configure(text=rhs)
#GUI
root=Tk()
root.title("Temperature Converter") #Gives a title to the Window
root.geometry("765x580") #Sets the Geometry Size of Window
root.iconbitmap('Brand-Logo-Icon.ico') #Icon for the Window
root.resizable(False, False) #Restricts user to resize the Window
root.configure(bg='lemon chiffon') #Background Color dor Window
appLabel = Label(root, text="Convert Your Temperature", font=("Times", "42", "bold italic"), fg="red", bg='lemon chiffon', anchor=CENTER) #Label for Appname
appLabel.pack() #Packs appLabel
appLabel.place(x=10,y=5) #Position for appLabel
temp_frame = LabelFrame(root, text="Temperature", background="lemon chiffon", bd=4, fg='red', labelanchor=N) #Creates a frame for Guess Boxes
tempLabel = Label(temp_frame, text="Temperature You Want to Convert: ", font=("Times", "20"), fg="blue", bg='lemon chiffon', anchor=CENTER) #Label for tempLabel
tempLabel.grid(row=0, column=1, padx=10, pady=5) #Position tempLabel
temp_entry = Entry(temp_frame, font=("Helvetica", "15")) #Creates temp_entry
temp_entry.grid(row=0, column=2, padx=10, pady=10) #Position for temp_entry
fromClicked=StringVar()
fromClicked.set(units[0])
fromUnit=OptionMenu(temp_frame,fromClicked,*units) #Creates Dropdown for fromUnit
fromUnit.grid(row=0, column=3, padx=10, pady=10) #Position for units dropdown
temp_frame.pack() #Packs Guess Frame
temp_frame.place(x=10, y=90) #Positions guess_frame
convert_button = Button(root, text="Convert", fg='white', bg='green', font=("Helvetica", "15", "italic"), bd='3', command=convert) #Creates convert_button
convert_button.pack() #Packs convert_button
convert_button.place(x=150, y=175) #Positions convert_button
toLabel = Label(root, text="to", font=("Times", "20"), fg="black", bg='lemon chiffon', anchor=CENTER) #Label for tempLabel
toLabel.pack() #Packs convert_button
toLabel.place(x=250, y=178) #Positions convert_button
toClicked=StringVar()
toClicked.set(units[0])
toUnit=OptionMenu(root,toClicked,*units) #Creates Dropdown for toUnit
toUnit.pack() #Packs convert_button
toUnit.place(x=290, y=183) #Positions convert_button
result_frame = LabelFrame(root, text="Converted Temperature: ", background="lemon chiffon", bd=4, fg='red', labelanchor=N) #Creates a frame for result_frame
givenLabel=Label(result_frame, text="", font=("Times", "20"), fg="black", bg='lemon chiffon', anchor=CENTER) #Label for resultLabel
givenLabel.grid(row=0, column=0, padx=10, pady=10) #Position for resultLabel
resultLabel=Label(result_frame, text="", font=("Times", "20"), fg="black", bg='lemon chiffon', anchor=CENTER) #Label for resultLabel
resultLabel.grid(row=0, column=1, padx=10, pady=10) #Position for resultLabel
result_frame.pack() #Packs result_frame
result_frame.place(x=270, y=235) #Positions result_frame
#DEVELOPER LABEL
devNameLabel = Label(root, text="Developed By:", font=("Times", "20", "underline"), fg="green", bg="lemon chiffon")
devNameLabel.pack()
devNameLabel.place(x=225, y=500)
devName = Label(root, text="Raunak Kumar", font=("Times", "20"), fg="orange", bg="lemon chiffon")
devName.pack()
devName.place(x=400, y=500)
devContact = Label(root, text="Lets Connect", fg="blue", cursor="hand2")
devContact.pack()
devContact.place(x=350, y=540)
devContact.bind("<Button-1>", lambda e: openWebsite("https://www.raunakmishra.com.np/#Contact"))
root.mainloop()
