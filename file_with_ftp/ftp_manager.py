from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

user = input("Digiteo o login: ")
password = input("Digite a senha: ")

ftp.login(user, password)

print("Diretorio atual: ", ftp.pwd())

ftp.cwd("pub")

print("Diretorio corrente: ", ftp.pwd())
print(ftp.retrlines("LIST"))

ftp.quit()
