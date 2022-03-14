import banana_dev as banana
from tkinter import * 
from tkinter import messagebox
root=Tk()
 
def myClick():
     if len(e1.get())!=0:
      messagebox.showwarning("Story Generator", "Takes upto 5 min for GPT XL Model to compute")
     model_parameters = { "text": e1.get(), "length": 50, "temperature": 0.9, "topK": 50, "topP": 0.9}
     out_list = banana.run("275dec85-c4c8-419c-b524-9bbd26421d6b","gptj",model_parameters)
     temp = (out_list['modelOutputs'][0])
     myLabel3 = Label(root,text = temp)
     myLabel3.pack()
     
          
myLabel1=Label(root, text = "Welcome!")
myLabel1.pack()

myLabel2=Label(root, text = "Enter a character Name")
myLabel2.pack()

e1=Entry(root,width=15)
e1.pack()

myLabel2.pack(padx=(18), pady=(18))

myButton=Button(root,text="generate",command=myClick)
myButton.pack()

myButton.pack(padx=(18), pady=(18))



root.mainloop()
