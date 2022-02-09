class Book():
  def __init__(self): #constructor
      self.title = 'Guia desenvolvedor web' #attr
      self.isbn = 878844 #attr
      print('Construtor chamado para criar um objeto desta classe')

  def print(self): #method
    print('Foi criado o livro %s e ISBN %d' %(self.title, self.isbn))

PythonBook = Book()

print(type(PythonBook))
print(PythonBook.print())
