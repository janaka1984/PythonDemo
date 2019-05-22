class Person(object):
    def __init__(self,name):
        self.name = name

    def read(self):
        print 'my name is {}'.format(self.name)

class BlackPerson(Person):
    def __init__(self,name, surname):
        super(BlackPerson, self).__init__(name)
        self.surname = surname

    def read(self):
        super(BlackPerson,self).read()
        print ' and surname is {}'.format(self.surname)

# janaka = Person("janaka")
# janaka.read()

janaka = BlackPerson("janaka","weerarathna")
janaka.read()