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
    def remove_duplicates(self):
        #temp list to store data elements adnd check their existence
        dup_list = list()
        previous = self.head
        current = self.head
        #loop over linked list
        while current:
            found = False
            #import pdb;pdb.set_trace()
            for i in range(len(dup_list)):
                #print("Mohan")
                if current.data == dup_list[i]:
                    found = True
                    break
            if not found:
                dup_list.append(current.data)
                previous = current
                current = current.next_node
            else:
                previous.next_node = current.next_node
                current = previous.next_node

    def remove_duplicates_nospace(self):
        current = self.head
        while current:
            runner = current.next_node
            previous_runner = current
            while runner:
                if runner.data == current.data:
                    previous_runner.next_node = runner.next_node
                    runner = previous_runner.next_node
                else:
                    previous_runner = runner
                    runner = runner.next_node
            current = current.next_node

my_list = LinkedList()

for i in range(5):
    i = raw_input("Enter data:" )
    my_list.insert_node(int(i))

my_list.print_list()
#my_list.remove_duplicates()
my_list.remove_duplicates_nospace();
my_list.print_list()

