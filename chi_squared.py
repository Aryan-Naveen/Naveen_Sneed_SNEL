
#Aryan Naveen
#January 31, 2019

def chi_squared(list):
    chi = 0
    expected = sum(list)/len(list)
    for num in list:
        chi += ((num - expected)**2)/expected

    return chi

