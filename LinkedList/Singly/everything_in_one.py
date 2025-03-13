class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def append(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("NOne")
    def sortadd(self,data):
        new=Node(data)
        if not self.head or self.head.data>data:
            new.next=self.head
            self.head=new
            return
        current=self.head
        while current.next and current.next.data<data:
            current=current.next
        new.next=current.next
        current.next=new
    def begin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def specifylast(self,data,place):
        new=Node(data)
        if not self.head:
            print("The list is empty.")
            return
        if self.head.data==place:
            new.next=self.head.next
            self.head.next=new
            return
        current=self.head
        while current.next:
            if current.data==place:
                new.next = current.next
                current.next = new
                return
            current=current.next
        print(f"Node with data '{place}' not found.")
    def specifyfirst(self,data,place):
        new=Node(data)
        if not self.head:
            print("The list is empty.")
            return
        if self.head.data==place:
            new.next=self.head
            self.head=new
            return
        current=self.head
        while current.next:
            if current.next.data==place:
                new.next=current.next
                current.next=new
                return
            current=current.next
        print(f"Node with data '{place}' not found.")
    def delete(self,data):
        if not self.head:
            print("The list is empty.")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next:
            if temp.next.data==data:
                temp.next=temp.next.next
                return
            temp=temp.next
        print(f"Node with data '{data}' not found.")
    def deletefirst(self):
        if not self.head:
            print("its empty")
            return
        if self.head:
            self.head=self.head.next
            return
    def deletelast(self):
        if not self.head:
            print("its empty")
            return
        if self.head.next==None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def reverse(self):
        temp=self.head
        prev=None
        while temp:
            new=temp.next
            temp.next=prev
            prev=temp
            temp=new
        self.head=prev
    def lister(self):
        arr=[]
        temp=self.head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        return arr
    def middle(self):
        slow=self.head
        fast=self.head
        while fast.next and fast:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    def palindrome(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        temp=slow
        prev=None
        while temp:
            new=temp.next
            temp.next=prev
            prev=temp
            temp=new

        first=self.head
        second=prev
        while second:
            if first.data!=second.data:
                return False
            first=first.next
            second=second.next
        return True
        
    def delete_middle(self):
        if not self.head or not self.head.next:
            print("The list is too short to delete the middle.")
            return
        
        slow = self.head
        fast = self.head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = slow.next

ob=single()
ob.append(34)
ob.append(45)
ob.append(22)
ob.append(22)
ob.sortadd(12)
ob.sortadd(13)
ob.begin(23)
ob.begin(89)
ob.begin(56)
ob.specifylast(182,56)
ob.specifylast(2344,45)
ob.specifyfirst(21,56)
ob.specifyfirst(465,22)
ob.delete(12)
ob.delete(22)
ob.deletefirst()
ob.deletelast()
ob.reverse()
ob.display()
ob.delete_middle()
print(ob.lister())
print(ob.middle())
print(ob.palindrome())

