import random

j=0
i=0

for i in range(100):
    text = ""
    file = open('file' + str(i) + '.txt', 'w')
    for j in range (18000):
        text += chr(random.randint(32, 126))

    file.write(text)
