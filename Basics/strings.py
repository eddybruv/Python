# a string is created by enclosing text in quotes

# a string can also be created using the str() function
number = str(9.89)

# triple quotes are used to enclose multiline strings
poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When tho door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway;
'''

# strings can be combined using +
# string literals can be combined by just putting them together
print('I am ' 'Eddy')

# getting a substring from a string using slice
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[20:])
print(letters[19::4])
print(letters[:21:5])  # start skip 5 and end at 21

# we can reverse a string by using this shortcut
print("In revers order: ", letters[-1::-1])

# we can use the functions split and join to create arrays and strings respect
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(' '))

# we can clear white spaces using strip() function
# we can get the length of a variable using len() fx
print("The length of tasks is: ", len(tasks))

# USEFUL FUNCTIONS
# .startswith() and .endswith()
# .capitalize() .title()
# .upper() .lower()

# OLD style
print('{} {}'.format(tasks, letters))

# ASSIGNMENT
# 5.1 Capitalize the word starting with m:
song = '''When an ell grabs your arm,
And it causes great harm,
That's - a moray!
'''
song_arr = song.split(' ')

for word in song_arr:
    if word.startswith('m'):
        word = word.capitalize()
    song_arr += word

song_arr = ' '.join(song_arr)
print(song_arr)
