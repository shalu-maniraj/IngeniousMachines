from nltk.chat.util import Chat,reflections
qna=[
    [r'hi joe',['hi john']],
    [r'how are you',['iam fine hoping you good']],
    [r'where are you working right now?',['Iam working at the Ust global']],
    [r'Oh really,what is your post there',['iam working as a software engineer']],
    [r'that really nice to hear',['thanks Rini,what about you?']],
    [r'Iam working at the goverment college as lecturer',['oh great']],
    [r'I have to catch my class,going bye',['sure,bye']],
    
    

]
def chatbot():
    print("welcome to chatbot,How can i help you") 
    chat=Chat(qna,reflections)
    return chat.converse()

if __name__=="__main__":
    chatbot()