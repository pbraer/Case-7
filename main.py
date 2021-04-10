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
print(dict_start_words)

finish_words_var = []


dict_middle_words = {}
dict_finish_words = {}

