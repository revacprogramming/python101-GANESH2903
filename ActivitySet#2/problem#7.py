
class Menu:
    """fill in class definition here"""
  def __init__(self,food):
    self.food=food
    
  def __add__(self,qty):
    print(self.food,qty)

m1 = Menu("idly",10)
m2 = Menu("vada",20)
m = m1 + m2  # Hint: operator overloading special methods (__add__, __sub__, etc.)




print(m)  # should print the menu properly