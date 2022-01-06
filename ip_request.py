import socket

response = "S"

while(response == "S"):
  url = input("Digite ula url: ")
  ip = socket.gethostbyname(url)

  print("o IP referente a url informada é: ", ip)

  response = input("Digitte S para continuar: ").upper()
