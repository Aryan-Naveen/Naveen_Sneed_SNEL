import random

j=0
text = ""

file = open('file.txt', 'w')
for j in range (18000):
    text += chr(random.randint(32, 126))

file.write(text)
