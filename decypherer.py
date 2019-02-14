# for decyphering the cyphers
# version 1
# couldnt find "file _1C67.txt",

file_names = ["File_30d3.txt"]

'''"file_063d.txt",  "file_0936.txt", "file_0aa7.txt",
              "File_0d01.txt", 
              "file_1f87.txt", "File_21c1.txt",
              "file_2a62.txt" , "file_340b.txt", '''

def open_file(file_name):
    with open ("text_files/" + file_name, 'r') as f:
        return f.read()



'''~~~~~~~~~ The Cyphers ~~~~~~~~~'''
#1 the ascii replace
def substitution_cypher(string):
     key = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
     answer = ""
##     ''' this encrypts -- go in reverse
##     for letter in string:
##          letter_number = ord(letter)-32
##          answer += key[letter_number]'''
    
     for letter in string:
        number = key.find(letter) + 32
        answer+= chr(number)
        #print (letter + "   " + chr(number))
         
     print (answer)

#vigenere cipheR
def vigenere_cypher(string, key):
    answer = ""

    for i in range (len(string)):
        encripted_num = ord(string[i])
        unencripted_num =  encripted_num - (ord(key[i%(len(key))]))
        while unencripted_num < 32:
            unencripted_num += 95
        answer += chr(unencripted_num)

    return answer
        
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


for f in file_names:
    print("""*******
            new test


                 """)
    file = open_file(f)
    #substitution_cypher(file)
    print(vigenere_cypher(file, "enigma"))
