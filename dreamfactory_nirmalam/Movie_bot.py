#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openai
import re

# set up the OpenAI API credentials
openai.api_key = 'your Api Key Here'

# function to get the movies of an actor with year and ratings
def get_movies(actor_name):
    name_of_actor = re.sub('[^a-zA-Z\s]', '', actor_name).title()
    prompt = f'List movies of {name_of_actor} with year and rating'
    completions = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    movies_data = message.strip().split('\n')
    return movies_data

# function to handle user input and generate bot response
def respond(user_input):
    if user_input.lower() == 'exit':
        return 'Goodbye!'
    else:
        actor_name = user_input
        try:
            movies_data = get_movies(actor_name)
            if movies_data:
                response = f'The movies of {actor_name} are:\n'
                for movie in movies_data:
                    response += f'{movie}\n'
                return response
            else:
                return f'Sorry, I could not find any movies for {actor_name}.'
        except openai.Error as e:
            return f'Sorry, there was an error: {e}.'
        
# main loop to run the chatbot
print('Hello, I am a movie recommendation bot.')
while True:
    user_input = input('Enter the name of an actor: ')
    bot_response = respond(user_input)
    print(bot_response)
    if bot_response == 'Goodbye!':
        break


# In[ ]:




