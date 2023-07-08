from SimpleSinglyLinkedList.linked_list import LinkedList
import pytest


class TestLinkedListPrepend:
    def test_prepend(self):
        """
        Tests the prepend() method in the LinkedList class.
        Checks if the value added to the beginning of the list
        becomes the first element.
        """
        l = LinkedList()
        l.append(3)
        l.append(2)
        l.prepend(1)
        assert str(l)[1] == "1"
#
#
#
class TestLinkedListLength:
    def test_length(self):
        """
        Tests the length() method in the LinkedList class.
        Checks if the length of the list is returned correctly.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        assert l.length() == 2
#
#
#
class TestLinkedListInsertion:
    def test_insertion(self):
        """
        Tests the insert() method in the LinkedList class.
        Checks if the value inserted at the specified position
        is at the correct position in the list.
        """
        l = LinkedList()
        l.append(1)
        l.append(3)
        l.insert(1, 2)
        assert str(l)[4] == "2"

    def test_if_index_is_negative_number(self):
        """
        Tests the insert() method in the LinkedList class with a negative index.
        Checks if an IndexError is raised when trying to insert an element
        at a negative position.
        """
        l = LinkedList()
        with pytest.raises(IndexError):
            l.insert(-1, 2)

    def test_if_index_is_bigger_then_length_of_the_list(self):
        """
        Tests the insert() method in the LinkedList class with an index
        greater than the length of the list.
        Checks if an IndexError is raised when trying to insert an element
        at a position greater than the length of the list.
        """
        l = LinkedList()
        l.append(2)
        l.append(3)
        with pytest.raises(IndexError):
            l.insert(120, 2)
#
#
#
class TestLinkedListAppend:
    def test_append_if_head_is_none(self):
        """
        Tests the append() method in the LinkedList class when the head is None.
        Checks if the value added to an empty list becomes the first element.
        """
        l = LinkedList()
        l.append(12)
        assert repr(l) == "1"

    def test_append_if_head_contains_more_than_one_element(self):
        """
        Tests the append() method in the LinkedList class when the head contains more than one element.
        Checks if the value added to the list increases its length.
        """
        l = LinkedList()
        for _ in range(3):
            l.append(12)
        assert repr(l) == "3"
#
#
#
class TestLinkedListAppendBefore:
    def test_append_before(self):
        """
        Tests the append_before() method in the LinkedList class.
        Checks if the value added before the specified value is at the expected position.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append_before(2, 5)
        assert str(l)[4] == "5"

    def test_if_user_wrote_number_that_is_not_in_the_list(self):
        """
        Tests the append_before() method in the LinkedList class with a value that is not in the list.
        Checks if a ValueError is raised when trying to add a value before a value that does not exist in the list.
        """
        l = LinkedList()
        l.append(1)
        l.append(3)
        l.append(5)
        with pytest.raises(ValueError):
            l.append_before(2, 4)
#
#
#
class TestLinkedListAppendAfter:
    def test_append_after(self):
        """
        Tests the append_after() method in the LinkedList class.
        Checks if the value added after the specified value is at the expected position.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append_after(2, 5)
        assert str(l)[7] == "5"

    def test_if_user_wrote_number_that_is_not_in_the_list(self):
        """
        Tests the append_after() method in the LinkedList class with a value that is not in the list.
        Checks if a ValueError is raised when trying to add a value after a value that does not exist in the list.
        """
        l = LinkedList()
        l.append(1)
        l.append(3)
        l.append(5)
        with pytest.raises(ValueError):
            l.append_after(2, 4)
#
#
#
class TestLinkedListRemove:
    def test_remove(self):
        """
        Tests the remove() method in the LinkedList class.
        Checks if the specified value is successfully removed from the list.
        """
        l = LinkedList()
        l.append(12)
        l.append(23)
        l.append(3)
        l.remove(23)
        assert repr(l) == "2"

    def test_remove_if_item_is_head_of_the_list(self):
        """
        Tests the remove() method in the LinkedList class when the item to be removed is the head of the list.
        Checks if the head is correctly updated after removing the item.
        """
        l = LinkedList()
        l.append(3)
        l.remove(3)
        assert repr(l) == "0"

    def test_remove_if_element_not_in_list(self):
        """
        Tests the remove() method in the LinkedList class when the specified element is not present in the list.
        Checks if a ValueError is raised when trying to remove an element that does not exist in the list.
        """
        l = LinkedList()
        l.append(3)
        with pytest.raises(ValueError):
            l.remove(2)

    def test_remove_if_list_is_empty(self):
        """
        Tests the remove() method in the LinkedList class when the list is empty.
        Checks if an IndexError is raised when trying to remove an element from an empty list.
        """
        l = LinkedList()
        with pytest.raises(IndexError):
            l.remove(2)
#
#
#
class TestLinkedListRemoveAll:
    def test_remove_item(self):
        """
        Tests the remove_all() method in the LinkedList class.
        Checks if all occurrences of the specified item are successfully removed from the list.
        """
        l = LinkedList()
        l.append(3)
        l.append(2)
        l.append(3)
        l.append(3)
        l.remove_all(3)
        assert repr(l) == "1"

    def test_remove_items_in_empty_list(self):
        """
        Tests the remove_all() method in the LinkedList class when the list is empty.
        Checks if an IndexError is raised when trying to remove items from an empty list.
        """
        l = LinkedList()
        with pytest.raises(IndexError):
            l.remove_all(3)

    def test_if_there_is_no_item_you_want_to_delete(self):
        """
        Tests the remove_all() method in the LinkedList class when the item to be removed is not present in the list.
        Checks if the list remains unchanged when trying to remove an item that does not exist in the list.
        """
        l = LinkedList()
        l.append(3)
        l.append(3)
        l.remove_all(2)
        assert repr(l) == "2"
#
#
#
class TestLinkedListDelete:
    def test_delete_with_str(self):
        """
        Tests the delete() method in the LinkedList class by specifying the index as a string.
        Checks if the element at the specified index is successfully deleted from the list.
        """
        l = LinkedList()
        l.append(3)
        l.append(4)
        l.delete(0)
        assert str(l)[1] == "4"

    def test_delete_with_repr(self):
        """
        Tests the delete() method in the LinkedList class by specifying the index as an integer.
        Checks if the element at the specified index is successfully deleted from the list.
        """
        l = LinkedList()
        l.append(3)
        l.append(4)
        l.delete(1)
        assert repr(l) == "1"

    def test_delete_if_index_out_of_the_range(self):
        """
        Tests the delete() method in the LinkedList class with an index that is out of the range.
        Checks if an IndexError is raised when trying to delete an element at an invalid index.
        """
        l = LinkedList()
        with pytest.raises(IndexError):
            l.delete(0)

    def test_if_index_is_0(self):
        """
        Tests the delete() method in the LinkedList class when the index is 0.
        Checks if the element at index 0 is successfully deleted, and the list is updated accordingly.
        """
        l = LinkedList()
        l.append(3)
        l.append(41)
        l.delete(0)
        assert repr(l) == "1"
#
#
# 
class TestLinkedListMinimal: 
    
    def test_minimal(self):
        """
        Tests the minimal() method in the LinkedList class.
        Adds multiple elements to the list and checks if the minimum value is correctly returned.
        """
        l = LinkedList()
        l.append(7)
        l.append(23)
        l.append(3)
        assert l.minimal() == 3
        
        
    def test_if_list_is_empty(self):
        """
        Tests the minimal() method in the LinkedList class when the list is empty.
        Checks if None is returned as expected.
        """
        l = LinkedList()
        assert l.minimal() == None
       
    def test_if_there_is_only_1_element(self):
        """
        Tests the minimal() method in the LinkedList class when there is only one element in the list.
        Checks if the same element is returned as the minimum.
        """
        l = LinkedList()
        l.append(7)
        assert l.minimal() == 7
#
#
#
class TestLinkedListMaximal: 
    def test_maximal(self):
        """
        Tests the maximal() method in the LinkedList class.
        Adds multiple elements to the list and checks if the maximum value is correctly returned.
        """
        l = LinkedList()
        l.append(7)
        l.append(23)
        l.append(3)
        assert l.maximal() == 23
        
        
    def test_if_list_is_empty(self):
        """
        Tests the maximal() method in the LinkedList class when the list is empty.
        Checks if None is returned as expected.
        """
        l = LinkedList()
        assert l.maximal() == None
        
    def test_if_there_is_only_1_element(self):
        """
        Tests the maximal() method in the LinkedList class when there is only one element in the list.
        Checks if the same element is returned as the maximum.
        """
        l = LinkedList()
        l.append(7)
        assert l.maximal() == 7
#
#
#
class TestLinkedListIndexOf: 
    def test_index_of(self):
        """
        Tests the index_of() method in the LinkedList class.
        Adds multiple elements to the list and checks if the correct index is returned for a given element.
        """
        l = LinkedList()
        l.append(3)
        l.append(7)
        
        assert l.index_of(7) == 1
        
    def test_if_list_do_not_contain_this_item(self):
        """
        Tests the index_of() method in the LinkedList class when the list does not contain the specified item.
        Checks if a ValueError is raised as expected.
        """
        l = LinkedList()
        l.append(3)
        l.append(7)
        
        with pytest.raises(ValueError):
            l.index_of(9)         

    def test_if_list_is_empty(self):
        """
        Tests the index_of() method in the LinkedList class when the list is empty.
        Checks if None is returned as expected.
        """
        l = LinkedList()
        
        assert l.index_of(3) == None
#
#
#
class TestLinkedListReduce:
    def test_reduce(self):
        """
        Tests the reduce_list() method in the LinkedList class.
        Adds multiple elements to the list and checks if the sum of all elements is correctly computed.
        """
        l = LinkedList()
        l.append(3)
        l.append(23)
        l.append(7)
        
        assert l.reduce_list() == 33
        
    def test_if_there_is_only_1_element(self):
        """
        Tests the reduce_list() method in the LinkedList class when there is only one element in the list.
        Checks if the same element is returned as the result.
        """
        l = LinkedList()
        l.append(7)
        
        assert l.reduce_list() == 7
        
    def test_if_list_is_empty(self):
        """
        Tests the reduce_list() method in the LinkedList class when the list is empty.
        Checks if None is returned as expected.
        """
        l = LinkedList()
        
        assert l.reduce_list() == None
#
#
#
class TestLinkedListClear:
    def test_clear(self):
        """
        Tests the clear() method in the LinkedList class.
        Adds multiple elements to the list and checks if the list is emptied after the method is called.
        """
        l = LinkedList()
        for i in range(10):
            l.append(i)
        l.clear()
        assert str(l)[1] == "]"   
        
    def test_if_list_is_already_empty(self):
        """
        Tests the clear() method in the LinkedList class when the list is already empty.
        Checks if the list remains empty after calling the method.
        """
        l = LinkedList()
        l.clear()
        assert str(l)[1] == "]"
#
#
#
class TestLinkedListReverse:
    def test_reverse(self):
        """
        Tests the reverse() method in the LinkedList class.
        Adds multiple elements to the list, calls the reverse() method, and checks if the elements are reversed correctly.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.reverse()
        
        assert str(l) == "[4, 3, 2, 1]"
        
    def test_if_there_is_only_one_element(self):
        """
        Tests the reverse() method in the LinkedList class when there is only one element in the list.
        Checks if the list remains the same after calling the reverse() method.
        """
        l = LinkedList()
        l.append(1)
        l.reverse()
        
        assert str(l) == "[1]"
        
    def test_if_there_is_no_elements(self):
        """
        Tests the reverse() method in the LinkedList class when the list is empty.
        Checks if the list remains empty after calling the reverse() method.
        """
        l = LinkedList()
        l.reverse()
        
        assert str(l) == "[]"
#
#
#
class TestLinkedListCount:
    def test_count(self):
        """
        Tests the count() method in the LinkedList class.
        Adds multiple elements to the list and checks if the count of a specific element is correctly computed.
        """
        l = LinkedList()
        l.append(2)
        l.append(2)
        l.append(2)
        l.append(7)
        
        assert l.count(2) == 3
        
    def test_if_list_is_empty(self):
        """
        Tests the count() method in the LinkedList class when the list is empty.
        Checks if the count of a specific element is 0.
        """
        l = LinkedList()
        
        assert l.count(1) == 0
#
#
#
class TestLinkedListToSet:
    def test_to_set(self):
        """
        Tests the to_set() method in the LinkedList class.
        Adds multiple elements to the list and checks if the list is correctly converted to a set.
        """
        l = LinkedList()
        l.append(3)
        l.append(3)
        l.append(1)
        l.append(5)

        assert l.to_set() == [3, 1, 5]
        
    def test_if_list_is_empty(self):
        """
        Tests the to_set() method in the LinkedList class when the list is empty.
        Checks if an empty set is returned.
        """
        l = LinkedList()
        
        assert l.to_set() == []
#
#
#
class TestLinkedListFilter:
    def test_filter(self):
        """
        Tests the filter_list() method in the LinkedList class.
        Adds multiple elements to the list and applies a filtering condition to check if the list is correctly filtered.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        condition = lambda x: x > 3
        l.filter_list(condition)
        
        assert str(l) == "[1, 2, 3]"
        
    def test_if_list_is_empty(self):
        """
        Tests the filter_list() method in the LinkedList class when the list is empty.
        Checks if an empty list is returned after applying the filtering condition.
        """
        l = LinkedList()
        condition = lambda x: x > 3
        l.filter_list(condition)
        
        assert str(l) == "[]"
#
#
# 
class TestLinkedListPop:
    def test_pop_data(self):
        """
        Tests the pop() method in the LinkedList class for removing and returning an element at a given index.
        Adds multiple elements to the list and checks if the correct element is returned after popping.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)        
        
        assert l.pop(1) == 2
        
    def test_pop_list(self):
        """
        Tests the pop() method in the LinkedList class for removing an element at a given index.
        Adds multiple elements to the list, pops an element, and checks if the list is correctly modified.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)        
        l.pop(1)
        
        assert str(l) == "[1, 3, 4]"
        
    def test_if_index_out_of_the_range(self):
        """
        Tests the pop() method in the LinkedList class when the index is out of range.
        Checks if the IndexError exception is raised.
        """
        l = LinkedList()
        
        with pytest.raises(IndexError):
            l.pop(23)
#
#
#
class TestLinkedListCopy:
    def test_copy(self):
        """
        Tests the copy() method in the LinkedList class.
        Adds elements to the list, creates a copy, and checks if the copied list is the same as the original list.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        b = l.copy()
        
        assert str(b) == "[1, 2]"
        
    def test_can_you_use_commands(self):
        """
        Tests the copy() method in the LinkedList class for deep copying.
        Adds elements to the list, creates a copy, modifies the copied list, and checks if the modifications do not affect the original list.
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        b = l.copy()
        b.append(3)
        b.delete(0)
        
        assert str(b) == "[2, 3]"   
#
#
#
class TestLinkedListLen:
    def test_len(self):
        """
        Tests the length() method in the LinkedList class.
        Adds elements to the list and checks if the length of the list matches the expected length using both length() method and len() function.
        """
        l = LinkedList()
        l.append(1)
        
        assert l.length() == len(l)
#
#
#
class TestLinkedListBubbleSort:
    def test_bubble_sort(self):
        """
        Test the bubble_sort() method in LinkedList class.
        Chechks if list after this function is equals to sorted list     
        """
        l = LinkedList()
        l.append(8)
        l.append(12)
        l.append(1)
        l.append(9)     
        l.bubble_sort()
        assert str(l) == "[1, 8, 9, 12]" 
    
    def test_if_list_is_empty(self):
        """
        Test so that an empty sorted list does not give an error 
        """
        l = LinkedList()  
        l.bubble_sort()
        assert str(l) == "[]"
#
#
#
class TestLinkedListLt:
    def test_lt_where_lists_have_different_size(self):
        """ 
        Test dunder method __lt__(self)
        check if the < sign is working 
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)

        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 < linked_list2) is True
        assert (linked_list2 < linked_list1) is False
#
#
#
class TestLinkedListLe:
    def test_le_but_lists_have_different_length(self):
        """ 
        Test dunder method __le__(self)
        check if the < sign is working 
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)

        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list2 <= linked_list1) is False 
        assert (linked_list1 <= linked_list2) is True
        
    def test_le_but_lists_have_the_same_length(self):
        """
        Check if the = sign is working
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        linked_list1.append(2)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list2 <= linked_list1) is True 
        assert (linked_list1 <= linked_list2) is True
#
#
#
class TestLinkedListEq:
    def test_eq_where_lists_have_the_same_size(self):
        """
        Tests for dunder method __eq__(self)
        tests where the answer must be True
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        linked_list1.append(2)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 == linked_list2) is True
        assert (linked_list2 == linked_list1) is True
        
    def test_eq_but_lists_have_different_size(self):
        """ 
        tests where the answer must be False
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 == linked_list2) is False
        assert (linked_list2 == linked_list1) is False
#
#
#
class TestLinkedListNe:
    def test_ne_where_lists_are_not_the_same(self):
        """
        Tests for dunder method __ne__(self)
        tests where the answer must be True
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 != linked_list2) is True
        assert (linked_list2 != linked_list1) is True
        
    def test_ne_but_lists_are_the_same(self):
        """ 
        tests where the answer must be True
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        linked_list1.append(2)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 != linked_list2) is False
        assert (linked_list2 != linked_list1) is False
#
#
#
class TestLinkedListGt:
    def test_qt_where_lists_have_different_size(self):
        """
        Tests for dunder methid __gt__(self)
        Check if the > sign is working 
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)

        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list1 > linked_list2) is False
        assert (linked_list2 > linked_list1) is True
#
#
#
class TestLinkedListGe:
    def test_qe_where_lists_have_different_size(self):
        """
        Tests for dunder methid __ge__(self)
        Check if the > sign is working 
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)

        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list2 <= linked_list1) is False
        assert (linked_list1 <= linked_list2) is True
        
    def test_ge_but_lists_have_the_same_length(self):
        """
        Check if the = sign is working
        """
        linked_list1 = LinkedList()
        linked_list1.append(1)
        linked_list1.append(2)
        
        linked_list2 = LinkedList()
        linked_list2.append(1)
        linked_list2.append(2)
        
        assert (linked_list2 <= linked_list1) is True 
        assert (linked_list1 <= linked_list2) is True
#
#
#
class TestLinkedListBool:
    def test_bool(self):
        """
        Test for dunder method __bool__(self)
        checks an empty list
        """
        l = LinkedList()
        assert bool(l) == False
        
    def test_bool_but_list_contain_item(self):
        """
        checks the list with the element.
        """
        l = LinkedList()
        l.append(7)
        assert bool(l) == True
#
#
#        
class TestLinkedListMul:
    def test_mul(self):
        """
        Test for dunder method __mul__(self)
        test when in the list is 1 element
        """
        l = LinkedList()
        l.append(1)
        l *= 3
        assert str(l) == "[1, 1, 1]"
    
    def test_mul_but_list_is_empty(self):
        """
        Test for an empty list
        """
        l = LinkedList()
        l *= 3
        assert str(l) == "[]"
#
#
#
class TestLinkedLisIadd:
    def test_iadd(self):
        """
        Tests for dunder method __iadd__(self)
        test whether the lists have been added correctly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l2 = LinkedList()
        l2.append(3)
        l2.append(4)
        l += l2
        assert str(l) == "[1, 2, 3, 4]"   
#
#
#
class TestLinkedListIsEmpty:
    def test_is_empty(self):
        """
        Tests for function is_empty()
        Test where answer must be True
        """
        l = LinkedList()
        
        assert l.is_empty() == True
        
    def test_is_empty_but_list_is_not_empty(self):
        """
        Test where answer must be False
        """
        l = LinkedList()
        l.append(2)
        
        assert l.is_empty() == False
#
#
#
class TestLinkedListStr:
    def test_str(self):
        """
        Test for dunder method __str__()
        test the correctness of the output
        """
        l = LinkedList()
        
        assert str(l) == "[]"
        
    def test_str_2(self):
        """
        test the correctness of the output
        """
        l = LinkedList()
        l.append(3)
        
        assert str(l) == "[3]"
#
#
#
class TestLinkedListRepr:
    def test_repr(self):
        """
        Test for dunder method __repr__(self)
        correctness test for element counting
        """
        l = LinkedList()
        l.append(2)
        l.append(3)
        
        assert repr(l) == "2"
        
    def test_repr_1(self):
        """
        correctness test for element counting
        """
        l = LinkedList()
        
        assert repr(l) == "0"
#
#
#
class TestLinkedListIter:
    def test_iter(self):
        """
        Test for dunder __iter__(self)
        Test if iteration works properly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        
        result = []
        for item in l:
            result.append(item.data)
            
        assert str(l) == str(result)
#
#
#
class TestLinkedListBubbleSort:
    def test_bubble_sort(self):
        """
        Test for bubble_sort function
        test if the array is correctly sorted
        """
        l = LinkedList()
        l.append(9)
        l.append(17)
        l.append(4)
        l.append(23)
        l.append(12)
        l.append(8)
        l.append(5)
        l.append(19)
        l.append(14)
        l.append(1)
        l.bubble_sort()
        assert str(l) == "[1, 4, 5, 8, 9, 12, 14, 17, 19, 23]"
#
#
#
class TestLinkedListAdd:
    def test_add(self):
        """
        Tests for dunder method __add__
        Test whether the lists have been added correctly
        """
        l = LinkedList()
        l.append(3)
        l.append(4)
        
        b = LinkedList()
        
        b.append(5)
        b.append(6)
        c = l + b
        
        assert str(c) == "[3, 4, 5, 6]"
#
#
#
class TestLinkedListRadd:
    def test_radd(self):
        """
        Tests for dunder method __radd__
        Test whether the lists have been added correctly
        """
        l = LinkedList()
        l.append(3)
        l.append(4)
        
        b = LinkedList()
        
        b.append(5)
        b.append(6)
        c = l + b
        
        assert str(c) == "[3, 4, 5, 6]"
#
#
#
class TestLinkedListQuickSort:
    def test_quick_sort(self):
        """
        Test for function quick_sort(LinkedList)
        test if the array is correctly sorted
        """
        l = LinkedList()
        l.append(9)
        l.append(17)
        l.append(4)
        l.append(23)
        l.append(12)
        l.append(8)
        l.append(5)
        l.append(19)
        l.append(14)
        l.append(1)
        l = l.quick_sort(l)
        assert str(l) == "[1, 4, 5, 8, 9, 12, 14, 17, 19, 23]"
#
#
#
class TestLinkedListGetItem:
    def test_getitem(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        
        assert l[0] == 1
        
    def test_but_index_is_negative(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        
        assert l[-1] == 3
#
#
#
class TestLinkedListSetItem:
    def test_setitem(self):
        """
        Test for dunder __setitem__(self)
        test whether index 0 has been replaced correctly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l[0] = 4
        
        assert l[0] == 4
        
    def test_but_index_is_negative(self):
        """
        test whether negative index has been replaced correctly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l[-1] = 4
        
        assert l[-1] == 4
#
#
#
class TestLinkedListShift:
    def test_right_shift(self):
        """
        Test function shift("right"/"left", times)
        Test if right shift works correctly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        
        l.shift("right", 1)
        
        assert str(l) == "[4, 1, 2, 3]"
        
    def test_left_shift(self):
        """
        Test if left shift works correctly
        """
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        
        l.shift("left", 1)
        
        assert str(l) == "[2, 3, 4, 1]"