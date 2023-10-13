def generate_squares():
    sq= []
    for i in range(1,6):
        sq.append(i*i)
    return sq


sq_list= generate_squares()
#print(sq_list)

def genarate_square_genrator(n):
    yield n*n

for i in range(1,10):
    print(next(genarate_square_genrator(i)))
