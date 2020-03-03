# Using the Python language, have the function SwapII(str)
# take the str parameter and swap the case of each character.
# Then, if a letter is between two numbers (without separation),
# switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3"
# the output should be 4hELLO6 -8wORLD, 7 YES3.


def SwapII(str):
    # code goes here
    # first swap characters of all the characters in the string
    # and store them in a list
    str = list(str.swapcase())
    for i, c in enumerate(str):
        if c.isdigit():
            # iterate through the remaining characters to find number pair(c,d)
            for j, d in enumerate(str[i+1:]):
                if d.isdigit():
                    # create substring where we can check our conditions
                    temp = "".join(str[i+1: i+1+j])
                    # swap if all characeter are non-space AND at least one character is an alphabet
                    if all([not e.isspace() for e in temp]) and any([f.isalpha() for f in temp]):
                        str[i], str[i+1+j] = str[i+1+j], str[i]
    str = "".join(str)
    return str


# keep this function call here
print(SwapII("dd3s---j5  f6-h4n5 d-3 -a2s"))
