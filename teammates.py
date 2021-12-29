import socket
import keyboard

# SETTINGS
key = "c"
support_ip = "1.2.3.4"
port = 3333

while True:
    keyboard.wait(key)
    s = socket.socket()
    s.connect((support_ip, port))
    s.close()
