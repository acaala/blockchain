import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-2aff026a-b404-11eb-8cd6-ee35b8e5702f'
pnconfig.publish_key = 'pub-c-de1f6b83-b216-4ae1-87bf-f44e9754cc31'
pubnub = PubNub(pnconfig)

TEST_CHANNEL =  'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    
    pubnub.publish().channel(TEST_CHANNEL).message({ 'foo': 'bar' }).sync()

if __name__ == '__main__':
    main()


