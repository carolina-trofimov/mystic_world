from numerology import run_numerology
from horoscope import run_horoscope

print("""Welcome to the Mystic World!

In this program you have a choice to see your Numerology number and what it means about you or you can get some advice for your daily Horoscope""")

def mystic_world():
    while True:
        print()
        print("""What would you like to do?

a - Numerology
b - Horoscope
c - Quit

Type a, b or c:""")
        print()

        user_choice = input("> ").lower()

        if user_choice == "a":
            print()
            run_numerology()
        
        elif user_choice == "b":
            print()
            run_horoscope()
            
        elif user_choice == "c":
            print("Thank you for using the Mystic World. Bye!")
            break
        else:
            print("This is not a valid option")


mystic_world()