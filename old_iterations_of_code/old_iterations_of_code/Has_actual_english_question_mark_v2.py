#river version

# open the file

def generate_file(i):
    file_name = "file" + str(i) +".txt"
    print("folder_of_files/" + file_name)
    with open ("folder_of_files/" + file_name, 'r') as f:
        return f.read()
     
#River
#2/1/2019

#count the amount of each letter
def char_counter(file_string):

    chars=[0]*127

    for letter in file_string:
        chars[ord(letter)] += 1

    return chars[32:]


#Aryan Naveen
#January 31, 2019

#creates chi square value
def chi_squared(list):
    chi = 0
    expected = sum(list)/len(list)
    for num in list:
        chi += ((num - expected)**2)/expected

    return chi

file_size = 100
for i in range (file_size):
    file = generate_file(i)
    string_count = char_counter(file)
    chi = chi_squared(string_count)
    print(chi)

