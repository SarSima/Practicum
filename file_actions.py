file = open('example.txt','w', encoding='utf-8')
file.write('Зевну, укроюсь с головою,\nбудильник заведу на март.\n')
file.close()

file = open('example.txt','r')
content = file.read(12)
print(content.encode('utf-8'))
file.close()
