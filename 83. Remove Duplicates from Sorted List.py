"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
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
    def deleteDuplicates(self, list1: ListNode) -> ListNode:
        head = ListNode(None)
        list_result = head

        while list1:
            if list_result.val != list1.val:
                list_result.next = ListNode(list1.val)
                list_result = list_result.next
            list1 = list1.next
        return head.next


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
    test1 = list_to_listnode([1, 1, 2])
    ans1 = list_to_listnode([1, 2])
    assert Solution().deleteDuplicates(test1) == ans1

    test2 = list_to_listnode([1, 1, 2, 3, 3])
    ans2 = list_to_listnode([1, 2, 3])
    assert Solution().deleteDuplicates(test2) == ans2

    test = list_to_listnode([1, 1, 1, 1, 1])
    ans = list_to_listnode([1])
    assert Solution().deleteDuplicates(test) == ans
    
    test = list_to_listnode([])
    ans = list_to_listnode([])
    assert Solution().deleteDuplicates(test) == ans

    test = list_to_listnode([1, 1, 1, 2, 2])
    ans = list_to_listnode([1, 2])
    assert Solution().deleteDuplicates(test) == ans

if __name__ == '__main__':
    main()
