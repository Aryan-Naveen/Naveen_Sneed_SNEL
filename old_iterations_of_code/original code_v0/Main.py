import chi_squared
import char_counter

with open ('file.txt', 'r') as f:

     file = f.read().splitlines()

string_count = char_counter.char_counter(file)
chi = chi_squared.chi_squared(string_count)

print(chi)
