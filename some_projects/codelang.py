import random
import string

print('-'*15, "MENU", '-'*15)
print("1.Code")
print("2.Decode")

while True:
    try:
        entry = int(input("What you wanna do? (1,2)\n"))
        if entry in [1,2]:
            match entry:
                case 1:
                    print("----You have selected to code----")
                    code = input("Enter your string:\n")
                    if len(code)<3:
                        print("".join(reversed(code)))
                    elif len(code)>=3:
                        random_letters1 = ''.join(random.choices(string.ascii_letters, k=3))
                        random_letters2 = ''.join(random.choices(string.ascii_letters, k=3))
                        new_str = random_letters1 + code[3:] + code[2] + code[1] + code[0] + random_letters2
                        print(new_str)
                    break
                case 2:
                    print("----You have selected to decode----")
                    decode = input("Enter your string:\n")
                    if len(decode)<3:
                        print("".join(reversed(decode)))
                    # elif len(decode)==4:
                    #     new_str = decode[-4] + decode[-5] + decode[-6] + decode[3] - decode[:2] - decode[-3:-1]
                    #     print(new_str)
                    elif len(decode)>=3:
                        new_str = decode[-4] + decode[-5] + decode[-6] + decode[3:-6]
                        print(new_str)
                    break
    except:
        print("Enter a valid input")





                    
        
