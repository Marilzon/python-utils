import getpass
import socket

current_user = getpass.getuser()
current_address = socket.gethostbyname(socket.gethostname())

# Debugg trick {var =} sintax
print(f'hello sci, {current_user = }, you addres is {current_address}')
