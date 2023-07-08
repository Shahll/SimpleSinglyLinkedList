## Project Scope

This project serves as an exploration of the sllist topic and is not intended for global use.
## Package Functionality

The package I have developed is specifically designed for handling integer data. It does not support other data types, and therefore, no tests have been conducted using non-numeric data. If you encounter errors while using non-numeric values, please note that such behavior is expected.
## Functionality and Testing

The package offers a variety of functions that may cater to your needs, along with corresponding tests to help identify any errors. If you intend to modify any of the functions, it is advisable to test their functionality to ensure their effectiveness.
## Documentation and Code Comments

Detailed documentation for each function can be found in the index.py file. This documentation provides a clear understanding of each function's purpose, parameter types, input requirements, return values, and data types of the output. Additionally, the code includes brief comments alongside each function, describing its functionality and usage.


## Installation

### You can install the package using `pip`:
```shell
pip install SimpleSinglyLinkedList
```

###  Make sure you have upgraded version of pip:
Windows
```shell
py -m pip install --upgrade pip
```
Linux/MAC OS
```shell
python3 -m pip install --upgrade pip
```

## If you want to use tests in my package you need to install pytest:
```shell
pip install pytest
```



## How to use functions:


## 1. Append, AppendAfter, AppendBefore

## 1.1 append(item)
Adds the item to the end of the list
```shell
l = LinkedList() # Creating a LinkedList 
l.append(1) -> [1]
l.append(2) -> [1, 2]
```

## 1.2 append_after(value, item)
Adds the item after the value 
```shell
l = LinkedList() 
l.append(2) -> [2]
l.append_after(2,3) -> [2, 3]
# "2" is value after which we add item "3" 
# if the value was not found, raises ValuerError
```

## 1.3 append_before(value, item)
Adds the item before the value 
```shell
l = LinkedList() 
l.append(2) -> [2]
l.append_before(2,1) -> [1, 2]
# "2" is value before which we add item "1" 
# if the value was not found, raises ValuerError
```


## 2. Prepend and Insert

## 2.1 prepend(item)
Adds item at the beginning of the list
```shell
l = LinkedList() 
l.append(2) -> [2]
l.prepend(1) -> [1, 2]
```

## 2.2 insert(index, item)
Inserts the item at index 
```shell
l = LinkedList() 
l.append(1) -> [1]
l.append(3) -> [1, 3]
l.insert(1,2) -> [1, 2, 3]
# "2" is index into which item will be inserted
# if index is bigger then the length of the list, raises IndexError
```


## 3. Remove, RemoveAll, Delete, Pop

## 3.1 remove(item)
Removes item from the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.remove(2) -> [1]
# "2" is item that removes from the list
# if the "item" was not found, raises ValueError
```

## 3.1 remove_all(item)
Removes all items from the list
```shell
l.append(1) -> [1]
l.append(1) -> [1, 1]
l.append(1) -> [1, 1, 1]
l.append(2) -> [1, 1, 1, 2]
l.remove_all(1) -> [2]
# "1" is item that removes completely
# If list is empty, raises IndexError
```

## 3.3 delete(index)
Removes item at a specific index
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.delete(1) -> [1, 3]
# "1" is index of the element to be deleted
# if index is out of the range, raises IndexError
```

## 3.4 pop(index)
Deletes value by index and return data of this value
```shell
l = LinkedList()
l.append(3) -> [3]
l.append(4) -> [3, 4]
l.append(2) -> [3, 4, 2]
l.pop(1) -> 4 , [3, 2]
# "1" is the index of the element to be deleted
# returns deleted data
# if index is out of the range, raises IndexError
```
## 4. Minimal and Maximum

## 4.1 minimal()
Looks for the smallest number in the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(7) -> [1, 7]
l.append(3) -> [1, 7, 3]
l.minimal() -> 1
```
## 4.2 maximal()
Searches for the highest number in the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(7) -> [1, 7]
l.append(3) -> [1, 7, 3]
l.maximal() -> 7
```


## 5. Index of

## 5.1 index_of(item)
Returns the index of the specified number
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.append(7) -> [1, 2, 3, 7]
l.index_of(3) -> 2
# If item was not found, raises ValueError
```


## 6. Print and Str

## 6.1 print(LinkedList)
Displays LinkedList as an array in console
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
print(l)
# outputs [1, 2, 3]
```

## 6.2 str(LinkedList)
Returns all list items as if we were using a print
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
str(l) -> [1, 2, 3] 
# They are the same:
print(str(l))
print(l)
```


## 7. Count, Length, len(), repr()

## 7.1 count(item)
Counts how many "items" are on the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(1) -> [1, 1]
l.append(2) -> [1, 1, 2]

l.count(1) -> 2
```

## 7.2 length()
Counts the length of the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.length() -> 3
```

## 7.3 len(LinkedList)
Counts the length of the list but uses dunder method __len__
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
len(l) -> 3
```

## 7.4 repr(self)
Counts the length of the list but uses dunder method __repr__ and returns it as a string
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
repr(l) -> "3"
```

## 8. Is_Empty and Bool

## 8.1 is_empty()
Indicates whether the list is empty or not
```shell
l = LinkedList()
l.is_empty() -> True

l.append(1) -> [1]
l.is_empty() -> False
```

## 8.2 bool(LinkedList)
Indicates whether something is on the list
```shell
l = LinkedList()
bool(l) -> False

l.append(1) -> [1]
bool(l) -> True
```


## 9. Copy, Clear, To_Set

## 9.1 copy(LinkedList)
Refers to an exact copy of the LinkedList
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]

list_2 = LinkedList.copy(l)
# list_2 -> [1, 2]
```

## 9.2 clear()
Clears the list completely
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.clear() -> []
```

## 9.3 to_set()
Makes a list of unique LinkedList items
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(1) -> [1, 1]
l.append(1) -> [1, 1, 1]
l.append(2) -> [1, 1, 1, 2]
l.append(7) -> [1, 1, 1, 2, 7]
l.to_set()  -> [1, 2, 7]
# It returns an array and not changing LinkedList
```


## 10. Sort and Filter_List

## 10.1 sort()
Sorts the list 
```shell
l = LinkedList()
l.append(8) -> [8]
l.append(6) -> [8, 6]
l.append(5) -> [8, 6, 5]
l.append(11)-> [8, 6, 5, 11]
l.append(1) -> [8, 6, 5, 11, 1]
l.sort() -> [1, 5, 6, 8, 11]
```

## 10.2 filter_list(lamda_condition)
Sorts the list by lambda condition
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.append(4) -> [1, 2, 3, 4]
l.append(5) -> [1, 2, 3, 4, 5]
condition = lambda x: x > 3 
l.filter_list(condition) -> [1, 2, 3]
```


## 11. Shift and Reverse

## 11.1 shift("right" or "left", times)
Moves the list to the right or left "times" times
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]

l.shift("right", 1) -> [3, 1, 2]
# if the direction is not written correctly, raises TypeError
```
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.append(4) -> [1, 2, 3, 4]

l.shift("left", 2) -> [3, 4, 1, 2]
# if the direction is not written correctly, raises TypeError
```
## 11.2 reverse()
Reverses the list
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.append(4) -> [1, 2, 3, 4]
l.reverse() -> [4, 3, 2, 1]
```

## 12. Reduce_List

## 12.1 reduce_list()
Returns the sum of all the elements
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]
l.append(4) -> [1, 2, 3, 4]
l.reduce_list() -> 10
```


## 13. Comparison operator

## 13.1 "<" and "<="
Lengths of lists are compared
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_1.append(3) -> [1, 2, 3]
list_2 = LinkedList.copy(list_1)  -> [1, 2, 3]

list_1 < list_2 # False, 3 < 3
list_1 <= list_2 # True, 3 <= 3

list_2.append(4) -> [1, 2, 3, 4]

list_1 < list_2 # True, 3 < 4
```

## 13.2 ">" and ">="
Lengths of lists are compared
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_1.append(3) -> [1, 2, 3]
list_2 = LinkedList.copy(list_1)  -> [1, 2, 3]

list1 > list_2 # False, 3 > 3
list1 >= list_2 # True 3 >= 3

list_1.append(4) -> [1, 2, 3, 4]

list_1 > list_2 # True, 4 > 3
```

## 13.3 "!=" and "=="
"==" compares each item in the list and if the lists are perfectly equal returns True
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_2 = LinkedList.copy(list_1)  -> [1, 2]

list_1 == list_2(2) # True, 1 == 1, 2 == 2
# =========================================
list_1 = LinkedList()
list_1.append(1)
list_1.append(2)
list_2 = LinkedList()
list_2.append(2)
list_2.append(3)

list_1 == list_2 # False, 1 == 2, 2 == 3
```
"!=" compares each item in the list and if the lists are perfectly equal returns False
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_2 = LinkedList.copy(list_1)  -> [1, 2]

list_1 != list_2(2) # False, 1 != 1, 2 != 2
# =========================================
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_2 = LinkedList()
list_2.append(2) -> [2]
list_2.append(3) -> [2, 3]

list_1 != list_2 # True, 1 != 2, 2 != 3
```

## 13.4 "+=" and "+"
Concatenate the LinkedList with another LinkedList
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_2 = LinkedList.copy(list_1)  -> [1, 2]

list_1 += list_2
list_1 -> [1, 2, 1, 2]
# if list_2 is not LinkedList, raises TypeError
```
```shell
list_1 = LinkedList()
list_1.append(1) -> [1]
list_1.append(2) -> [1, 2]
list_2 = LinkedList.copy(list_1)  -> [1, 2]

list_3 = list_1 + list_2
list_3  -> [1, 2, 1, 2]
# if list_2 is not LinkedList, raises TypeError
```


## 13.5 multiplication
Repeats the LinkedList n number of times
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]

l = l * 3
l -> [1, 2, 1, 2, 1, 2]
# if 3 not int TypeError will be raised
```


## 14. __getitem__, __setitem__, __delitem__   

## 14.1 __getitem__ returns data when using LinkedList[index]
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]

l[1] -> 2
```

## 14.2 __setitem__ changes data when using LinkedList[index] = data
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l[1] = 3

l -> [1, 3]
```

## 14.3 __delitem__ removes data when using LinkedList[index]
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]

del l[1]
l -> [1]
```

## 15. __iter__
Goes through each element using the yield
```shell
l = LinkedList()
l.append(1) -> [1]
l.append(2) -> [1, 2]
l.append(3) -> [1, 2, 3]

x = sum(node.data for node in l.__iter__()) -> 6
```