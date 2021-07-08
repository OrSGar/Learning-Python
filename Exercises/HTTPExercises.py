import requests
from random import choice
from pyfiglet import print_figlet

'''
Ask for a joke topic - if we get mutiple results, get one at random
- Send request
- Check number of results 
    - Multiple jokes
    - One joke
'''


def get_jokes(topic):
    url = "https://icanhazdadjoke.com/search"
    header = {"Accept": "application/json"}

    response = requests.get(url, headers=header, params={
        "term": topic
    })

    joke_json = response.json()
    jokes = joke_json["results"]

    return jokes


print_figlet("Cheesy Joke Generator", font="slant", colors="MAGENTA")

user_topic = input("Let me tell you a joke! Give me a topic: ")

topic_jokes = get_jokes(user_topic)


if len(topic_jokes) == 0:
    print(f"Sorry, I dont have any jokes about {user_topic}! Please try again.")
elif len(topic_jokes) == 1:
    print(f"Ive got one joke about {user_topic}. Here it is:")
    print(choice(topic_jokes)["joke"])
else:
    print(f"Ive got {len(topic_jokes)} jokes about {user_topic}. Here it is:")
    print(choice(topic_jokes)["joke"])


