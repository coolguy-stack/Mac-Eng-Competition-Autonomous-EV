import speech_recognition as sr
import numpy as np
import random
import time

#This is a speech to text program which we wished to implement with the communication interface, however we ran into some troubles with implementation and ran out of time.

r=sr.Recognizer()


class comm:
     
    def __innit__(self, velocity, is_passenger, weather, airbag, music, volume, acceleration, self_driving, speed):
        self.speed = speed
        self.is_passenger = is_passenger
        self.weather = weather
        self.airbag = airbag
        self.music = music
        self.volume = volume
        self.acceleration = acceleration
        self.self_driving = self_driving
        return

    def speech2text(self):
        x=0
        while x<1:
        
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                
                print('Please say your response: ')
                
                audio = r.listen(source)
                
                try:
                    y=r.recognize_google(audio)
                    print(y)
                    
                except Exception as e:
                    print("error: "+str(e))
            x+=1
        return y
    
    def entermessage(self):
        yes=['yes','yup','yea']
        incoming_messages=['What time are you free today?','Are you busy this weekend?',
                           'When are you reaching home?','Can you grab groceries on your way home?']
        auto_messages='Sorry, I am driving. Can I call you later?'
        print('You have an incoming message: \n' + incoming_messages[random.randrange(0,len(incoming_messages))])
        time.sleep(0.1)
        speech=str(self.speech2text())
        print('Is this what you want to send?')
        speech=str(self.speech2text())
        for i in range(0,len(yes)):
            if speech in yes:
                print('Message sent!')
                break
            else:
                print('Alright, the following message will be sent: \n'+ auto_messages)
                break


c = comm()
c.entermessage()
        
        
        