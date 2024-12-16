
# QUESTION 2
for i in range(1, 13):
    for j in range(1, 13):
        print(i*j, end = '\t')
    print()


# QUESTION 3
for i in range(1, 13):
    for j in range(1, i+1):
        print(i*j, end = '\t')
    print()

# QUESTION 3
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
if a < 0 or b < 0:
  print("This program does not support negative numbers")
else:
  c = 0
  while b > 0:
    c += a
    b -= 1
  print("c = ", c)