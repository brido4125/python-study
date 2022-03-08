cipher_text = "RVJZJSRJVUFERUVJZXEGIZETZGCVBEFNERJRJLSJKZKLKZFEGVIDLKRKZFEEVKNFIBREUZJVWWZTZVEKZESFKYJFWKNRIVREUYRIUNRIV"


# Using ASCII to convert char to int
def get_key_value_by_e(ch):
    return ord(ch) - ord('E')


def char_to_int(ch):
    return ord(ch) - 65


def int_to_char(num):
    return chr(num)


def decryption(key):
    plain_text = " "
    key = get_key_value_by_e(key)

    for i in range(len(cipher_text)):
        before = (char_to_int(cipher_text[i]) - key) % 26
        plain_text = plain_text + int_to_char(before + 65 + 32)

    return plain_text


# R,Z,V,J,K by Counter
print(decryption("R"))
print(decryption("Z"))
print("Meaningful Sentence :" + decryption("V"))  # "V" has meaningful sentence
print(decryption("J"))
print(decryption("K"))
