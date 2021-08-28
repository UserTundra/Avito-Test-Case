import unittest
import slack
from unittest.mock import MagicMock

from sender import Sender


class SenderTestCase(unittest.TestCase):
    def test_sender_positive(self):
        channels = [
            {
                "channel": "test1",
                "text": "Hello, world!"
            }
        ]
        client = slack.WebClient()
        client.chat_postMessage = MagicMock(return_value = 0)

        sender = Sender(client)
        sender.send(channels)
        for msg in channels:
            client.chat_postMessage.assert_called_with(channel = msg['channel'], text = msg['text'])

    def test_sender_negative(self):
        channels = [
            {
                "channel": "test0",
                "text": "Bad day, huh"
            }
        ]

        client = slack.WebClient()
        client.chat_postMessage = MagicMock(return_value = 0)
        client.chat_postMessage.side_effect = Exception("Boom!")
        sender = Sender(client)

        with self.assertRaises(Exception):
            sender.send(channels)

if __name__ == '__main__':
    unittest.main()
