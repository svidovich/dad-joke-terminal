#!/usr/bin/env python3

import json
import requests


def main():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json', 'User-Agent': 'dad-joke-terminal'})
    joke: dict = json.loads(response.text)
    if 'joke' in joke.keys():
        print('Dad says:')
        print(f"\t{joke['joke']}")
    else:
        print("Sorry champ, Dad just couldn't find a joke for you this time.")
    

if __name__ == '__main__':
    main()
