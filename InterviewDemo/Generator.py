def gen(num):
    a,b = 0,1
    for i in range(0,num):
        yield "{}:{}".format(i+1,a)
        a,b = b, a+b

for x in gen(10):
    print x