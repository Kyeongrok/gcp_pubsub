import time
import os
from google.cloud import pubsub_v1
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    '/Users/mattheu/coexon-seoul-dev-898d91a66539.json')

project           = "coexon-seoul-dev"
subscription_name = "my-sub"

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
subscription_path = subscriber.subscription_path(
    project, subscription_name)

def callback(message):
    print('Received message: {}'.format(message))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking, so we must keep the main thread from
# exiting to allow it to process messages in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)