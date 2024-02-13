count = 0
question1 = ['what is the capital of India?', '1) delhi', '2) bhopal', '3) goa', '4) pune']

question2 = ['What Indian mom wants from there child?', '1) to stay at home', '2) fill refrigerator bottle', '3) to study', '4) to go temple']

question3 = ['who is the master of naruto?', '1) jeraya sensie', '2) kakashi', '3)tsunate', '4) all of the above']

question4 = ['which app is the best to use?', '1) youtube', '2) whatsapp', '3) snapchat', '4) Instagram']

correctans = [question1[1], question2[1], question3[4], question4[1]]
answers = []

for i in question1:
    print(i)

a1 = int(input('enter the correct option number\n'))
if(a1 == 1):
    answers.append(question1[1])
elif(a1 == 2):
    answers.append(question1[2])
elif(a1 == 3):
    answers.append(question1[3])
else:
    answers.append(question1[4])

print('for question 1 you have enter : ', answers[0])

if(answers[0] == correctans[0]):
    print('CORRECTR ANSWER, WON $100\n')
    count = count + 1
else:
    print('WRONG ANSWER!!:(\n')

for i in question2:
    print(i)

a2 = int(input('enter the correct option number\n'))
if(a2 == 1):
    answers.append(question2[1])
elif(a2 == 2):
    answers.append(question2[2])
elif(a2 == 3):
    answers.append(question2[3])
else:
    answers.append(question2[4])

print('for question 2 you have enter : ', answers[1])

if(answers[1] == correctans[1]):
    print('CORRECTR ANSWER, WON $100\n')
    count = count + 1
else:
    print('WRONG ANSWER!!:(\n')

for i in question3:
    print(i)

a3 = int(input('enter the correct option number\n'))
if(a3 == 1):
    answers.append(question3[1])
elif(a3 == 2):
    answers.append(question3[2])
elif(a3 == 3):
    answers.append(question3[3])
else:
    answers.append(question3[4])

print('for question 3 you have enter : ', answers[2])

if(answers[2] == correctans[2]):
    print('CORRECTR ANSWER, WON $100\n')
    count = count + 1
else:
    print('WRONG ANSWER!!:(\n')


for i in question4:
    print(i)

a4 = int(input('enter the correct option number\n'))
if(a4 == 1):
    answers.append(question4[1])
elif(a4 == 2):
    answers.append(question4[2])
elif(a4 == 3):
    answers.append(question4[3])
else:
    answers.append(question4[4])

print('for question 2 you have enter : ', answers[3])

if(answers[3] == correctans[3]):
    print('CORRECTR ANSWER, WON $100\n')
    count = count + 1
else:
    print('WRONG ANSWER!!:(\n')

if(count == 0):
    print('you have entered all wrong answers')
elif(count == 1):
    print('you won $100')
elif(count == 2):
    print('you won $200')
elif(count == 3):
    print('you won $300')
elif(count == 4):
    print('you won $400')


