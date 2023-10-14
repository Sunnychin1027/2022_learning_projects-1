"""
File: class_reviews.py
Name: Sunny
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    This program will help calculate the scores from SC001 and SC101,
    also, it will show the maximum, minimum, average score of eah class.
    If there are no score enter either class, it will show 'No score for ---'
    """
    # maximum = -float('inf')
    # minimum = float('inf')
    count0 = 0
    count1 = 0           # count how many times it runs to calculate the average

    while True:
        class0 = input('Which class? ' + str()).upper()
        # set break point if user enter -1 at the very beginning
        if class0 == str('-1') and count0 == 0 and count1 == 0:
            print('No class scores were entered')
            break

        else:
            # Two situation, either class sc001 or sc101, have to calculate it separately
            if class0 == str('SC001'):
                count0 += 1

                # This will be the first time and first value for it to store, sc001
                if count0 == 1:
                    score0 = int(input('Score: '))
                    max_score0 = score0
                    min_score0 = score0
                    total_score0 = score0

                # After the second score enter, it will have the previous score to compare, sc001
                else:
                    score0 = int(input('Score: '))
                    if score0 > max_score0:
                        max_score0 = score0
                    if score0 < min_score0:
                        min_score0 = score0
                    total_score0 += score0

            elif class0 == str('SC101'):
                count1 += 1
                # This will be the first time and first value for it to store, sc101
                if count1 == 1:
                    score0 = int(input('Score: '))
                    max_score1 = score0
                    min_score1 = score0
                    total_score1 = score0

                # After the second score enter, it will have the previous score to compare, sc101
                else:
                    score0 = int(input('Score: '))
                    if score0 > max_score1:
                        max_score1 = score0
                    if score0 < min_score1:
                        min_score1 = score0
                    total_score1 += score0

            # Three kinds of situation that might print out
            elif class0 == '-1' and count0 >= 1 and count1 >= 1:
                print('=============SC001=============')
                print('Max(001): ' + str(max_score0))
                print('Min(001): ' + str(min_score0))
                print('Avg(001): ' + str(total_score0 / count0))
                print('=============SC101=============')
                print('Max(101): ' + str(max_score1))
                print('Min(101): ' + str(min_score1))
                print('Avg(101): ' + str(total_score1 / count1))
                break

            elif class0 == '-1' and count0 == 0 and count1 >= 1:
                print('=============SC001=============')
                print('No score for SC001')
                print('=============SC101=============')
                print('Max(101): ' + str(max_score1))
                print('Min(101): ' + str(min_score1))
                print('Avg(101): ' + str(total_score1 / count1))
                break

            elif class0 == '-1' and count1 == 0 and count0 >= 1:
                print('=============SC001=============')
                print('Max(001): ' + str(max_score0))
                print('Min(001): ' + str(min_score0))
                print('Avg(001): ' + str(total_score0 / count0))
                print('=============SC101=============')
                print('No score for SC101')
                break

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
