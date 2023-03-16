"""
Given the head of a linked list, return the list after sorting it in ascending order.
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
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        lst = []
        while head.next:
            lst.insert(0, head.val)
            head = head.next
        lst.insert(0, head.val)
        l = sorted(lst)

        head = ListNode(l[0])
        tail = head
        for i in l[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        return head


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
    test = list_to_listnode([1, 2, 4, 3, 7, 6])
    ans = list_to_listnode([1, 2, 3, 4, 6, 7])
    assert Solution().sortList(test) == ans, ans

    test = list_to_listnode([-1,5,3,4,0])
    ans = list_to_listnode([-1,0,3,4,5])
    assert Solution().sortList(test) == ans, ans

    test = list_to_listnode([])
    ans = list_to_listnode([])
    assert Solution().sortList(test) == ans, ans


if __name__ == '__main__':
    main()
