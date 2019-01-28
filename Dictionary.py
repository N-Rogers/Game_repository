#DICTIONARIES IN PYTHON
#commonly known as key value pairs

my_details = {'id':1, 'name':'Rogers', 'Age':25,
'Nationality': 'Ugandan'}

#printing out elements in a python dictionary
print(my_details)

'''
Accessing single elements in a dictionary
We can always access values of given keys
'''

print(my_details['id'])
print(my_details['name'])  #etc

#We cna also add new items to an already eisting dictionary
my_details['Passion'] = 'Being a siftware Developer'
print(my_details)

#looping over elements in a dictionary

for x, y in my_details.items():
    print(x,":",y)

