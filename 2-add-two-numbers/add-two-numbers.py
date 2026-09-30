# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        count=0
        Sum=0
        Sum1=0
        while(l1 or l2):
            if l2:
                Sum1+=l2.val*10**count
                l2=l2.next
            if l1:
                Sum+=l1.val*10**count
                l1=l1.next
            count+=1
        Sum=str(Sum1+Sum)
        for i , num in enumerate(Sum):
            if i == 0:
                L=ListNode(int(num))
            else:
                L=ListNode(int(num),L)
        return L


        