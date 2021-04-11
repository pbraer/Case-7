# Case-study #7
# Developers:   Braer P. (70%),
#               Kokorina D. (50%),
#               Novoselov V. (35%)

print("""Case-study Генератор текста
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")

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

middle_words_var = []
for word in middle_words:
    if word not in middle_words_var:
        middle_words_var.append(word)

dict_middle_words = {}
words_after = []
position = -1
for word in middle_words_var:
    for all_word in words:
        position += 1
        if word == all_word and position != len(words) - 1:
            words_after.append(words[position + 1])
    if word not in dict_middle_words:
        dict_middle_words[word] = words_after
    position = -1
    words_after = []

finish_words_var = []
for word in finish_words:
    if word not in finish_words_var:
        finish_words_var.append(word)

dict_finish_words = {}
words_after = []
position = -1
for word in finish_words_var:
    for all_word in words:
        position += 1
        if word == all_word and position != len(words) - 1:
            words_after.append(words[position + 1])
    if word not in dict_finish_words:
        dict_finish_words[word] = words_after
    position = -1
    words_after = []

import random as r


amount_sentence = int(input('Количество генерируемых предложений: '))
amount_sentence += 1
sent = 1

start_len = len(start_words_var)-1
middle_len = len(middle_words_var)
finish_len = len(finish_words_var) - 1

while sent != amount_sentence:
    words_amount = r.randint(2, 18)
    words_amount += 1
    start_word = r.randint(0, start_len)
    start_1 = start_words_var[start_word]
    start_mean = r.randint(0, len(dict_start_words[start_1])-1)
    start_w_2 = dict_start_words[start_1]
    start_2 = start_w_2[start_mean]
    print(start_1 + ' ' + start_2, sep='', end=' ')
    wrd = 1
    st = ' '
    while wrd != words_amount and st[len(st) - 1] != '.':
        middle_word = r.randint(0, middle_len-1)
        middle_1 = middle_words_var[middle_word]
        middle_w_2 = dict_middle_words[middle_1]
        middle_mean = r.randint(0, len(middle_w_2)-1)
        middle_2 = middle_w_2[middle_mean]
        st += middle_1.lower() + ' ' + middle_2.lower() + ' '
        wrd += 1

    st = st[1:len(st)-1]
    if st[len(st) - 1] == ' ':
        st = st[:len(st)-1]
    if st[len(st) - 1] == ',':
        st = st[:len(st)-1]
    print(st, sep='', end='. ')

    sent += 1


