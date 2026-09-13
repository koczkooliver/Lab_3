def get_peer_node(username): # function name get_peer_node
used to create new username
username: used to create peer node
return: n

def join_group(node, group): # function name join_group
used to let peers go into chatrooms
node: peer to peer node going into chatrooms
group: chatrooms peers can join

def chat_task(ctx, pipe, n, group): # function name chat_task
used to send and receive messages
ctx: This is a ZeroMQ Connection Context
pipe: This is a communications pipe polled by ZeroMQ for messages.
n: This is the peer to peer node my chat app is connected as
group: chatrooms peers can join

def get_channel(node, group): # function name get_channel
used to start chat
node: peer to peer node going into chatrooms
group: chatrooms peers can join
