#Exercise 1

for number in range(1,1000):
    cubed = number ** 3
    if cubed >1000:
        break
    print (cubed)

#Exercise 2
    
for a in range(2, 101):
    number = a
    divisors = []
    for b in range (1,number+1):
        if number%b == 0:
            divisors.append(b)
    if len(divisors) == 2:
        print (number)


#Exercise 3
        
age = int(input(" How old are you? "))

if age < 18:
    print("You're a kid!")
elif age <= 65:
    print("You're an adult!")
else:
    print("You're a senior!")