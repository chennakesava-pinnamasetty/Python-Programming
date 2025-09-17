# Here are some rondom types in python they are :

# 1. Import the random variable
     # All random number features comes from 
import random


# 2. Random Integers
       # randint(a,b) -->  random integers between a and b ( inclusive )
print(random.randint(1,9))    # e.g 7


# 3. Random Floats
     # random() --> random floats between 0.0 and 1.0
print(random.random())  # e.g 0.41460
     # uniform(a,b) --> random float between a and b
print(random.uniform(1,10))  # e.g 8.72176


# 4. Random choice from a list
fruits = ["apple", "banana","cherry"]
print(random.choice(fruits))    # e.g banana


# 5. Multiple Random choices
       # choice(population,k = n) --> can repeat items
       # sample(population, k = n) --> no repeats
print(random.choices(fruits, k=2))     # ['banana', 'banana']
print(random.sample(fruits, k=2))      # ['cherry', 'apple']


# 6. Shuffle a list
cards = [1,2,3,4,5]
random.shuffle(cards)
print(cards)             # [1, 3, 2, 5, 4]


# 7. random Ranges
     # randrange( start , stop, step)
print(random.randrange(0,101,5))         # 30


# 8. Using secrets for secure random numbers
      # If you need cryptogrophically secure randommess(password, tokens)
#imoprt secrets
#print(secrets.randbelow(10))   # 0 - 9
#print(secrets.token-hex(8))   # random hex string