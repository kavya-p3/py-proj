import collections

# Declaring namedtuple() 
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values 
S = Student('Nandini', '19', '2541997')

# initializing iterable  
li = ['Manjeet', '19', '411997']

# initializing dict 
di = {'age': 19, 'DOB': 1391997,'name': "Nikhil"}

'''# using _make() to return namedtuple() 
print("The namedtuple instance using iterable is  : ")
k = Student._make(li)
t = dict(k._asdict())
print(dict(t))
print(type(t))'''

# using _asdict() to return an OrderedDict()
#print("The OrderedDict instance using namedtuple is  : ")
#print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(di)
print(Student(**di))