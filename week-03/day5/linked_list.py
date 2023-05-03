class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, li, l2):
        l1_as_num = llToNum(l1)
        l2_as_num = llToNum(l2)
        total = l1_as_num + l2_as_num

        return numToLL(total)
    
def llToNum(ll):
    sum = 0
    factor = 1
    current = ll
    while(current):
        sum += current.val * factor
        factor *= 10
        current = current.next
    
    return sum

def numToLL(num):
    num_as_ll = ListNode()
    current = num_as_ll

    while num != 0:
        current.val = num % 10
        num = num // 10
        if num != 0:
            current.next = ListNode()
            current = current.next
    return num_as_ll

