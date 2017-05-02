# Azure storage account and secret key
azure_storage_account = ""
key=""

import random, string
from azure.storage.queue import QueueService

# Initialize the service
queue_service = QueueService(account_name=azure_storage_account, account_key=key)

# Create a new queue
queue_service.create_queue('testqueue')

# Put a message into the queue
rnd = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))

print (rnd)

queue_service.put_message('testqueue', rnd)

# Peek at all messages in the queue - without dequeuing or deleting
messages = queue_service.peek_messages('testqueue')
for message in messages:
	print ("expiration_time: " + message.expiration_time)
	print ("insertion_time: " + message.insertion_time)
	print ("message_id: " + message.message_id)
	print ("message_text: " + message.message_text)
	print ("expiration_time: " + message.expiration_time)
	print ("pop_receipt: " + message.pop_receipt)
	print ("time_next_visible: " + message.time_next_visible)
