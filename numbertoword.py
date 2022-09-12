start = 0
i = 0
k = 1
numbers = {
    '1' : "one",
    '2' : "two",
    '3' : "three",
    '4' : "four",
    '5' : "five",
    '6' : "six",
    '7' : "seven",
    '8' : "eight",
    '9' : "nine",
    '0' : "zero"
}

value = input ('phone num ')
count = len(value)
print(count)

while  count != start:
  start = start + 1
  sep_value = value[i]
  print(value[i] + ' -> ' + numbers[sep_value] )
  i = i + 1
 
