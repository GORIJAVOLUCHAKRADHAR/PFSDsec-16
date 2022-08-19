'''Parse JSON - Convert from JSON to Python
 If you have a JSON string, you can parse it by using the json.loads() method.'''
import json  #json means java script object notation
# some JSON:
x ='{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)
print(y["name"])
print(y["age"])
print(y["city"])


'''Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.'''

import json
# a Python object (dict):
x = {"name": "John", "age": 30,"city": "New York"}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
