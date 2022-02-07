import os

message = input("Digite uma mensagem: \n")

file = open(os.path.join("message.txt"), "w")

for word in message.split():
  file.write(word + ' ')

print("Conteodo gravado no arquivo message.txt")
file.close()
