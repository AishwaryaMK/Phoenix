from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

cbot = ChatBot('phoenix')
cbot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/DELL/Downloads/Chatbot_Project-master/data/'):
    source = open('C:/Users/DELL/Downloads/Chatbot_Project-master/data/'+ files,'r').readlines()
    cbot.train(source)
    
while True:
    message  = input('me')
    if message.strip()!='Bye':
        
        reply = cbot.get_response(message)
        print('ChatBot :',reply)
    if message.strip() =='bye':
        print('ChatBot : bye')
        break 
  
