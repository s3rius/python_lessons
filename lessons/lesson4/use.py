from collections import Counter

def main(filename) -> int:
  with open(filename) as file:
    lines = file.readlines()
  counter = 0 
  for line in lines: 
    c = Counter(line)
    if c['E'] > c['A']:
      counter += 1
  return counter


if __name__ == "__main__" :
  print(main("lessons/lesson4/test_data.txt"))