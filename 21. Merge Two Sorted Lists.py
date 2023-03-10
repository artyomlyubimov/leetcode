"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode(None)
        list_result = head

        while list1 and list2:
            if list1.val > list2.val:
                list_result.next =list2 
                list2 = list2.next
            else:
                list_result.next = list1
                list1 = list1.next

            list_result = list_result.next

        if list1:
            list_result.next = list1

        if list2:
            list_result.next = list2

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


def listnode_to_lst(ln: ListNode) -> list:
    lst = []
    while ln.next:
        lst.append(ln.val)
        ln = ln.next
    return lst


def main():
    test1 = Solution().mergeTwoLists(list_to_listnode([1, 2, 4]), list_to_listnode([1, 3, 4]))
    answer1 = list_to_listnode([1, 1, 2, 3, 4, 4])
    assert  test1 == answer1

    test2 = Solution().mergeTwoLists(list_to_listnode([]), list_to_listnode([]))
    answer2 = list_to_listnode([])
    assert test2 == answer2

    test3 = Solution().mergeTwoLists(list_to_listnode([1, 2, 3, 4]), list_to_listnode([]))
    answer3 = list_to_listnode([1, 2, 3, 4])
    assert test3 == answer3

    test4 = Solution().mergeTwoLists(list_to_listnode([1, 3, 5]), list_to_listnode([0, 2, 4, 6, 10]))
    answer4 = list_to_listnode([0, 1, 2, 3, 4, 5, 6, 10])
    assert test4 == answer4

    test5 = Solution().mergeTwoLists(list_to_listnode([-3, -1, 5]), list_to_listnode([-4, -2, 6, 10]))
    answer5 = list_to_listnode([-4, -3, -2, -1, 5, 6, 10])
    assert test5 == answer5

    test6 = Solution().mergeTwoLists(list_to_listnode([-3]), list_to_listnode([-4, -2, 6, 10]))
    answer6 = list_to_listnode([-4, -3, -2, 6, 10])
    assert test6 == answer6

    test7 = Solution().mergeTwoLists(list_to_listnode([-3]), list_to_listnode([10]))
    answer7 = list_to_listnode([-3, 10])
    assert test7 == answer7

    test8 = Solution().mergeTwoLists(list_to_listnode([-3]), list_to_listnode([]))
    answer8 = list_to_listnode([-3])
    assert test8 == answer8


if __name__ =='__main__':
    main()
