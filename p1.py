class Node:
    def __init__(self,val):
        self.pre=None
        self.val=val
        self.next=None
    def set_pre(self,pre):
        self.pre=pre
    def get_pre(self):
        return self.pre
    def set_val(self,val):
        self.val=val
    def get_val(self):
        return self.val
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
class Dll:
    def __init__(self):
        self.head=None
    def add_at_head(self,val):
        p=Node(val)
        g=self.head
        if self.head==None:
            self.head=p
        else:
            p.set_next(self.head)
            g.set_pre(p)
            self.head=p
        print("Node added at head!")
    def add_at_tail(self,val):
        l=Node(val)
        if self.head==None:
            self.head=g
        else:
            g=self.head
            while g.get_next()!=None:
                g=g.get_next()
            g.set_next(l)
            l.set_pre(g)
        print("Added at tail!") 
    def add_after_position(self,pos,val):
        v=Node(val)
        l=self.head
        for i in range(1,pos):
            l=l.get_next()
        v.set_next(l.get_next())
        l.get_next().set_pre(v)
        l.set_next(v)
        v.set_pre(l)
        print('Node added after position!')
    def list_nodes(self):       
        if self.head==None:
            print("It's Empty Mowa")
        else:
            l=self.head
            while l!=None:
                    print(l.get_val(),end=' ')
                    l=l.get_next()
dll=Dll()
class main:
    while True:
        print('\nMenu\n1.Add at head\n2.Display\n3.Add at tail\n4.Add after position\n9.Exit')
        option=int(input("Choose the option:"))
        if option==1:
            val=int(input("Enter the value:"))
            dll.add_at_head(val)
        elif option==2:
            dll.list_nodes()
        elif option==3:
            val=int(input('Enter node:'))
            dll.add_at_tail(val)
        elif option==4:
            pos=int(input("Enter Position:"))
            val=int(input("Enter value:"))
            dll.add_after_position(pos,val)
        else:
            exit()