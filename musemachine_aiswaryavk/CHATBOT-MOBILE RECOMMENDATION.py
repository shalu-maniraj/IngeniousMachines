#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing modules
import openai
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API credentials
openai.api_key = 'your api here'

# Define function to extract smartphone data from Flipkart
def extract_smartphone_data(brand, ram):
    url = f"https://www.flipkart.com/search?q={brand}+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&sort=price_asc&ram={ram}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    smartphone_list = []
    for item in soup.select("._2kHMtA"):
        name = item.select_one("._4rR01T").text
        rating = item.select_one("._3LWZlK").text
        price = item.select_one("._30jeq3._1_WHN1").text
        smartphone_list.append(f"{name} ({rating}, {price})")
    return smartphone_list

# Define function to generate smartphone recommendations based on brand and RAM
def generate_smartphone_recommendations(brand, ram):
    prompt = f"Please recommend all smartphones by {brand} with {ram}GB RAM from Flipkart"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    smartphone_list = response.choices[0].text.strip().split("\n")
    return smartphone_list

# Define function to handle user input and generate bot response
def respond(user_input):
    if user_input.lower() == 'exit':
        return 'Goodbye!'
    else:
        try:
            brand, ram = user_input.split(',')
            smartphone_list = extract_smartphone_data(brand, ram)
            if smartphone_list:
                response = f"Here are all the smartphones by {brand} with {ram}GB RAM on Flipkart:\n"
                for smartphone in smartphone_list:
                    response += f"- {smartphone}\n"
                return response
            else:
                return f"Sorry, I could not find any smartphones by {brand} with {ram}GB RAM on Flipkart."
        except (ValueError, TypeError):
            return "Please enter a valid input in the format: 'Brand, RAM'."
        except openai.Error as e:
            return f"Sorry, there was an error: {e}."
        
# Define main function to run the chatbot
def main():
    print("Hello! I am a Flipkart smartphone recommendation bot. You can ask me for all the smartphones of any brand with a specific RAM capacity. Type 'exit' to quit.")
    while True:
        user_input = input("Enter the brand and RAM of the smartphone (format: Brand, RAM): ")
        bot_response = respond(user_input)
        print(bot_response)
        if bot_response == "Goodbye!":
            break
            
# Run the chatbot
if __name__ == '__main__':
    main()            


# In[ ]:




