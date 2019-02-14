#River
#2/1/2019

def char_counter(file_string):

    chars=[0]*127

    for letter in range(len(file_string)):
        chars[ord(file_string[letter])] += 1

    return chars
    
