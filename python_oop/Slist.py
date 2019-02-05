class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self, msg=""):
        runner = self.head               
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
    
    def remove_node(self, val):
        if self.head != None:
            current_node = self.head
        if self.head.value == val: 
            self.head.next.prev = None
            self.head = self.head.next
    #can't figure out middle?#
        elif self.tail.value == val:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            while current_node.next.value != val
            currernt_node = current_node.next
            if currrent_node.next.value != val:
                print "value not in the list"
                return False

    def insert_node_after(self,val,insert_val):
        if self.head != None:
            current_node = self.head
            new_node = Node(insert_val)

        if self.head.value == val:
            self.head.next.prev = new_node
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next = new_node

        elif self.tail.value == val:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        #now traverse#
        else:
            while current_node.value != val:
                current_node = current_node.next
                if current_node.value != val:
                    print"value not in the list"
                    return False




            

      
print("\n")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Attempt 1")



# Part 2 - implement removeNode(val)
# Implement removeNode(val) where it removes a node with the value val.  For example list.removeNode(5) 
# will see if there's a node with the value of 5.  If it is, it will remove that from the linked list.  
# When you do this, you'll need to consider the following cases:
# when the node you want to remove is in the beginning of the linked list
# when the node you want to remove is in the middle of the linked list
# when the node you want to remove is at the end of the linked list
# For each of these cases, you will probably need to have different logics to handle the removal.
#
#  Part 3***** (optional)**** - Implement insertNode(val, index)
# Implement InsertNode(val, index), which insert a new node of value 'val' on the specified index.  
# For example, for a linked list with the value of 5 -> 3 -> 1, performing insertNode(7, 2) 
# would insert a Node of value 7 at its 2nd index, making the node 5 -> 3 -> 7 -> 1.

# Please make sure that this method allows you to insert a new node as the first node in the list 
# (if index is 0), anywhere in the middle of the list, or at the end of the list 
# (if the specified index is at the end of the list).