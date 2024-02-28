#This functon converts a number to a word, in dholuo 
#Goes from 0 to 99
# TODO Extend to 999

def numbers_to_words(number):

    onesAndTens = ["achiel", "ariyo", "adek", "ang'wen", "abich", "auchiel", "abiriyo", "aboro", "ochiko", "apar", "apar gachiel",
                 "apar gariyo", "apar gadek", "apar gang'wen", "apar gabich", "apar gauchiel", "apar gabiriyo", "apar  gaboro", "apar gochiko"]
    prefixes = [ "gachiel", "gariyo", "gadek", "gang'wen", "gabich", "gauchiel", "gabiriyo", "gaboro", "gochiko"]

    if 0 < number > 1000  :
        return "Number out of range"

    elif number == 0:
        return "sufuri"

    elif number < 20:
        return onesAndTens[number - 1]
    elif 20 <= number < 100:
        return "piero " + onesAndTens[number // 10 -1] +  " " + prefixes[number % 10 -1]

print(numbers_to_words(100))
