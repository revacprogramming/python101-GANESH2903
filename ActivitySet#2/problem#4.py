l=[]
t=tuple()

def get_cs():
  #s=input('Enetr a string')
  s='system=s;database=d;username=u;passwd=p'
  return s


def cs_to_lot(cs):
  x=cs.split(';')
  ln=len(x)
  for i in range(ln):
    y=x[i].split('=')
    t=tuple(y)
    new = l.append(t)
  return new

def lot_to_cs(lot):
  """convert list of strings to connected string"""
  equal = '='
  separate = ';'
  ln=len(lot)
  for i in range(lot):
    lot[i]=equal.join(lot[i])
  return lot
    
def main():
  cs=get_cs()
  lot=cs_to_lot(cs)  # convert connect string to list of tuples
  print(lot)
  
  cs=lot_to_cs(lot)  # convert list of strings to connect string
  separate=';'
  newcs=separate.join(cs)
  return newcs


if __name__ == '__main__':
  main()
print(newcs)
