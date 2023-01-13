# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)


def URLify(phrase, true_length):
    phrase = list(phrase)
    space_count = 0
    # for i in range(0, true_length):
    #     if phrase[i] == ' ':
    #         space_count += 1

    index = len(phrase)
    for i in range(true_length-1, 0, -1):
        if (phrase[i] ==  ' '):
            phrase[index - 1] = '0'
            phrase[index - 2] = '2'
            phrase[index - 3] = '%'
            index = index - 3
        else:
            phrase[index-1] = phrase[i]
            index = index - 1

    return ''.join(phrase)


assert URLify("Mr John Smith    ", 13) == "Mr%20John%20Smith"

assert URLify("Mr John  ",7) == "Mr%20John"



