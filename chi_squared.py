numbers = [11, 12, 8, 9, 7, 13]

def chi_squared(list):
    chi = 0
    expected = sum(list)/len(list)
    for num in list:
        chi += ((num - expected)**2)/expected

    return chi

print( chi_squared(numbers) )
