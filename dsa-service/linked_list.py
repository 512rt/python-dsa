
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class linked_list:

    def __init__(self):
        pass

    def load_run_ll(self):
        # Set up linked list - load data
        # nodes = [1,2,3,4,5,6]
        # print(f"src -> {nodes}")

        # dummy = ListNode()
        # cur = dummy
        # for n in nodes:
        #     cur.next = ListNode(n)
        #     cur = cur.next
        
        # calling the code
        # head = self.load_ll(nodes)
        # result = self.reverseBetween(head, 2, 5)

        # calling the code
    #Input: l1 = [2,4,3], l2 = [5,6,4]

        node1 = [1,8,9]
        node2 = [4,5,7]
        print(f"l1 -> {node1}")
        print(f"l2 -> {node2}")
        head1 = self.load_ll(node1)
        head2 = self.load_ll(node2)
        result = self.addTwoNumbers(head1, head2)


        # Printing the result
        res = []
        cur = result
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        print(f"result -> {res}")
    
    def load_ll(self, nodes: List[int]) -> ListNode:
        dummy = ListNode()
        cur = dummy
        for n in nodes:
            cur.next = ListNode(n)
            cur = cur.next
        
        return dummy.next
        

            


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

    #region 2. Add Two Numbers
    #You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    #You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    #Example 1:

    #Input: l1 = [2,4,3], l2 = [5,6,4]
    #Output: [7,0,8]
    #Explanation: 342 + 465 = 807.
    #Example 2:

    #Input: l1 = [0], l2 = [0]
    #Output: [0]
    #Example 3:

    #Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    #Output: [8,9,9,9,0,0,0,1]
    #Constraints:
    #The number of nodes in each linked list is in the range [1, 100].
    #0 <= Node.val <= 9
    #It is guaranteed that the list represents a number that does not have leading zeros.
    #endregion

    def addTwoNumbers(self, l1, l2):
        
        carry = 0

        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            res = v1 + v2 + carry
            carry = res//10
            res = res%10

            cur.next = ListNode(res)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
