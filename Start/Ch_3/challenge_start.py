# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

length = len(test_str)
digits = len([s for s in test_str if s.isdigit()])
punctuation = len([s for s in test_str if s in string.punctuation])
unique_letters = "".join({s for s in test_str if s in string.ascii_letters})

# print the data
str_data = {
    "Length": length,
    "Digits": digits,
    "Punctuation": punctuation,
    "Unique Letters": unique_letters,
    "Unique Count": len(unique_letters),
}
pprint.pp(str_data)
