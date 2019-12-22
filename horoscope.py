import requests
import json
from datetime import datetime
import re


JANUARY_20 = datetime(2019, 1, 20)
FEBRUARY_19 = datetime(2019, 2, 19)
MARCH_21 = datetime(2019, 3, 21)
APRIL_20 = datetime(2019, 4, 20)
MAY_21 = datetime(2019, 5, 21)
JUNE_21 = datetime(2019, 6, 21)
JULY_23 = datetime(2019, 7, 23)
AUGUST_23 = datetime(2019, 8, 23)
SEPTEMBER_23 = datetime(2019, 9, 23)
OCTOBER_23 = datetime(2019, 10, 23)
NOVEMBER_22 = datetime(2019, 11, 22)
DECEMBER_22 = datetime(2019, 12, 22)


def welcome():
    welcome = """Welcome to the Daily Horoscope.
This program gives you important advices to help you to deal better with your day."""
    print(welcome)
    print()

def request_get(url):
  return requests.get(url)


def convert_strToJson(data):
  return json.loads(data)


def get_birthday():
    while True:
        request_birthday = input("""What is your birthday?
(Use the format mm-dd)
> """)
        print()
        bday_search = re.search(r'^\d\d-\d\d$', request_birthday)

        # Is there a match?
        if (bday_search):
            bday_input = bday_search.group() + '-2019'
            # Is the match a valid date?
            if (validate_date(bday_input)):
                return bday_input
            else:
                print("Date is invalid, please try again.")
                print()
        else: 
            print ("use format mm-dd")
            print()
        
            
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False

def convert_str_to_date(date_str):
    return datetime.strptime(date_str, "%m-%d-%Y")


def get_sign(birthday):

    if JANUARY_20 <= birthday < FEBRUARY_19:
        return "aquarius"
    if FEBRUARY_19 <= birthday < MARCH_21:
        return "pisces"
    if MARCH_21 <= birthday < APRIL_20:
        return "aries"
    if APRIL_20 <= birthday < MAY_21:
        return "taurus"
    if MAY_21 <= birthday < JUNE_21:
        return "gemini"
    if JUNE_21 <= birthday < JULY_23:
        return "cancer"
    if JULY_23 <= birthday < AUGUST_23:
        return "leo"
    if AUGUST_23 <= birthday < SEPTEMBER_23:
        return "virgo"
    if SEPTEMBER_23 <= birthday < OCTOBER_23:
        return "libra"
    if OCTOBER_23 <= birthday < NOVEMBER_22:
        return "scorpio"
    if NOVEMBER_22 <= birthday < DECEMBER_22:
        return "sagittarius"
    else:
        return "capricorn"

def get_url(sign):
    url = f"http://ohmanda.com/api/horoscope/{sign}/"
    return url


def get_horoscope(json_horoscope):
    return json_horoscope["horoscope"]
    
def horoscope():
    birthday_date = get_birthday()
    date = convert_str_to_date(birthday_date)
    sign = get_sign(date)
    url = get_url(sign)
    response = request_get(url).text
    converted_json = convert_strToJson(response)
    horoscope = get_horoscope(converted_json) 

    print(f"""{sign.title()} -{horoscope}""")

def ask_to_calculate_again():
    print("Would you like to read another horoscope??")
    print()

    play_again = input("Type Yes to try again: ")
    play_again = play_again.title()
    print()
    if play_again.startswith("Y"):
        return True

    print("""Thank you for using the Daily Horoscope. Bye!""")
    print()
    return False

# Loop through numerology until user quit

def calculate_again():
        
    calculating = ask_to_calculate_again()

    while calculating:
        if calculating == False:
            break
        print("Let's calculate another horoscope")
        print()
        horoscope()

        calculating = ask_to_calculate_again()


def run_horoscope():
    welcome()
    print()
    horoscope()
    print()
    calculate_again()
