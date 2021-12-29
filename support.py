import socket
from pynput.keyboard import Controller

# SETTINGS
port = 3333
key_to_press = 'r'

s = socket.socket()
s.bind((socket.gethostname(), port))
s.listen(5)
keyboard = Controller()

while True:
    clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established.")
    clientsocket.close()
    keyboard.press(key_to_press)
    keyboard.release(key_to_press)
