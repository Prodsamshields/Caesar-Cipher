print("Welcome to Caesar Cipher solver")
def encryption():
    cipher = input("Input your text: ").upper()
    key = int(input("Input your shift key: "))
    num_list = []
    for n in cipher:
        num_list.append(ord(n))
    sumkey = int(key)
    encode = []
    for char in num_list:
        if char in range(0, 64):
            encode.append(32)
            continue
        else:
            char += sumkey
            encode.append(char)
    encoded = []
    for char in encode:
        if char in range(91, 96):
            char = char - 26
            encoded.append(chr(char))
            continue
        elif char > 90:
            char = char - 26
            encoded.append(chr(char))
        else:
            encoded.append(chr(char))
    fulle = ''.join(encoded).upper()
    print("Your text encoded is: ", fulle)
def decryption():
    cipher = input("Input your text: ").upper()
    key = int(input("Input your shift key: "))
    num_list = []
    for n in cipher:
        num_list.append(ord(n))
    sumkey = int(key)
    decode = []
    for char in num_list:
        if char in range(0, 64):
            decode.append(32)
            continue
        else:
            char -= sumkey
            decode.append(char)
    decoded = []
    for char in decode:
        if char in range(91, 96):
            char += 26
            decoded.append(chr(char))
            continue
        elif char > 90:
            char += 26
            decoded.append(chr(char))
            continue
        elif char < 65 and char != 32:
            char += 26
            decoded.append(chr(char))
            continue
        else:
            decoded.append(chr(char))
    fulle = ''.join(decoded).lower()
    print("Your text decoded is:", fulle)
question = input("Select (D)ecryption or (E)ncryption to get started: ").title()
if question == "D":
    decryption()
elif question == "E":
    encryption()
else:
    print("Input is not compatible.")
    question = False
while question == False:
    ques1 = input("Would you like to try again? (Yes/No): ").title()
    if ques1 == "Yes":
        question = input("Select (D)ecryption or (E)ncryption to get started: ").title()
        if question == "D":
            decryption()
        elif question == "E":
            encryption()
        else:
            print("Sorry, your input is not compatible.")
            question = False
    elif ques1 == "No":
        print("Ok. Goodbye.")
        break
    else:
        break
