class Node:
    """
    A class representing a linked list node.

    :param data: the data stored in the node.
    :type data: preferred int
    """
    def __init__(self, data, newNext=None):
        self.__data = data
        self.__next = newNext
    
    @property
    def data(self):
        """
        Get the data stored in the node.
        
        :return: the data stored in the node.
        :rtype: any
        """
        return self.__data

    @data.setter
    def data(self, newData):
        """
        Set the data stored in the node.
        
        :param newData: the new data to be stored in the node.
        :type newData: any
        """
        self.__data = newData
        
    @property
    def advance(self):
        """
        Get the reference to the next node.
        
        :return: the reference to the next node.
        :rtype: Node
        """
        return self.__next

    @advance.setter
    def advance(self, newNext):
        """
        Set the reference to the next node.
        
        :param newNext: the new reference to the next node.
        :type newNext: Node
        """
        self.__next = newNext

            
        