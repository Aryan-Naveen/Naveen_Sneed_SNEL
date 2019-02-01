#river version

# open the file
with open ('file.txt', 'r') as f:
     file = f.read()
     
#River
#2/1/2019

def char_counter(file_string):

    chars=[0]*127

    for letter in file_string:
        chars[ord(letter)] += 1

    return chars[32:]


#Aryan Naveen
#January 31, 2019

def chi_squared(list):
    chi = 0
    expected = sum(list)/len(list)
    for num in list:
        chi += ((num - expected)**2)/expected

    return chi



string_count = char_counter(file)
chi = chi_squared(string_count)

print(chi)
