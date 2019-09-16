# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        number1 = str()
        number2 = str()
        
        while l1 != None:
            number1 = '{}{}'.format(l1.val,number1)
            l1 = l1.next
        
        while l2 != None:
            number2 = '{}{}'.format(l2.val,number2)
            l2 = l2.next
        
        
        temp_root = ListNode(0)
        final_answer_ll = temp_root
        
        for number in str(int(number1) + int(number2))[::-1]:
            final_answer_ll.next = ListNode(number)
            final_answer_ll = final_answer_ll.next
        
        return temp_root.next