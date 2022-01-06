import platform
from datetime import datetime
import getpass

print("Usuario: ", getpass.getuser())
print('Nome da maquina: ', platform.node())
print('Arquiquetura: ', platform.architecture())
print('S.O: ', platform.system())
print('Versao: ', platform.release())
print('Processador: ', platform.processor())
print('Versao do python: ', platform.processor())

print(
  'Data: ',
  datetime.now().day,"/",
  datetime.now().month,"/",
  datetime.now().year)
