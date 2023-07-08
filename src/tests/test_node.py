from SimpleSinglyLinkedList.node import Node



def test_data_getter():
    """
    Test to see if the data from the node gets correctly 
    """
    new_node = Node(2)
    assert new_node.data == 2
    
def test_data_setter():
    """
    Test to see if the data in the node sets correctly 
    """
    new_node = Node(2)
    new_node.data = 3
    assert new_node.data == 3


def test_next_getter():
    """ 
    Test to see if the elements are correctly attached
    """
    new_node = Node(2)
    assert new_node.advance == None

def test_next_setter():
    """ 
    Test to see if the next elements sets correctly
    """
    new_node = Node(2)
    new_node.advance = 3
    assert new_node.advance == 3