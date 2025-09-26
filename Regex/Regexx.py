
# 1. What is Regex?

           # Regex (Regular Expressions) are patterns used to search, match, or replace text.
           
           # In Python, regex is handled with the re module.



# 2. Basic Functions in re
                            
                #    Function	                  Use
                #    
                #    re.match()	      Matches only at the beginning of string
                #    
                #    re.search()	      Finds first occurrence anywhere
                #    
                #    re.findall()	  Returns all matches as a list
                #    
                #    re.finditer()	  Returns iterator with match objects
                #    
                #    re.sub()	      Replace matched text
                #    
                #    re.split()	      Split string by regex pattern


'''

import re                                     # "\d+" this only workd integers valuea

text = "My phone nbr is 123456789"

m = re.search(r"\d+",text)                             #  # \d+ = one or more digits
print(m.group())         # 123456789

m1 = re.search(r"\d+",text)
print(m1)          # <re.Match object; span=(16, 25), match='123456789'>

n = re.findall(r"\d+",text)
print(n)           # ['123456789']

m = re.match(r"My",text)
print(bool(m))            # True


m = re.sub(r"\d+","chenna",text)
print(m)           # My phone nbr is chenna

'''




