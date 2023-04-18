import requests
import json
import openai

openai.api_key = "YOUR_SECRET_KEY"

def generate_response(user_input):
    prompt = f"Generate a response to the user input: '{user_input}'\n\nResponse:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_SECRET_KEY&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def display_weather(city, data):
    if data['cod'] == 200:
        print(f"Location: {city}")
        print(f"Weather data: {data}")
        temp = data['main']['temp']
        print(f"The weather in {city} is currently {data['weather'][0]['description']} with a temperature of {temp} degrees Celsius.")
    else:
        response = generate_response(f"What is the weather in {city}?")
        print(response)

def main():
    print("Welcome to weather-bot! How can I help you?")
    while True:
        user_input = input("User: ").strip().lower()
        if user_input == "thank you":
            print("Goodbye!")
            break
        else:
            data = get_weather_data(user_input)
            display_weather(user_input, data)

if __name__ == '__main__':
    main()