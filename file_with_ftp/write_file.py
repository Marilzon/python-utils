from datetime import date

today = date.today()

file = open("infos.txt", "w")
actual_date = "Data " + str(date.today())

file.write(actual_date)

file.close()
