
# open the file
def file_num_to_hex(dec):
     num=hex(dec)[2:]
     num_zero = 4-len(num)
     return num_zero * "0" + num  

def generate_file(i):
    file_name = "file_" + i +".txt"
    #print("folder_of_files/" + file_name)
    with open ("text_files/" + file_name, 'r') as f:
        return f.read()
 

file_size = 18000 


answer = ""

for i in range (file_size):
     num = file_num_to_hex(i)
     file = generate_file(num)
     answer+= file[0]
     
print(answer)
