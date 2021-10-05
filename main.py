from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
bot=ChatBot("My Bot")
convo = {
    'hello',
    'hi there !',
    'what is your name ?',
    'I am your Assistant.You can ask any query here',
    'how are you ?',
    "I'm pretty good thanks for asking.",
    'thank you',
    'In which city you live ?',
    'How can I help you',
    'In which language you talk?',
    ' I mostly talk in english',
    'Here you can get all information for your crop',
    'Nice to meet u',
    'Good Afternoon, Good to see you again, need some more help?',
    'Good Morning, Good to see you again, need some more help?',
     'Good Evening, Good to see you again, need some more help?',
     "Sure, I'll be here if you need any other information.",
      "The weather is just perfect for me",
      'I am sorry, currently I do not have information about the same. For any other assistance'
}
trainer=ListTrainer(bot)
#now training the bot with the help of Trainer
trainer.train(convo)
#answer=bot.get_response("What's your name?")
#print(answer)
#print("Talk to bot")
#while True:
    #query=input()
   # if query=='exit':
      #  break
    #answer=bot.get_response(query)
   # print("bot : ",answer)
main =Tk()
main.geometry("500x650")
main.title("Assistant Virtuel")
img=PhotoImage(file="img.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
def ask_from_bot():
    query=textF.get()
    answer_from_bot= bot.get_response(query)
    msgs.insert(END,"you: "+ query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot: "+ str(answer_from_bot))
    textF.delete(0,END)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()
main.mainloop()