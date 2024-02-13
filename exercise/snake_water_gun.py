# create 1d list
# NAIVE WAY
# N = 5
# arr = [0]*N
# print(arr)

# # COMPREHENSION WAY
# N = 5
# arr = [0 for i in range(N)]
# print(arr)

# # create 2d list
# # NAIVE WAY
# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# print(arr)

# COMPREHENSION WAY
# rows, cols = (5, 5)
# arr = [[0 for i in range(cols)] for j in range(rows)]
# print(arr, "\n")

# arr[0][1] = 1
# # print(arr)
# for row in arr:
#     print(row)

# excercise (snake, water and gun)
import random as rand
R, C = (3,3)
array = [[0 for i in range(C)] for j in range(R)]
# print(array)
array[0][1] = 1
array[0][2] = -1
array[1][0] = -1
array[1][2] = 1
array[2][0] = 1 
array[2][1] = -1
# for row in array:
#     print(row)
while(True):

    user = int(input('\nenter any number:\n1) 0 for snake\n2) 1 for water\n3) 2 for gun\n4) 3 for exit\n'))

# error handling
    if(user<0 or user>3):
        raise ValueError('INVALID INPUT')

    if(user == 0):
        print('You choose Snake')
    elif(user == 1):
        print('You choose Water')
    elif(user == 2):
        print('You choose Gun')
    elif(user == 3):
        break


# generating random input between 0 to 2
    computer = rand.randint(0, 2)

    if(computer == 0):
        print('Computer choose Snake\n')
    elif(computer == 1):
        print('Computer choose Water\n')
    else:
        print('Computer choose Gun\n')

    if(array[user][computer] == 0):
        print('This match has been draw')
    elif(array[user][computer] == -1):
        print('You Lost')
    else:
        print('You Won')





