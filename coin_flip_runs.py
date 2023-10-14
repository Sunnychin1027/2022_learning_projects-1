"""
File: coin_flip_runs.py
Name: Sunny
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program will let user enter an int, it will
	randomly shows head(H) or tail(T), if there are continuous H or T
	it will count 1 time(1 run), the program will stop once it have successfully
	finish the number of runs.
	"""
	print("Let's flip a coin!")
	num = int(input('Number of runs: '))
	count = 0
	is_in_a_row = False
	aroll = r.choice('TH')
	outcome = str(aroll + '')
	while True:
		if num == count:
			break
		else:
			broll = r.choice('TH')
			outcome += str(broll)
			if aroll == broll:
				if not is_in_a_row:
					count += 1
					is_in_a_row = True
				else:
					pass
			else:
				is_in_a_row = False
			aroll = broll
	print(outcome)

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
