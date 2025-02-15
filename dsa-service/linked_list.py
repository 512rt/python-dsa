
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class linked_list:

    def __init__(self):
        pass

    def load_run_ll(self):
        # Set up linked list - load data
        nodes = [1,2,3,4,5,6]
        print(f"src -> {nodes}")

        dummy = ListNode()
        cur = dummy
        for n in nodes:
            cur.next = ListNode(n)
            cur = cur.next
        
        # calling the code
        head = dummy.next
        result = self.reverseBetween(head, 2, 5)

        # Printing the result
        res = []
        cur = result
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        print(f"result -> {res}")
            


    #region 92. Reverse Linked List II
    # Given the head of a singly linked list and two integers left and right where left <= right, 
    # reverse the nodes of the list from position left to position right, and return the reversed list.
    # Example 1: 
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]
    
    # Example 2:
    # Input: head = [5], left = 1, right = 1
    # Output: [5]

    # Constraints:
    # The number of nodes in the list is n.
    # 1 <= n <= 500
    # -500 <= Node.val <= 500
    # 1 <= left <= right <= n
    #endregion
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None:
            return head

        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        
        left -=1
        right -= 1
        while left <= right:
            nodes[left], nodes[right] = nodes[right], nodes[left]
            left += 1
            right -= 1
        
        dummy = ListNode(0)
        cur = dummy
        for n in nodes:
            cur.next = ListNode(n)
            cur = cur.next

        return dummy.next

