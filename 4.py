class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    def set_val(self,val):
        self.val=val
    def get_val(self):
        return self.val
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
class SLL:
    def __init__(self):
        self.head=None
    def add_at_head(self,val):
        l=Node(val)
        g=self.head
        if self.head==None:
            self.head=l
            print("Added at head!")
        else:
            l.set_next(self.head)
            self.head=l
            print("Added at head!")
    def add_at_tail(self,val):
        l=Node(val)
        g=self.head
        if self.head==None:
            self.head=l
            print("Added at tail!")
        else:
            e=self.head
            while e.get_next()!=None:
                e=e.get_next()
            e.set_next(l)
            print("Added at tail")
    def add_after_position(self,pos,num):
        l=Node(num)
        g=self.head
        for i in range(1,pos):
            g=g.get_next()
        l.set_next(g.get_next().get_next())
        g.set_next(l)
        print("Added after position!")
    def delete_node(self,val):
        got=False
        r=self.head
        k=r
        while r.get_next()!=None:
            if r.get_val()==val:
                got=True
                k.set_next(r.get_next())
            r=r.get_next()
        if got:
            print("Node Deleted!")
        else:
            print("Node not found!")
    def list_nodes(self):
        e=self.head
        while e!=None:
            print(e.get_val(),end=" ")
            e=e.get_next()
sll=SLL()
class main:
    while True:
        print("\nMENU\n1.Add at head\n2.Display\n3.Add at tail1\n4.Add after position\n5.Delete node\n9.Exit")
        option=int(input('Choose :'))
        if option==1:
            val=int(input("Enter number:"))
            sll.add_at_head(val)
        elif option==2:
            sll.list_nodes()
        elif option==3:
            val=int(input("Enter value:"))
            sll.add_at_tail(val)
        elif option==4:
            pos=int(input("Enter Position:"))
            val=int(input("Enter value:"))
            sll.add_after_position(pos,val)
        elif option==5:
            val=int(input("Enter Node:"))
            sll.delete_node(val)
        else:
            break