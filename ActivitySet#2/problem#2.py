
def add(a, b):
  sum = a + b
  return sum


def output(a, b, sum):
  return print(sum)


def main():
  a = int(input('input?'))
  b = int(input('input?'))
  sum = add(a, b)

  output(a, b, sum)


if __name__ == '__main__':
    main()
