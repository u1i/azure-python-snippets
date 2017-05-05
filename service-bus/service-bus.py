from azure.servicebus import ServiceBusService, Message, Queue

from random import randint

# Initialize

bus_service = ServiceBusService(
    service_namespace='YOUR_NAMESPACE',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='YOUR_KEY')


# Create a queue
bus_service.create_queue('myqueue')

# queue_options = Queue()
# queue_options.max_size_in_megabytes = '5120'
# queue_options.default_message_time_to_live = 'PT1M'
# bus_service.create_queue('myqueue', queue_options)

# Add message to queue
msg = Message(b'Test Message ' + str(randint(1000,9999)))
bus_service.send_queue_message('myqueue', msg)

# Read messages
msg = bus_service.receive_queue_message('myqueue', peek_lock=False)
print(msg.body)
