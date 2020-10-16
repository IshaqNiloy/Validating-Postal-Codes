regex_integer_in_range = r"[0-9]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=\d\1)"	# Do not delete 'r'.

#(\d): Match and capture a digit in group #1
#(?=: Start lookahead
#\d: Match any digit
#\1: Back-reference to captured group #1
#): End lookahead

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
