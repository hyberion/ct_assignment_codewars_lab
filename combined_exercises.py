#Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#*********************************************************************************************************************#
    
#Count Vowels

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

#*********************************************************************************************************************#

#Number to String

def number_to_string(num):
    return str(num)

#*********************************************************************************************************************#