import socket

def request():
    response = "S"
    while(response == "S"):
        url = input("Digite ula url: ")
        ip = socket.gethostbyname(url)

        print("o IP referente a url informada é: ", ip)

        response = input("Digite S para continuar ou ENTER para sair: ").upper()
    if( response == "S"):
        return request()
    else:
        return

request()
