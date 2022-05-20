import re

print('Submit a string you would like to reverse:\n')
str = input('> ')

print('\nWould you like to reverse the letters or the words?\n')
inp = input('> ')
print()

words = str.split()

reversed_w = words[::-1]

def reverse_l():
    for w in words:
        reversed_l = ''.join(reversed(w))
        print(reversed_l, sep=' ', end=' ')

if inp == 'words':
    print(' '.join(reversed_w))

elif inp =='letters':
    reverse_l()
