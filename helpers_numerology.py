def get_first_name():
    return input("First name: ").title()

def get_middle_name():
    return input("Middle name: ").title()

def get_last_name():
    return input("Last name: ").title()

def get_name(name):
    return input(name + " name: ").title()

#  Sums the value of each of a string's character in the dictionary
def sum_found_char_in_dict(string, dictionary):
    result = 0
    for character in string:
        if character in dictionary:
            result =  result + dictionary[character]
    
    return result

# Accepts a number, takes each digit of number and sums them together. 
# If the sum is greater than 9, repeat the process until you have a single digit
#  ** if the number is 11 or 22 do not keep collapsing

# Ex: 123  => 1 + 2 + 3 = 6
#   : 8721 => 8 + 7 + 2 + 1 = 18 => 1 + 8 = 9
#   : 245  => 2 + 4 + 5 = 11 **special rule don't collapse

def collapse_number(number):

    while number > 9:
        if number == 11 or number == 22:
            break
        number_str = str(number)
        result = 0
        for n in number_str:
            result = result + int(n)
        number = result

    return number


def collapse_consonants(number):
    while number > 9:
        number_str = str(number)
        result = 0
        for n in number_str:
            result = result + int(n)
        number = result
    return number