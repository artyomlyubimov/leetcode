"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val}->{self.next}'
    
    def __call__(self) -> str:
        return f'{self.val}->{self.next}'
    
    def __eq__(self, other) -> bool:
        return self() == other()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_t = tuple(str(self.to_int(l1) + self.to_int(l2))[::-1])
        head = ListNode(res_t[0])
        tail = head
        for i in res_t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        return head

    def to_int(self, l: ListNode) -> int:
        if l.next:
            s = ''
            while l.next:
                s += str(l.val)
                l = l.next
            s += str(l.val)
        else:
            s = str(l.val)
        return int(s[::-1])
    

def list_to_listnode(l: list) -> ListNode:
    if not l:
        return None
    head = ListNode(l[0])
    tail = head
    for i in l[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head
    

def main():
    l1 = list_to_listnode([2, 4, 3])
    l2 = list_to_listnode([5, 6, 4])
    ans = list_to_listnode([7, 0, 8])
    test = Solution().addTwoNumbers(l1, l2)
    assert test == ans, test

    l1 = list_to_listnode([2,4,9])
    l2 = list_to_listnode([5,6,4,9])
    ans = list_to_listnode([7,0,4,0,1])
    test = Solution().addTwoNumbers(l1, l2)
    assert test == ans, test


if __name__ == '__main__':
    main()
