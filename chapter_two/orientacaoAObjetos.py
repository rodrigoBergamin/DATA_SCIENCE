import string 

class Person(object): #criando uma classe

    def set_name(self, name): #parametro self se refere ao próprio objeto
        if len(name) >= 2:
            self.name = name


class CapitalizedPerson(Person):
    def set_name(self, name):
        if name[0] in string.ascii_uppercase:
            Person.set_name(self, name)


womanCapitalized = CapitalizedPerson()
womanCapitalized.set_name('Ju')
print(womanCapitalized.name)


#exemplo do livro
#simulando um conjunto Set, através da criação de uma classe Set

class Set:
    def __init__(self, values = None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)
    
    def __repr__(self):
        return "Set: " + str(self.dict.keys())
    
    def add(self, value):
        self.dict[value] = True
    
    def contains(self, value):
        return value in self.dict
    
    def remove(self, value):
        del self.dict[value]


s = Set([1,2,3])
s.add(4)
print(s.contains(4))
print(s)