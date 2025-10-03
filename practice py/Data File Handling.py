# METHOD 1: USING close() method.
f = open('text.txt' , 'w')
print(f.write('this is a text file.'))
f.close()

# method 2: use --> with --> automatically without close method file closed.
with open('text.txt' , 'w') as f:
    print(f.write('this is text file..')) #override

# using --> append --> denoted --> 'a'
with open('text.txt' , 'a') as f:
    print(f.write('new line add using --> append concept'))

# using --> append --> denoted --> 'a' 
# & using escape character like --> \n
with open('text.txt' , 'a') as f:
    print(f.write('\nnext line text generated using --> escape character like (back slash n)..'))

# read file using 'r' , read() method..
with open('text.txt' , 'r') as f:
    file_content = f.read()
    print(file_content)
