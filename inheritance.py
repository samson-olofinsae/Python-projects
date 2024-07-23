# inheritance
class Mammals:
  def walk(self):
    print ('walk')

class Dog(Mammals):
  def bark(self):
    print ('bark')
  #print('bark')
class Cat (Mammals):
  def be_annoying(self):
    print('mewing')
  
class Humans(Mammals):
    def talk(self):
      print('talk')

# dog = Dog()
# dog.bark()
# cat = Cat()
human = Humans()
human.talk()
