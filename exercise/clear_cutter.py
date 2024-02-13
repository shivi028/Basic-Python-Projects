import os
files = os.listdir('exercise')
i = 1
for file in files:
    if file.endswith('.png'):
        print(file)
        os.rename(f'exercise/{file}', f'exercise/{i}.png')
        i += 1

# files = os.listdir('exercise')
# i = 101
# for file in files:
#     if file.endswith('.jpg'):
#         print(file)
#         os.rename(f'exercise/{file}', f'exercise/{i}.jpg')
#         i += 1

files = os.listdir('exercise')
i = 101
for file in files:
    if file.endswith('.jpg'):
        print(file)
        os.rename(f'exercise/{file}', f'exercise/{i}.png')
        i += 1