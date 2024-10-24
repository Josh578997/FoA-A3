from __future__ import annotations

from typing import List, Tuple, TypeVar
from treasure import Treasure
from data_structures.bst import BinarySearchTree
from data_structures.node import TreeNode
from algorithms.mergesort import mergesort
from data_structures.linked_stack import LinkedStack

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: nlog(n)
            Worst Case Complexity: nlog(n)
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)
    def __iter__(self):
        return ReverseBSTInOrderIterator(self.root)
    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: nlog(n)
            Worst Case Complexity: nlog(n)
            n is the amount of elements in the betterbst
        """
        return mergesort(elements,lambda x: x[0])
    
    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: O(n*log(n))
            Worst Case Complexity: O(n*log(n))
            n is the number of elements in the list

        Justification:
            Builds a balanced tree through recursion, the function will be called n amount of times 
            and takes log(n) time to insert into the tree, yeilding an overall complexity of O(n*log(n))

        """
        if len(elements) is not 0:
            mid = len(elements)//2
            self[elements[mid][0]]= elements[mid][1]
            self.__build_balanced_tree(elements[:mid])
            self.__build_balanced_tree(elements[mid+1:])
    

class ReverseBSTInOrderIterator:
    """ Reverse In-order iterator for the binary search tree.
        Performs stack-based BST traversal. (right,root,left)
    """

    def __init__(self, root: TreeNode[K, I]) -> None:
        """ Iterator initialiser. """

        self.stack = LinkedStack()
        self.current = root

    def __iter__(self):
        """ Standard __iter__() method for initialisers. Returns itself. """

        return self

    def __next__(self) -> TreeNode[K, I]:
        """ The main body of the iterator.
            Returns keys of the BST one by one respecting the in-order.
        """

        while self.current:
            self.stack.push(self.current)
            self.current = self.current.right

        if self.stack.is_empty():
            raise StopIteration

        result = self.stack.pop()
        self.current = result.left

        return result