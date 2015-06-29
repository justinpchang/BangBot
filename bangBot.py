'''
bangBot.py

author: ALL_ABORED
date: 6/29/2015
version: 1.0

shoots down Snoos faster than... something thats fast
'''

import socket

# config vars
server = "irc.veuwer.com"
port = 6667
channel = "#voat"
nick = "nickgoeshere"
trigger = "A wild Snoo appeared!"

# connect to the server
def connect():
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, port))

# user auth
def auth():
    ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :Snoo killing machine.\n")
    ircsock.send("NICK "+ nick +"\n")

# respond to server pingeys
def ping():
    ircsock.send("PONG :Pong\n")

# send message to channel
def sendmsg(chan, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")

# join a channel
def joinchan():
    ircsock.send("JOIN " + channel + "\n")

# THAT IS MY TRIGGER
def trigger():
    ircsock.send("PRIVMSG " + channel + " :.bang\n")

connect()
auth()
joinchan()

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    pring(ircmsg)

    if ircmsg.find(":A wild Snoo appeared!" or ":The Voat Goat appeared!") != -1:
        trigger()

    # respond to pingeys
    if ircmsg.find("PING :") != -1:
        ping()
