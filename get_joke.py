#!/usr/bin/env python3

import argparse
import cowsay
import json
import requests


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--cow', action='store_true', required=False, help='A cow tells the joke.')
    args = parser.parse_args()

    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json', 'User-Agent': 'dad-joke-terminal'})
    joke: dict = json.loads(response.text)
    if 'joke' in joke.keys():
        joke = joke['joke']
        if args.cow:
            cowsay.cow(joke)
        else:
            print('Dad says:')
            print(f"\t{joke}")
    else:
        print("Sorry champ, Dad just couldn't find a joke for you this time.")
    

if __name__ == '__main__':
    main()
