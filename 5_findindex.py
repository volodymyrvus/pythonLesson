import random
guess=int(input("Lets guess number in list: "))
a=[random.randint(0,9) for i in range(50)]
print(a)
print('Your numbers in',  a.index(guess)+1, 'possituion.')
print('Your numbers counted',  a.count(guess), 'times in this list.')
