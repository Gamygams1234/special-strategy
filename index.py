from tkinter import *
#keydown function
#first define the click event
def click():
    entered_text = textentry.get() #this will collect the data from the text emtry
    output.delete(0.0, END)#making sure the text box is clear
    try:
        definition = my_compdictionary[entered_text]
    except :
        definition = 'Sorry that is not an attrubute to become SPECIAL!'
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
Label(window, image= photo1, bg = 'black') .grid(row=0, column=0, sticky=W)
# Label for text
Label(window, text = "How do I survive COVID 19 in a S.P.E.C.I.A.L. way?", bg = "black", fg = "white", font= "none 12 bold").grid(row=1, column=0, sticky=W)
#creating an entry for a text box
textentry = Entry(window, width= 30, bg = "white")
textentry.grid(row= 2, column=0, sticky = W)
#adding a submit button
Button(window, text= 'SUBMIT', width  = 6, command= click) .grid(row=3, column=0, sticky=W)
#Crating another label to describe cullen
Label(window, text = "\n Definition:", bg = "black", fg = "white", font= "none 12 bold").grid(row=4, column=0, sticky=W)
#making an output
output = Text(window, width = 75 , height= 6, wrap = WORD, background = "white") # WRAP = WORD  wraps the text when it overflows
output.grid(row=5, column=0, sticky=W)

#making the dictionary
my_compdictionary = {
'strength':'The quality or state of being physically strong.',
'perception':'The state of being or process of becoming aware of something through the senses.',
'endurance':'The fact or power of enduring an unpleasant or difficult process or situation without giving way.',
'intelligence':'The ability to acquire and apply knowledge and skills.',
'agility':'Ability to move quickly and easily.',
'luck':"""Success or failure apparently brought by chance rather than through one's own actions."""
}
#to exit
Label(window, text = "To exit the program, click here:", bg = "black", fg = "white", font= "none 12 bold").grid(row=6, column=0, sticky=W)
# exit Button
Button(window, text= 'Exit', width  = 4, command= close_window) .grid(row=7, column=0, sticky=E)
#close window


window.mainloop();
