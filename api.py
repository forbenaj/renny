from characterai import PyCAI

def chat(message):
    client = PyCAI('39b1fa309f245479a9f440cebb1af394399ac90a')
        
    data = client.chat.send_message('tDMVnZFsQxT33IY306y5Fia_AYhfqgx3ecUYIpo6ZWQ', message)
    
    message = data['replies'][0]['text']
    #name = data['src_char']['participant']['name']
    
    #print(f"{name}: {message}")
    return message