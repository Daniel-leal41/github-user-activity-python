import argparse
import urllib.request
import json


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


parser_fetch = subparsers.add_parser("github-activity")
parser_fetch.add_argument("username")


args = parser.parse_args()

if args.command == "github-activity":
    url = f"https://api.github.com/users/{args.username}/events"

    with urllib.request.urlopen(url) as answer:
        data = json.loads(answer.read())

    print(data)