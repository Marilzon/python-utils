class Book():
  def __init__(self, title, release): #constructor
      self.title = title #prop
      self.release = release #prop
      print('Construtor chamado para criar o objeto desta classe')

  def print(self): #method
    print('Foi criado o livro %s e lancamento %s' %(self.title, self.release))

DevGuide = Book('Guia desenvolvedor', '13/05/2022')

print(type(DevGuide))
print(DevGuide.print())
