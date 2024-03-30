fruits = ["Appel", "Orange", "Peach"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
for number in range(1, 10):
    print(number)

total = 0
for number in range(1, 101) :
    if number % 2 == 0:
        total += number
print(total)

target = 100
for number in range(1, target+1) :
    if number % 3 == 0 and number % 5 == 0 :
        print("fizzbuzz")
    elif number % 3 == 0 :
        print("fizz")
    elif number % 5 == 0 :
        print("buzz")
    else:
        print(number)
