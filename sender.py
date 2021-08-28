class Sender:
    def __init__(self, client):
        self.client = client

    def send(self, channels):
        result = []
        for message in channels:
            #self.client.chat_postMessage(channel=message['channel'], text=message['text'])
            result.append(self.client.chat_postMessage(channel=message['channel'], text=message['text']))
        return result