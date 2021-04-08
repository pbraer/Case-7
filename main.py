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
print(words)

words_2 = []
for word in words:
    if word not in words_2:
        words_2.append(word)
print(words_2)