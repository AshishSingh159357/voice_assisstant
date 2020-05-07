import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import tkinter as tk



import tkinter as tk
from tkinter import messagebox
import pymongo
connection=pymongo.MongoClient('localhost',27017)
database=connection['Junior']
collection=database['emails']






#Emails={'ashish':'as3861425@gmail.com','Jimit':'jimitvaghani2122@gmail.com','DK':'dhruv4458@gmail.com'}

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello sir ashish. what can i help you.")



#to return voice into the string form
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")   
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        
        print("user said:{} ".format(query))
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"
    return query



#sending mail
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.login('as8715819@gmail.com','ashishsingh1234')
    server.sendmail('as8715819@gmail.com',to,content)
    server.close()
    
    

#This is the main program
wishme()      
while True:
    query=takecommand().lower()
    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("searching wikipedia...")
       
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
        
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        
    elif 'play music' in query:
        music_dir='E:\\songs'
        song=os.listdir(music_dir)
        print(song)
        random_song=random.randrange(0,len(song))
        #now starting the file
        os.startfile(os.path.join(music_dir,song[random_song]))
        
    elif 'open chrome' in query:
        path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        os.startfile(os.path.join(path))
        
    elif 'the time' in query:
        strTime=datetime.datetime.now().time()
        print(strTime)
        speak("sir,the time is :{0}".format(strTime))
        
    elif 'send a mail' in query:
        try:
            speak("who you want send")
            to=takecommand()
            emails=collection.find_one({'name':to})
            speak("what you want to send")
            content=takecommand()
            sendEmail(emails['email'],content)
            speak('Email has been sent')
            print("Email has been sent")
        except Exception as e:
            
            #####################################  Application #####################
            


            root=tk.Tk()
            root.geometry('400x400')
            root.title('Junior')


            label1=tk.Label(root,text='Email Data',font=("Helvetica", 30))
            label1.place(x=100,y=15)



            label2=tk.Label(root,text='Name',font=("Helvetica",15))
            label2.place(x=80,y=100)
            txt2=tk.Entry(root,width=20)
            txt2.place(x=150,y=100)


            label3=tk.Label(root,text='Email',font=("Helvetica",15))
            label3.place(x=80,y=150)
            txt3=tk.Entry(root,width=20)
            txt3.place(x=150,y=150)


            def add():
                if '@gmail.com' in txt3.get():    
                    data={'name':txt2.get(),'email':txt3.get()}
                    collection.insert_one(data)
                    messagebox.showinfo('add',"data inserted successfully")
                else:
                    label3=tk.Label(root,text='Ivalid email-id',fg='red')
                    label3.place(x=150,y=200)
    
    
            def update():
                collection.update_many({'name':txt2.get()},{"$set":{'email':txt3.get()}})
                messagebox.showinfo('update','Updated successfully')


            def delete():
                collection.delete_many({'name':txt2.get()})
                messagebox.showinfo('delete','deleted successfully')
    

            def cancel():
                root.destroy()

            #this are the Buttons
            btn1=tk.Button(root,text='ADD',width=10,command=add)
            btn1.place(x=100,y=250)
            btn2=tk.Button(root,text='UPDATE',width=10,command=update)
            btn2.place(x=100,y=300)
            btn3=tk.Button(root,text='DELETE',width=10,command=delete)
            btn3.place(x=200,y=250)
            btn4=tk.Button(root,text='CANCEL',width=10,command=cancel)
            btn4.place(x=200,y=300)


            root.mainloop()
            
            
            
            ##################################### Application ##########################
            speak('sorry Ashish bhai ,i am not able to send a mail')
            print("sorry Ashish bhai ,i am not able to send a mail")
        
           
        
    elif 'shut down' and 'shutdown' in query:
        break
    
