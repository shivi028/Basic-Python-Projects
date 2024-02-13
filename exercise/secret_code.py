# utiliy functions
def count_len(message):
    count = 0
    for i in message:
        count += 1
    return count

def reverse_string(message):
    count = 1
    for i in message[-1]:
        # print(i)
        count -= 1
        return(i,message[count])

# ENCRYPTING MESSAGE
# taking input
message = input('enter the message to encrypt\n')
# message = shivi
# length_message = count_len(message)
length_message = len(message)
# print(length_message)
# print(message)

if(length_message < 3):
    reverse_str = reverse_string(message)
else:
    poped = message[0]
    manipulate_str = message.replace(message[0], "")
    # print(poped)
    manipulate_str = "nar" + manipulate_str + poped + 'ari'

# printing final encrypted message
a = int(input('press 1 to check your encrypred message : '))
if(a == 1):
    if(length_message < 3):
        print(f'your encypted message is here : {reverse_str}')
    else:
        print(f'your encypted message is here : {manipulate_str}')
else:
    raise ValueError('INVALID INPUT')

# DECRYPTING MESSAGE
secret_code = 101
key_value = int(input('enter the secret code to see the decrypted message : '))
if(secret_code == key_value):
    if(length_message < 3):
        reverse_str = reverse_string(reverse_str)
        print(reverse_str)
    else:
        x = manipulate_str[0 : 3]
        y = manipulate_str[-3 : ]
        manipulate_str = manipulate_str.replace(x, "")
        manipulate_str = manipulate_str.replace(y, "")
        # print(manipulate_str)
        pop = manipulate_str[-1]
        # print(pop)
        manipulate_str = pop + manipulate_str[:-1]
        print(manipulate_str)

    


