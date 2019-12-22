from constants_numerology import vowel_meanings, vowels, consonant_meanings, consonants, alphabet_meanings, alphabet, welcome
from helpers_numerology import *

def greeting():
    print(welcome)
    print()

    
def numerology():

    first_name = get_name("First")
    middle_name = get_name("Middle")
    last_name = get_name("Last")
    print()

    print(f"Hi, {first_name}! We are calculating your special numbers...")
    print()

    first_name = first_name.replace(" ", "").lower()
    middle_name = middle_name.replace(" ", "").lower()
    last_name = last_name.replace(" ", "").lower()


    # Below code calculates 'Stimulus number' => a number based on the vowels of their full name. Calculates separately to avoid edge case.

    vowels_first = sum_found_char_in_dict(first_name, vowels)
    sum_first = collapse_number(vowels_first)

    vowels_middle = sum_found_char_in_dict(middle_name, vowels)
    sum_middle = collapse_number(vowels_middle)

    vowels_last = sum_found_char_in_dict(last_name, vowels)
    sum_last = collapse_number(vowels_last)

    vowels_sum = sum_first + sum_middle + sum_last
    total_vowels = collapse_number(vowels_sum)
    
    if total_vowels == 0:
        print("Unsupported name. Please, try again.")
        return 
    
    print("Your Stimulus Number is:  ")
    print()
    print(str(total_vowels), vowel_meanings[total_vowels])
    

    # Below code calculcates 'Presentation number' => a number based on the consonants of their full name. Calculates separately to avoid edge case.
    
    consonants_first = sum_found_char_in_dict(first_name, consonants)
    sum_first = collapse_consonants(consonants_first)

    consonants_middle = sum_found_char_in_dict(middle_name, consonants)
    sum_middle = collapse_consonants(consonants_middle)

    consonants_last = sum_found_char_in_dict(last_name, consonants)
    sum_last = collapse_consonants(consonants_last)

    consonants_sum = sum_first + sum_middle + sum_last
    total_consonants = collapse_consonants(consonants_sum)

    if total_consonants == 0:
        print("Unsupported name. Please, try again.")
        return 
        
    print("Your Presentation Number is:  ")
    print()
    print(str(total_consonants), consonant_meanings[total_consonants])


    # Below code calculates 'Social number' => a number based on all the letter of their full name. Calculates separately to avoid edge case.
    
    letters_first = sum_found_char_in_dict(first_name, alphabet)
    sum_first = collapse_number(letters_first)

    letters_middle = sum_found_char_in_dict(middle_name, alphabet)
    sum_middle = collapse_number(letters_middle)

    letters_last = sum_found_char_in_dict(last_name, alphabet)
    sum_last = collapse_number(letters_last)

    letters_sum = sum_first + sum_middle + sum_last
    total_letters = collapse_number(letters_sum)
    
    print("Your social number is:  ")
    print()
    print(str(total_letters), alphabet_meanings[total_letters])


def ask_to_calculate_again():
    print("Would you like to calculate another name?")
    print()

    play_again = input("Type Yes to try again: ").title()

    print()
    if play_again.startswith("Y"):
        return True

    print("""Thank you for using the Quantum Calculator. Bye!""")
    print()
    return False

# Loop through numerology until user quit

def calculate_again():
        
    calculating = ask_to_calculate_again()

    while calculating:
        if calculating == False:
            break
        print("Let's calculate another name!")
        print()
        numerology()

        calculating = ask_to_calculate_again()

def run_numerology():

    greeting()
    print()
    numerology()
    print()
    calculate_again()
    
