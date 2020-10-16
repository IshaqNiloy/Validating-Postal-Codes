regex_integer_in_range = r"[0-9]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
