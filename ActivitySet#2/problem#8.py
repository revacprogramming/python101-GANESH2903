class Menu:
  def __init__(self):
    pass


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)





# class Menu:
#   def __init__(self,food,qty):
#     self.food = food
#     self.qty = qty
#   def __setattr__(self,food,qty):
#     self.__dict__[food]=qty
  


# m = Menu("item",10)
# m.idly=30
# m.vada=20
# # m["idly"] = 10
# # m["vada"] = 20

# print(m.__dict__)
