def read_text_genrator(filename, comment_char='#'):
    with open(filename,'r') as file:
        for line in file:
            if not line.startswith(comment_char):
                yield line.strip()

text_gen = read_text_genrator('sample.txt')

for i in range(5):
    print(next(text_gen))
