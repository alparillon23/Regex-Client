# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Built-in library supporting regex operations

# NEW: Don't use regex package
# hardcode it with ONLY . and +
# all other special chars in regex are considered at face value (regular characters)
# Only drawback in solution is
# let char be a character: not . or +
# if char+char (same char after char+ is considered, it will return false:
# char+char => char+ in this design)


# we can build the list of all Unicode characters covered in Python using chr
# 32 is the first character that is not an instruction

chars = {}
for i in range(32, 1114111):
    chars[i] = chr(i)


# accepts phrase, position of inspection
# and token
# returns -1 (fail) for multiple reasons
#  - should phrase at this point have no such character
#  - should "++" be a token
# returns the last position where char+ is settled otherwise
def check_plus(phrase, pos, tok):
    f = -1
    ch = tok[0]
    if pos >= len(phrase):
        return f
    if tok[0] == chars[46]:
        ch = phrase[pos]
    if tok[0] == chars[43]:
        return f
    for e in range(pos, len(phrase)):
        if phrase[e] != ch:
            break
        else:
            f = e
    return f


# accepts phrase, position of inspection
# and token
# returns -1 (fail) for multiple reasons
#  - should phrase at this point have no such character
#  - should "+" be a token (we encounter this when + starts the reg_code or "[_+][+]" is encountered)
# returns pos otherwise
def val_check(phrase, pos, tok):
    f = -1
    if pos >= len(phrase):
        return f
    if tok == chars[46]:
        return pos
    if tok == chars[43]:
        return f
    if tok == phrase[pos]:
        return pos
    else:
        return f


# accepts the reg_code provided by the user
# returns a list of tokens for each value
# this allows us to parse the unique members easily
def tokenized(reg):
    tokens = []
    e = 0
    while e < len(reg):
        if e + 1 < len(reg):  # checks for "_+" tokens
            if reg[e + 1] == chars[43]:
                tokens.append(reg[e:e + 2])
                e += 2
            else:
                tokens.append(reg[e])
                e += 1
        else:  # regular tokens (single char)
            tokens.append(reg[e])
            e += 1
    return tokens


# Compares the given input string to a provided reg_ex
# . = 46, + = 43
def reg_exp(phrase, reg_code):
    p = 0
    tokens = tokenized(reg_code)
    for t in tokens:
        if len(t) == 2:  # token with char len == 2 are "char+"
            e = check_plus(phrase, p, t)
        else:
            e = val_check(phrase, p, t)
        if e == -1:
            return False
        else:
            p = e + 1
    return p == len(phrase)


def reg_ex_app():
    phrase = input("Insert your phrase: ")
    reg_code = input("Insert the code to match against: ")
    if reg_exp(phrase, reg_code):
        print("The phrase matches.")
    else:
        print("The phrase does not match.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reg_ex_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
