
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.



#  1) What is JSON?
#  
#  JSON = JavaScript Object Notation.
#  
#  It’s a text format (a string) for exchanging structured data (objects/arrays).
#  
#  Humans and machines both can read it. Widely used in APIs.



#  2) JSON syntax (must-follow)
#  
#  Objects use curly braces {} and string keys with double quotes: {"name": "Alice"}.
#  
#  Arrays use square brackets []: ["apple","banana"].
#  
#  Values: string (double quotes), number, true/false, null, object, array.
#  
#  Important: JSON requires double quotes for keys/strings — single quotes ' are invalid JSON.


#  3) JSON ↔ Python type mapping (cheat sheet)
#     JSON	       Python
#     object {}	    dict
#     array []	    list
#     string	    str
#     number	    int / float
#     true/false	True / False
#     null	None



import json

x = {
    "name": ["chenna", "kesava", "reddy"],
    "age": [11, 22, 33],
    "coding": ["python", "c++", "java"],
    "address": {
        "state": "telangana",
        "pincode": 1234
    }
}

y = json.dumps(x)   # ✅ convert to JSON string
print(y)                                     # {"name": ["chenna", "kesava", "reddy"], "age": [11, 22, 33], "coding": ["python", "c++", "java"], "address": {"state": "telangana", "pincode": 1234}}

print(x["age"][1])      # 22

print(x["name"])        # ['chenna', 'kesava', 'reddy']

print(x["name"][1])     # kesava

print(x["address"]["pincode"])       # 1234

print(sum(x["age"]))             # 66

print(json.dumps(x, indent = 2, sort_keys = True))


# {
#   "address": {
#     "pincode": 1234,
#     "state": "telangana"
#   },
#   "age": [
#     11,
#     22,
#     33
#   ],
#   "coding": [
#     "python",
#     "c++",
#     "java"
#   ],
#   "name": [
#     "chenna",
#     "kesava",
#     "reddy"
#   ]
# }


print(type("name"))       # <class 'str'>