from tkinter import *
root = Tk()
root.title("Calculate")
root.geometry("400x500")
root.iconbitmap("calculator.ico")
def clickButton():
    print("click")

# button = [
#        ["7","8","9","/"],
#        ["4","5","6","*"],
#        ["1","2","3","-"],
#        ["+/-","0","=","+"]
#        ]
button = [
       "7","8","9","/",
       "4","5","6","*",
       "1","2","3","-",
       "+/-","0","=","+"
       ]



for i in range(5): root.columnconfigure(index = i, weight = 1)
for j in range(4): root.rowconfigure(index = j, weight = 1)


# for i in range(len(button)):
#     for j in range(len(button[0])):
        
#         btn = Button(text = f"{button[i][j]}" ,height=7, width=15)
#         btn.grid(row = i,column = j,ipadx=6, ipady=6, padx=4, pady=4)

item = 0
for i in range(1,5):
    for j in range(0,4):
        btn = Button(text = button[item] ,height=3, width=8,font="Aeial")
        btn.grid(row = i,column = j, ipadx=5,  ipady=5, padx=5, pady=5)
        item+=1
        
entr1 = Entry(width=50)

entr1.grid(row=0,column=0,columnspan=4)

root.mainloop()
