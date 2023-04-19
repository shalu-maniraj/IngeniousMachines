import openai

# set up your OpenAI API credentialsl
openai.api_key = "YOUR_API_KEY"

# create a prompt for the chatbot to generate a response
prompt = ""

# define a function to get the chatbot's response to user input
def get_response(input_text):
    # append the user's input to the prompt
    prompt_with_input = prompt + " " + input_text.strip() + "\nAI:"
    
    # define dictionary of responses for different user inputs
responses = {
    "hi": "Hello! How can i help you?",
    "i need to make an appointment": "Sure, what type of appointment are you looking for?",
    "i need to see a doctor for checkup": "Ok, Could you tell your Patient ID?",
    "yes 207068":" Great, when would you like to schedule the appointment?",
    "next friday at 3 pm": "Okay, let me check the availability. Yes, we have an opening at 3:15 pm. Would you like to confirm this appointment?",
    "yes please confirm": "Ok, It's Confirmed.Is there anything else I can help you with?",
    "no":"Alright, feel free to contact us if you need any further assistance. Have a great day!",
    "ok bye":"Goodbye"

}

# main function to handle user input and generate AI responses
def main():
    # greet the user and ask for input
    print("Hi there! I'm an Doctor - Book chatbot. I'm here to help you?")
    
    # loop to continuously get user input and generate AI responses
    while True:
        # get user input
        user_input = input("> ")
        
        # check if the user wants to end the conversation
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Goodbye! Have a nice day")
            break
        
        # get AI response based on user input
        if user_input.lower() in responses:
            ai_response = responses[user_input.lower()]
        else:
            ai_response = "I'm sorry, I don't understand. Can you please try again?"
            
        
        # print AI response
        print("AI: " + ai_response)
      

# call main function
if __name__ == "__main__":
    main()
