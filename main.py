import slack
import json

from sender import Sender

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    try:
        client = slack.WebClient(token=config['bot_token'])

        sender = Sender(client)
        sender.send(config['channels'])
    except Exception:
        print("Error")
        exit(-1)
    print('ok')