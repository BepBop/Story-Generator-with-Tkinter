from tkinter import * 
from tkinter import messagebox
import random
root=Tk()
 
def myClick():
 if len(e1.get())==0:
   messagebox.showwarning("Story Generator", "Noun field empty")
 if len(e2.get())==0:
    messagebox.showwarning("Story Generator", "Adjective field empty")
   
 if len(e1.get())!=0:
    
    k=random.randint(1,2)
    k2=str(random.randint(1,8))

    Noun=["is a good person ","is a brave person ","lives in New Delhi ","lives in Bihar ", "lives in Shimla "]
    
    Setup=["There was a cruel Ork King", "A Red dragon was terrorizing the kingdom","A princess was trapped in magical kingdom by a Red Dragon","The enemy of Orks were at kingdom's door","The kings army were desperate for a hope!","Kingdom was fighting a loosing battle"]
  
    Noun2 = {
     "1": " struggling to get by ",
     "2": " the proud owner of a small textile mill ",
     "3": " who worked as a small tailor ",
     "4": " tending to his farm ",
     "5": " a common man ",
     "6": " and was a successful student ",
     "7": " a middle class salaryman ",
     "8": " a son to a small bussinessman "
            }
    
    Noun3 = {
     "1": " but on a quest to become the richest person!"  ,
     "2": " and on a quest to save their village against drought" ,
     "3": " on an impossible mission of getting her daughter into a college",
     "4": " However on a mission of getting the dam built for their village" , 
     "5": " with a burning desire to become a highly respectable member of the society",
     "6": " with a goal of becoming successful in life!",
     "7": " with a deep desire to break free from his monotonous job and finally travel the world!",
     "8": " hoping to open his own business one day"
           }
           

 if k==2 and len(e2.get())!=0:
    myLabel4=Label(root,text="Once upon a time, " + random.choice(Setup) + " and " + e1.get() + Noun2[k2] + "magically summoned to the rescue!")
    myLabel4.pack()
 
 if k==1 and len(e2.get())!=0:
    myLabel4=Label(root,text=e1.get()+" "+Noun[k]+Noun2[k2]+ "Suddenly, all went awry when they were summoned to the magical kingdom!")
    myLabel4.pack()
 
 if len(e2.get())==0:
    myLabel4=Label(root,text=e1.get()+" "+Noun[k]+Noun2[k2]+Noun3[k2]+ ". All was changed forever when they won a lottery worth crores!")
    myLabel4.pack()

 if k>0:
    Adjective = ["However didnt let go of their ","was great confusion and they let go of "," were mesmerised and felt "," However felt nothing like a hero should, "]


 #monologue
 
 if k>0 and len(e2.get())!=0:

    MonologueIntro=["Upon reaching the kingdom, ","Upon reaching the kingdom's court, ","Upon being summoned to the kingdom, ","Upon being summoned in the middle of dark winter night to the kingdom, ", "Upon being summoned to the kingdom's church ", "It was warm sunny morning when our hero appeared ","Warm sun shinning on the vast green grassland when our hero touched the soil of magic kingdom the first time"]
    
    MonologueResponsible=["The King was thrilled.", "The King's Court was thrilled.","The King Kingdom was filled with up hope.","The king asked them to help them with fighting the dragon.","The King pleaded them to join them in conquest against the dragon.","The Kingdom was overjoyed with arrival of the new hero.", "Suddenly the whole kingdom was filled with joy for now they had a fighting chance"]
    
    MonologueHero=["To be the hero of the story,","The hero of our story,","Once a common mam now hero,","Our hero,"," Magic Kingdom last hero",]
    
    MonologueFight=["went into the deep redwood forest","Our hero went deep to save the day","Charged the battle that was knocking at the kingdom's door","Our now hero listening to the problem found the courage and charged the battle!","Our hero went out to the battle on the Great Mount Volca","Our common man now hero lead the kingdom army to the warfield of King Doom","air was warm and night dark but hero feared none and charged the Dragon Mount"]
    
    MonologueEnd=["Hero passing through dense kingdom forest to the battlefield was suddenly attacked","Suddenly the hero was attacked by magic casters with fireballs","The oracks surrounded our hero","The dragon flew over our hero","Enemies hidden in thick forest surrounded our hero passing by to the battlefield","enemies archers shot some arrows at our hero","Our hero party shot their warning shot at the dragon lair"]
   
    MonologueEnd1=["Our hero fought bravely and was victorious","Our hero at the end saved this kingdom","Our hero fought the war and kingdom was saved", "Everyone was happy when out hero returned from the conquest victorious!"]
    myLabel5=Label(root,text=random.choice(MonologueIntro)+" "+random.choice(MonologueResponsible))
    myLabel5.pack()
    
    myLabel5=Label(root,text=e1.get()+" "+ random.choice(Adjective)+ e2.get()+ " in their heart")
    myLabel5.pack()
    
    myLabel6=Label(root,text=random.choice(MonologueHero)+" "+random.choice(MonologueFight))
    myLabel6.pack()

    myLabel6=Label(root,text=random.choice(MonologueEnd))
    myLabel6.pack()
   
    myLabel6=Label(root,text=random.choice(MonologueEnd1))
    myLabel6.pack()

    myLabel6=Label(root,text="x---------x")
    myLabel6.pack()
    
 

       
     
        
                  
myLabel1=Label(root, text = "Welcome!")
myLabel1.pack()

myLabel2=Label(root, text = "Enter a Character Name")
myLabel2.pack()

e1=Entry(root,width=18)
e1.pack()

myLabel3=Label(root, text = "Enter an Character Trait")
myLabel3.pack()

e2=Entry(root,width=18)
e2.pack()
    
myButton=Button(root,text="generate",command=myClick)
myButton.pack()


myLabel1.pack(padx=(30), pady=(20))
myLabel2.pack(padx=(30), pady=(5))
myLabel3.pack(padx=(30), pady=(5))
myButton.pack(padx=(30), pady=(20)) 

root.mainloop()

