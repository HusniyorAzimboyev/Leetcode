class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            sum = sum % 10
            current.next = ListNode(sum)
            current = current.next
        
        return dummy.next
print(addTwoNumbers(ListNode(3, ListNode(1, ListNode(2))),ListNode(3, ListNode(1, ListNode(2)))))
