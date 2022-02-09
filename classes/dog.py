
class Dog():
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print('Construtor chamado para criar o objeto desta classe')

  def bark(self):
    print('%s - %s Says: Woof! Woof' %(self.breed, self.name))

Kiara = Dog('Kiara', 'PIT-BULL')
Mickey = Dog('Mickey', 'PASTOR ALEMAO')

print(Kiara.bark())
print(Mickey.bark())
