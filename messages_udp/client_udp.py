from socket import *

server = '127.0.0.1'
port = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
quit = ""

while quit != "Q":
  message = input("Digite sua mensagem: ")
  obj_socket.sendto(message.encode(), (server, port))
  data, origin = obj_socket.recvfrom(65535)
  print("Resposta do servidor: ", data.decode())
  quit = input("Digite Q para sair: ").upper()

obj_socket.close()
