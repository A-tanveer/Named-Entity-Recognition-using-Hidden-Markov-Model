f = open('one.txt', encoding='utf8')

data = f.read()
f.close()
data = data.replace(':', '').replace(',', '')

f = open('one.txt', 'w', encoding='utf8')

f.write(data)
f.close()


