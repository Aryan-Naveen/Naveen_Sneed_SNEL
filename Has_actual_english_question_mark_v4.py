# version 3
#added a print statement to print the file number and the
# chi squared value for the file
'''need to change it so that it prints the actual
          name of the file not just the number?'''

# open the file
def return_file_number_in_hex(dec):
     new = hex(dec)
     num=new[2:]
     num_zero = 4-len(num)
     zero = 0
     return num_zero * str(zero) + num  

def generate_file(i):
    file_name = "file_" + i +".txt"
    #print("folder_of_files/" + file_name)
    with open ("text_files" + file_name, 'r') as f:
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
threshold = 150 # < the mimimun chi squared value to indicate that a file may have hidden text

for i in range (file_size):
    num =return_file_number_in_hex(i)
    file = generate_file(j)
    string_count = char_counter(file)
    chi = chi_squared(string_count)

    if (chi > threshold):
        print ("Chi: " + str(chi) + " || file: " + str(i))

