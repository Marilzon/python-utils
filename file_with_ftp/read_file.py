file = open("infos.txt", "r")

data = file.read()
rows = data.split(" ")
full_data = []

for row in rows:
  full_data.append(row)

print(full_data)
