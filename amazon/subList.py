#Node Class

class Node:

    def _init_(self, value=None):
        self.value = value
        self.next = None
        return

    def isempty(self):
        return self.value == None

# Link List
class Linkl():
    # Initializing head & Tail
    def _init_(self):
        self.head = None
        self.tail = None

    # Cheacking for Emptyness
    def isempty(self):
        return self.head == None

    # PUsh_HEAD:- Adding element in head of Link list
    def PUSH_HEAD(self, itemName):
        import pdb
        pdb.set_trace()
        curr = self.head
        self.head = Node(itemName)
        self.head.next = curr

    # PUsh_TAIL:- Adding element in END of Link list        
    def PUSH_TAIL(self, itemName):
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = Node(itemName)

    # POP_HEAD:- Remuving element from head of Link list
    def POP_HEAD(self):
        if self.isempty():
            return 'List is Alredy Empty'
        else:   
            curr = self.head
            self.head = self.head.next
            curr = None
        
    # Displaying Result(Link List)
    def _str_(self):
        curr = self.head
        while(curr.next != None):
            print(str(curr.value))
            curr = curr.next
        return str(curr.value)

l=Linkl()
l.PUSH_HEAD('CUP')
l.PUSH_HEAD('PEN')
l.PUSH_TAIL('FAN')
l.PUSH_HEAD('JAM')
l.POP_HEAD()
l.POP_HEAD()

#Printing
print(l)
