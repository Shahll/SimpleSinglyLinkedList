from node import Node


class LinkedList:
    """
    A class representing a SLinkedList

    :param head: The first node of the SLinkedList
    :type head: Node
    """
    
    def __init__(self):
        self._head = None
    #
    #
    #
    def __iter__(self):
        """ 
        Iterator for the class that goes through the elements
        """
        current = self._head
        while current:
            yield current
            current = current.advance
    #
    #
    #
    def __repr__(self):
        """ 
        Counts how many items in the SLinkedList and outputs them as a string
        
        :return: the number of numbers in the list
        :rtype: str
        """
        count = 0
        if self._head is None:
            return str(count)

        current = self._head
        while current:
            count += 1
            current = current.advance

        return str(count)
    #
    #
    #
    def __str__(self): 
        """
        The way the SLinkedList in the "print" function. Output looks like this:
        [element, element, element]  ||  [1, 2, 3]
        
        :return: all SLinkedList elements 
        :rtype: str
        """
        if self._head is None:
            return "[]"
        nodes = []
        current = self._head
        while current:
            nodes.append(str(current.data))
            current = current.advance

        return "[" + ", ".join(nodes) + "]"
    #
    #
    #
    def __len__(self):
        """ 
        How the "len" function on the SLinkedList will work
        Count all elements in the SLinkedList
        
        :return: length of the list
        :rtype: int
        """
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.advance
        return count
    #
    #
    #
    def __lt__(self, other):
        """
        How the < in SLinkedList comparison operator works
        Compares the lengths of the SLinkedList lists
        If the other is not the correct data type a NotImplemented returns
        
        :other: other SLinkedList
        :other type: LinkedList
        
        :return: whether the comparison is true
        :rtype: bool
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) < len(other)
    #
    #
    #
    def __le__(self, other):
        """
        How the <= in SLinkedList comparison operator works
        Compares the lengths of the SLinkedList lists
        If the other is not the correct data type a NotImplemented returns
        
        :other: other SLinkedList
        :other type: LinkedList
        
        :return: whether the comparison is true
        :rtype: bool
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) <= len(other)
    
    #
    #
    #
    def __eq__(self, other):
        """ 
        How the comparison operator == works in SLinkedList
        Compares each element of a SLinkedList
        If the other is not the correct data type a NotImplemented returns
        
        :other: other SLinkedList
        :other type: LinkedList
        
        :return: if the comparison is true
        :rtype: bool
        
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        current_self = self._head
        current_other = other._head
        while current_other and current_self:
            if current_other.data != current_self.data:
                return False
            current_self = current_self.advance
            current_other = current_other.advance
        if current_self is None and current_other is None: 
            return True
        else:
            return False
    #   
    # 
    #
    def __ne__(self, other):
        """
        How the comparison operator != works in SLinkedList
        Compares each element of a SLinkedList
        If the other is not the correct data type a NotImplemented returns
        
        :other: other SLinkedList
        :other type: LinkedList
        
        :return: whether the comparison is true
        :rtype: bool
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        current_self = self._head
        current_other = other._head
        while current_other and current_self:
            if current_other.data != current_self.data:
                return True
            current_self = current_self.advance
            current_other = current_other.advance
        if current_self is None and current_other is None: 
            return False
        else:
            return True
    #  
    #
    #
    def __gt__(self, other):
        """
        How the > in SLinkedList comparison operator works
        Compares the lengths of the SLinkedList lists
        If the other is not the correct data type a NotImplemented returns
        
        :other: other SLinkedList
        :other type: LinkedList
        
        :return: whether the comparison is true
        :rtype: bool
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) > len(other)
    #
    #
    #
    def __ge__(self, other):
        """
        How the >= in SLinkedList comparison operator works
        Compares the lengths of the SLinkedList lists
        If the other is not the correct data type a NotImplemented returns
        
        :return: whether the comparison is true
        :rtype: bool
        """
        if not isinstance(other, LinkedList):
            return NotImplemented
        return len(self) >= len(other)
    #
    #
    #
    def __bool__(self):
        """ 
        Empty SLinkedList or not
        
        :return: SLinkedList empty or noy
        :rtype: bool
        """
        return False if self._head is None else True
    #
    #
    #
    def __mul__(self, other):
        """
        How the * symbol works with SLinkedList
        LinkedList([1, 2, 3]) * 3 -> [1, 2, 3, 1, 2, 3, 1, 2, 3]
        If the other is not the correct data type a TyperError is displayed
        
        :other: how many times SLinkedList will be multiplied
        :other type: int
        
        :return: multiplied SLinkedList
        :rtype: LinkedList
        """
        if isinstance(other, int):
            base_list = self.copy()
            for _ in range(other - 1):
                for item in base_list:
                    self.append(item.data)
            return self
        else:
            raise TypeError("Unsupported operand type for *: int expected")
    #
    #
    #
    def __iadd__(self, other):
        """
        Concatenate the LinkedList with another LinkedList using the += operator.
        If the operand type for += is not supported (expected LinkedList), raises TypeError
        
        :param other: the LinkedList to concatenate with the current LinkedList.
        :type other: LinkedList
        """
        if isinstance(other, LinkedList):
            if self._head is None :
                self._head = other._head
            elif self._head.advance is None:
                self._head.advance = other._head
            else:
                current = self._head
                while current.advance:
                    current = current.advance
                current.advance = other._head
        else:
            raise TypeError("Unsupported operand type for +=: LinkedList expected")
        
        return self
    #
    #
    #
    def __add__(self, other):
        """
        Concatenate two LinkedLists using the + operator.
        If the operand type for + is not supported (expected LinkedList), raises TypeError
        
        :param other: the LinkedList to concatenate with the current LinkedList.
        :type other: LinkedList

        :return: a new LinkedList that is the concatenation of the current LinkedList and the other LinkedList.
        :rtype: LinkedList
        """
        if isinstance(other, LinkedList):
            current_self = self._head
            current_other = other._head
            new_list = LinkedList()
            while current_self:
                new_list.append(current_self.data)
                current_self = current_self.advance
            while current_other:
                new_list.append(current_other.data)
                current_other = current_other.advance
        else:
            raise TypeError("Unsupported operand type for +: LinkedList expected")
        return new_list
    #
    #
    #
    def __radd__(self, other):
        """
        Concatenate the LinkedList with another LinkedList using the + operator (when the LinkedList is on the right side).
        If the operand type for + is not supported (expected LinkedList), raises TypeError

        :param other: the LinkedList to concatenate with the current LinkedList.
        :type other: LinkedList

        :return: a new LinkedList that is the concatenation of the other LinkedList and the current LinkedList.
        :rtype: LinkedList 
        """
        if isinstance(other, LinkedList):
            current_self = self._head
            current_other = other._head
            new_list = LinkedList()
            while current_self:
                new_list.append(current_self.data)
                current_self = current_self.advance
            while current_other:
                new_list.append(current_other.data)
                current_other = current_other.advance
        else:
            raise TypeError("Unsupported operand type for +: LinkedList expected")
        return new_list
    #
    #
    #
    def __getitem__(self, index):
        """
        Get the item at the specified index.

        :param index: the index of the item to get.
        :type index: int
        """
        if index < 0:
            index = len(self) + index
        current = self._head
        i = 0 
        while current:
            if index == i:
                return current.data
            i += 1
            current = current.advance
    #
    #
    #
    def __setitem__(self, index, item):
        """
        Set the item at the specified index.

        :param index: the index of the item to set.
        :type index: int

        :param item: the new value to set at the specified index.
        :type item: any
        """
        if index < 0:
            index = len(self) + index
        current = self._head
        i = 0 
        while current:
            if index == i:
                current.data = item
                break
            i += 1
            current = current.advance
        return self
    #
    #
    #
    def append(self, item):
        """
        Adds a new node with the specified data to the end of the SLinkedList

        :param item: the data for the new node
        :type item: any
        """
        if not self._head:
            self._head = Node(item)
        else:
            current = self._head
            while current.advance:
                current = current.advance
            current.advance = Node(item)
    #
    #
    #
    def prepend(self, item):
        """
        Adds a new node with the specified data to the start of the SLinkedList

        :param item: the data for the new node
        :type item: any
        """
        self._head = Node(item, self._head)
    #
    #
    #
    def length(self):
        """
        Returns the length of the SLinkedList as an integer
        
        :return: length of the SLinkedList
        :rtype: int
        """
        if self._head == None:
            return 0
        current = self._head
        l = 0
        while current:
            l += 1
            current = current.advance
        return l
    #
    #
    #
    def insert(self, index, item):
        """
        Inserts the value "item" by the index "index"
        If index is negative or greater than SLinkedList length, outputs IndexError

        :param item: the data for the new node
        :type item: any
        
        :param index: the index for the new node
        :type item: int
        """
        if index < 0:
            raise IndexError("Index can't be negative number")
        if index > self.length() - 1:
            raise IndexError("Index can't be bigger that lenght of the list")
        
        current = self._head
        previous = None
        new_node = Node(item)
        i = 0
        while i != index:
            i += 1
            previous = current
            current = current.advance
        previous.advance = new_node
        new_node.advance = current
    #
    #
    #
    def append_before(self, beforeValue, item):
        """
        Adds value "item" before value "beforeValue"
        If no "beforeValue" is found, outputs ValueError

        :param beforeValue: the data before which the new value will be added
        :type beforeValue: any
        
        :param item: the value for the new node
        :type item: any
        """
        current = self._head
        previous = None
        find = False

        new_node = Node(item)
        while current and not find:
            if current.data == beforeValue:
                find = True
            if find != True:
                previous = current
                current = current.advance

        if find == False:
            raise ValueError(f"There is no number {beforeValue} in the list")

        previous.advance = new_node
        new_node.advance = current
    #
    #
    #
    def append_after(self, afterValue, item):
        """
        Adds value "item" after value "afterValue"
        If no "afterValue" is found, outputs ValueError

        :param afterValue: the data after which the new value will be added
        :type afterValue: any
        
        :param item: the value for the new node
        :type item: any
        """
        current = self._head
        previous = None
        find = False
        new_node = Node(item)
        while current and not find:
            find = current.data == afterValue
            previous = current
            current = current.advance
        if not find:
            raise ValueError(f"There is no number {afterValue} in the list")
        previous.advance = new_node
        new_node.advance = current
    #
    #
    #
    def remove(self, item):
        """
        Removes the "item" from the list 
        If list is empty, outputs IndexError
        If the "item" was not found, outputs ValueError

        :param item: the value to remove
        :type item: any
        """
        if self._head == None:
            raise IndexError("List out of the range")

        elif (self._head.data == item and self.length() != "1"):  
            temp = self._head
            self._head = self._head.advance
            temp.advance = None
            del temp

        elif (self._head.data == item and self.length == "1"): 
            self._head = None

        else:
            current = self._head
            previous = None
            find = False

            while current and not find:
                if current.data == item:
                    find = True
                if find != True:
                    previous = current
                    current = current.advance

            if find != True:
                raise ValueError(f"There is no item {item} in the list")

            previous.advance = current.advance
    #
    #
    #
    def remove_all(self, item):
        """
        Removes all values "item" from the list 
        If list is empty, outputs IndexError

        :param item: the value to remove
        :type item: any
        """
        if self._head == None:
            raise IndexError("List out of range")

        if (self._head.data == item and self.length() == 1):  
            self._head = None
            return

        current = self._head
        previous = None

        while current:
            if current.data == item:
                if previous is None:
                    self._head = current.advance
                else:
                    previous.advance = current.advance
                current.advance = None
                del current
                current = self._head
            else:
                previous = current
                current = current.advance
    #
    #
    #
    def delete(self, index):
        """
        Delete value by index from the list 
        If list is empty, outputs IndexError
        If index is out of the range, outputs IndexError

        :param index: the index of item to remove
        :type item: int
        """
        if self._head == None:
            raise IndexError("List out of the range")

        if index == 0:
            temp = self._head
            self._head = self._head.advance
            temp.advance = None
            del temp
        else:
            current = self._head
            previous = None
            i = 0
            find = False
            while current and find != True:
                i += 1
                previous = current
                current = current.advance

                find = i == index

            if find == False:
                raise IndexError("List out of the range")

            previous.advance = current.advance
    #
    #
    #
    def is_empty(self):
        """
        Checking whether the SLinkedList is empty or not
        
        :return: the SLinkedList is empty or not
        :rtype: bool
        """
        return self._head == None
    #
    #
    #
    def minimal(self):
        """ 
        Searches for the minimum number in the list
        If SLinkedList is empty returns None
        
        :return: minimal number
        :rtype: int
        """
        if self._head == None:
            return None
        current = self._head
        minimal = current
        while current:
            if current.data < minimal.data:
                minimal = current
            current = current.advance

        return minimal.data
    #
    #
    #
    def maximal(self):
        """ 
        Searches for the maximal number in the list
        If SLinkedList is empty returns None
        
        :return: maximal number
        :rtype: int
        """
        if self._head == None:
            return None
        current = self._head
        maximal = current
        while current:
            if current.data > maximal.data:
                maximal = current
            current = current.advance

        return maximal.data
    #
    #
    #
    def index_of(self, item):
        """ 
        Searches the index of the "item" element
        If value is not in the list, outputs ValueError
        
        :param item: the value whose index is searched for in the SLinkedList
        :type item: any
        
        :return: index of the value
        :rtype: int
        """
        if self._head == None:
            return None

        i = 0
        current = self._head
        find = False
        while current and not find:
            if current.data == item:
                find = True
            else:
                i += 1
                current = current.advance

        if find == False:
            raise ValueError(f"There is no item {item} in the list")

        return i
    #
    #
    #
    def reduce_list(self):
        """ 
        Counts the sum of all the elements in the SLinkedList
        
        :return: sum of all elements
        :rtype: int        
        """
        if self._head is None or self._head.advance is None:
            return self._head.data if self._head is not None else None

        current = self._head
        total = 0
        while current:
            total += current.data
            current = current.advance

        return total
    #
    #
    #
    def clear(self):
        """
        Clears the SLinkedList completely
        """
        while self._head != None:
            temp = self._head
            self._head = self._head.advance
            del temp
    #
    #
    #
    def reverse(self):
        """ 
        Reverses the SLinkedList
        """
        if self._head is None or self._head.advance is None:
            return self._head

        current = self._head
        previous = None
        temp = None

        while current:
            temp = current.advance
            current.advance = previous
            previous = current
            current = temp

        self._head = previous
    #
    #    
    #
    def count(self, item):
        """ 
        Counts how many "items" are on the list in the SLinkedList using __iter__
        
        :return: how many "items" in the list
        :rtype: int
        """
        return sum(1 for node in self.__iter__() if node.data == item)
    #
    #
    #
    def to_set(self):
        """
        Makes from SLinkedList set individual of the elements
        
        :return: set of elements
        :rtype: list
        """
        lst = []
        current = self._head
        while current:
            if current.data not in lst:
                lst.append(current.data)
            current = current.advance

        return lst
    #
    #
    #
    def filter_list(self, condition):
        """ 
        Filters the list according to a lambda function condition 
        
        :param condition: condition according to which the LinkedList will be filtered
        :condition type: lambda function
        """
        current = self._head
        previous = None

        while current:
            if condition(current.data):
                if previous is None:
                    self._head = current.advance
                else:
                    previous.advance = current.advance
                current = current.advance
            else:
                previous = current
                current = current.advance
    #
    #
    #
    def pop(self, index):
        """ 
        Deletes value by index and return data of this value
        If index is out of the range, ouputs IndexError
        
        :param index: index of the element to be deleted
        :index type: int
        
        :return: data of the value
        :rtype: any
        """
        current = self._head
        previous = None
        inner_index = 0
        find = False

        if index == 0 and self._head is not None:
            data = self._head.data
            self._head = current.advance
            return data

        while current and not find:
            find = inner_index == index
            if not find:
                inner_index += 1
                previous = current
                current = current.advance
        if not find:
            raise IndexError(f"There is no index {index} in the list")

        previous.advance = current.advance
        return current.data
    #
    #
    #
    def copy(self):
        """ 
        Copies the SLinkedList and returns a copy of it
        
        :return: copy of the SLinkedList
        :rtype: LinkedList
        """
        new_list = LinkedList()
        current = self._head

        while current:
            new_list.append(current.data)
            current = current.advance

        return new_list
    #
    #
    #        
    def sort(self):
        """ 
        Sorts the SLinkedList using a built-in function in python
        
        :return: new sorted SLinkedList with elements of SLinkedList
        :rtype: LinkedList
        """
        string = str(self)
        string = string[1:-1]
        arr = []
        new_list = LinkedList()
        for char in string.split(", "):
            arr.append(int(char))
        for number in sorted(arr):
            new_list.append(number)
        return new_list
    #
    #
    #
    def shift(self, direction, times):
        """ 
        Moves the SLinkedList left or right by the specified number of items
        If direction was written incorrect, outputs TypeError
        
        :param direction: the direction in which the SLinkedList will be moved
        :direction type: string, "left" or "right"
        
        :param times: the number of elements by which the SLinkedList will be shifted
        :times type: int
        """
        if direction == "left":
            for _ in range(times):
                self.append(self.pop(0))
        elif direction == "right":
            for _ in range(times):
                self.prepend(self.pop(len(self) -1))
        else:   
            raise TypeError("Unsupported variable : 'left' or 'right' expected")

if __name__ == "__main__":
    
    list_1 = LinkedList()
    list_1.append(1)
    list_1.append(2)
    list_1.append(3)
    list_2 = LinkedList.copy(list_1)

    list_1.append(3)

    print(list_2 < list_1)
    
