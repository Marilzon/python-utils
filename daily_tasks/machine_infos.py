import platform
from datetime import date
import getpass
import socket

def machine_infos():
    print("Usuario: ", getpass.getuser())
    print('Nome da maquina: ', platform.node())
    print('Arquiquetura: ', platform.architecture())
    print('S.O: ', platform.system())
    print('Versao: ', platform.release())
    print('Processador: ', platform.processor())
    print('Versao do python: ', platform.python_version())
    print('IP Local: ', socket.gethostbyname(socket.gethostname()))
    # CONVERTING DATE STYLE TO BRAZILLIAN DEFAULT
    actual_date = date.today()
    print('Data da consulta: ', actual_date.strftime('%d/%m/%Y'))
    return

machine_infos()
