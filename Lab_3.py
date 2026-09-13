

def get_username():
    username = input ("Enter your username: ")
    return username.strip().upper()

def get_group():
    group = input ("Enter group chat: ")
    return group.strip().upper()

def get_message():
    message = input ("Enter your message: ")
    return message.strip().upper()

def initialize_chat():
    username = get_username()
    group = get_group()

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf-8'))
        except(KeyboardInterrupt, SystemExit):
            break

    channel.send("Stop".encode('utf-8'))
    print("finished")

start_chat()

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")