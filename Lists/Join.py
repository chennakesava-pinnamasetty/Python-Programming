
# JOIN LISTS

# 1.Using + operators
list1 = ["apple","banana","cherry"]
list2 = ["mango","pineapple","papaya"]
list3 = list1+list2
print(list3)        # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# 2. EXTEND()
list1 = ["apple","banana","cherry"]
list2 = ["mango","pineapple","cherry"]
list1.extend(list2)
print(list1)      # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'cherry']


# 3. USING A LOOP
list1 = ["apple","banana","cherry"]
list2 = ["mango","pinapple","papaya"]
for item in list2:
    list1.append(item)
    print(list1)            # ['apple', 'banana', 'cherry', 'mango']
                            # ['apple', 'banana', 'cherry', 'mango', 'pinapple']
                            # ['apple', 'banana', 'cherry', 'mango', 'pinapple', 'papaya']


# 4. LIST COMPREHENSION
list1 = ["apple","banana","cherry"]
list2 = ["mango","pineapple","papaya"]
list3 = [item for item in list1]+[item for item in list2]
print(list3)              # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
