import unittest
import slack
import json

from sender import Sender


class MainTestCase(unittest.TestCase):
    def test_main(self):
        with open('./../config.json') as f:
            config = json.load(f)

        client = slack.WebClient(token=config['bot_token'])

        sender = Sender(client)
        result = sender.send(config['channels'])
        for r in result:
            self.assertTrue(r['ok'], "message to channel was not delivered")

if __name__ == '__main__':
    unittest.main()
