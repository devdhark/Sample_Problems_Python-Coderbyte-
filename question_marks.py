# Have the function QuestionsMarks(str) take the str string parameter,
# which will contain single digit numbers, letters, and question marks,
# and check if there are exactly 3 question marks between every pair of
# two numbers that add up to 10. If so, then your program should return
# the string true, otherwise it should return the string false.
# If there aren't any two numbers that add up to 10 in the string,
# then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program
# should return true because there are exactly 3 question marks between
# 6 and 4, and 3 question marks between 5 and 5 at the end of the string.


def QuestionsMarks(str):
    # code goes here
    # remain false if no numbers are found
    condition = "false"
    for i, c in enumerate(str):
        if c.isdigit():
            # find next number of out remaining string
            for j, d in enumerate(str[i+1:]):
                # check the sum
                if d.isdigit() and int(c)+int(d) == 10:
                    # slice the characters in between into a substring
                    sl = str[i+1:i+1+j]
                    # check for exactly 3 ?
                    if [e == "?" for e in sl].count(True) == 3:
                        condition = "true"
                    else:
                        # only return true if ALL (c+d=10) agrees with the condition otherwise false
                        condition = "false"

    return condition


# keep this function call here
print(QuestionsMarks("arrb6???4xxbl5???eee5"))
