#Exercise 9: Roll dice in such a way that every time you get the same number
#Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.

import random

for i in range(5):
    random.seed(2)
    print(random.randint(1, 6))
