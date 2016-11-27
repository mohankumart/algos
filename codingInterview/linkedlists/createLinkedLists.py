#create Linked lists

#Node creation class
import sys

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def print_data():
        print(self.data)



#LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_node(self, data):
        new_node = Node(data,self.head)
        self.head = new_node
    def print_list(self):
        current = self.head
        while current:
            if current.next_node:
                sys.stdout.write(str(current.data) + '---->')
            else:
                sys.stdout.write(str(current.data) + '\n')
            current = current.next_node
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if data == current.data:
                found = True
                break
            else:
                current = current.next_node
        if current is None:
            raise ValueError('Data does not exists')
        else:
            return current
    def list_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    def delete_node(self, data):
        current = self.search(data)
        previous = self.head
        while (previous.next_node).data != data:
            previous = previous.next_node
        previous.next_node = current.next_node
        current.next_node = None




my_list = LinkedList()
for i in range(10):
    my_list.insert_node(i)
my_list.print_list()


