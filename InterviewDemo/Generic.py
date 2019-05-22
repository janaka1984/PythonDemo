#list
list = [1,2,3,4]
for i in list:
    print i

print [i*i for i in list]
print "------------"
#tuple
tuple = (1,2,3,4)
for i in tuple:
    print i
print "------------"
#dictionary
dict = {"a":1,"b":2,"c":3}
for key,val in dict.iteritems():
    print "key {} val {}".format(key,val)
print "------------"
#set
set = {1,2,3}
for i in set:
    print i

