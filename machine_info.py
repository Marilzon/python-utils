import platform
from datetime import datetime
import getpass
import socket

print("Usuario: ", getpass.getuser())
print('Nome da maquina: ', platform.node())
print('Arquiquetura: ', platform.architecture())
print('S.O: ', platform.system())
print('Versao: ', platform.release())
print('Processador: ', platform.processor())
print('Versao do python: ', platform.processor())
print('IP Local: ', socket.gethostbyname(socket.gethostname()))

print(
  'Data: ',
  datetime.now().day,"/",
  datetime.now().month,"/",
  datetime.now().year)

