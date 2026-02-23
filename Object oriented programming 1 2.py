class fruit:

  def __init__(self, name, color):
    self.name = name
    self.color = color

apple = fruit('Apple','Red')

banana = fruit('Banana', 'Yellow')

print(apple.color,apple.name)

print(banana.color, banana.name)

print(banana.name,apple.name)