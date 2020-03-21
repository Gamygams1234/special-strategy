from tkinter import *
#keydown function
#first define the click event
def click(arg):
    output.delete(0.0, END)#making sure the text box is clear
    definition = my_compdictionary[arg]
    output.insert(END, definition)
def close_window():
    window.destroy()
    exit()
window = Tk()
window.title("SPECIAL Attributes")
#adding a background color
window.configure(background="black")
#adding a photo
photo1 = PhotoImage(file="cullenimage.gif")
# Label allows you to put something on to the window
Label(window, image= photo1, bg = 'black') .grid(row=0, column=0, columnspan = 7)
# Label for text
Label(window, text = "What make you S.P.E.C.I.A.L. during COVID 19?", bg = "black", fg = "white", font= "none 12 bold").grid(row=1, column=0,columnspan = 7)
#adding a submit button
strength_btn = Button(window, text= 'STRENGTH', width  = 12, command= lambda: click('STRENGTH')) .grid(row=3, column=0)
perception_btn = Button(window, text= 'PERCEPTION', width  = 12, command= lambda:click('PERCEPTION')) .grid(row=3, column=1)
endurance_btn = Button(window, text= 'ENDURANCE', width  = 12, command= lambda:click('ENDURANCE') ) .grid(row=3, column=2)
charisma_btn = Button(window, text= 'CHARISMA', width  = 12, command= lambda:click('CHARISMA')) .grid(row=3, column=3)
intelligence_btn = Button(window, text= 'INTELLIGENCE', width  = 12, command= lambda:click('INTELLIGENCE')) .grid(row=3, column=4)
agility_btn = Button(window, text= 'AGILITY', width  = 12, command= lambda:click("AGILITY")) .grid(row=3, column=5)
luck_btn = Button(window, text= 'LUCK', width  = 12, command= lambda:click('LUCK')) .grid(row=3, column=6)
#Crating another label to describe cullen
Label(window, text = "\n Definition:", bg = "black", fg = "white", font= "none 12 bold").grid(row=4, column=0, sticky=W,columnspan=7)
#making an output
output = Text(window , height= 6, wrap = WORD, background = "white") # WRAP = WORD  wraps the text when it overflows
output.grid(row=11, column=0, sticky=W , columnspan = 7)

#making the dictionary
my_compdictionary = {
'STRENGTH':'Strength:\nThe quality or state of being physically strong. \nMight need to carry groceries for yourself and others!',
'PERCEPTION':"""Perception:\nThe state of being or process of becoming aware of something through the senses. \nBe aware of how distant you are from others. Don't get too close!""",
'CHARISMA': 'Charisma:\nCompelling attractiveness or charm that can inspire devotion in others. \nInspire your friends and family during this time, and be kind to others. People will be more inclined to help you if you are kind and inspire other people.',
'ENDURANCE':"""Endurance:\nThe fact or power of enduring an unpleasant or difficult process or situation without giving way.\nMake sure you do not give up during this time. \nTough times don't last, Tough people do!""",
'INTELLIGENCE':'Intelligence:\nThe ability to acquire and apply knowledge and skills. \nNow is the time to make sure that you are wise with your resources and to know where to get more supplies.',
'AGILITY':'Agility:\nAbility to move quickly and easily. \nYou may have to move fast if someone gets too close to you! \nSOCIAL DISTANCING!!!',
'LUCK':"""Luck:\nSuccess or failure apparently brought by chance rather than through one's own actions. \nIt may take some luck, but the odds are in your favor if you follow social distancing!"""
}

window.mainloop();
