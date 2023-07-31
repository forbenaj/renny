#API Connecting to the Character.ai webpage

from characterai import PyCAI

def chat(message):
    client = PyCAI('39b1fa309f245479a9f440cebb1af394399ac90a')


    #Character ID, found in the url
    char = 'tDMVnZFsQxT33IY306y5Fia_AYhfqgx3ecUYIpo6ZWQ'
    
    #Send the message, wait for the response
    data = client.chat.send_message(char, message)
    
    #Get last response
    response = data['replies'][0]['text']

    return response