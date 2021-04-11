# Case-study #7
# Developers: Braer P. (%),
# Kokorina D. (%),
# Novoselov V. (%)
import codecs
text = ''
with codecs.open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if text == '':
                s = ''
            else:
                s = ' '
            if line.find('\r') != -1:
                text += s + line[:line.find('\r')]
            elif line.find('\n') != -1:
                text += s + line[:line.find('\n')]
            else:
                text += s + line
words = text.split(' ')

start_words = []
middle_words = []
finish_words = []

for word in words:
    if word.istitle() == True:
        start_words.append(word)
    elif word[len(word) - 1] == '.':
        finish_words.append(word)
    else:
        middle_words.append(word)

start_words_var = []
for word in start_words:
    if word not in start_words_var:
        start_words_var.append(word)

dict_start_words = {}
words_after = []
position = -1
for word in start_words_var:
    for all_word in words:
        position += 1
        if word == all_word and position != len(words) - 1:
            words_after.append(words[position + 1])
    if word not in dict_start_words:
        dict_start_words[word] = words_after
    position = -1
    words_after = []


import random
i = 0
n = random.randint(3, 18)
print(random.choice(dict_start_words))
while i < n:
    print(random.choice(dict_start_words))
    i = i+1
print(random.choice(dict_start_words))


middle_words_var = []
for word in middle_words:
    if word not in middle_words_var:
        middle_words_var.append(word)

dict_middle_words = {}
words_after_m = []
position_m = -1
for word in middle_words_var:
    for all_word in words:
        position_m += 1
        if word == all_word and position_m != len(words) - 1:
            words_after_m.append(words[position_m + 1])
    if word not in dict_middle_words:
        dict_middle_words[word] = words_after_m
    position_m = -1
    words_after_m = []


import random
n = random.randint(3, 18)
print(random.choice(dict_middle_words))
while i < n:
    print(random.choice(dict_middle_words))
    i = i+1
print(random.choice(dict_middle_words))

finish_words_var = []
for word in finish_words:
    if word not in finish_words_var:
        finish_words_var.append(word)

dict_finish_words = {}
words_after_f = []
position_f = -1
for word in finish_words_var:
    for all_word in words:
        position_f += 1
        if word == all_word and position_f != len(words) - 1:
            words_after_f.append(words[position_f + 1])
    if word not in dict_finish_words:
        dict_finish_words[word] = words_after_f
    position_f = -1
    words_after_f = []
print(dict_finish_words)
