#create Linked lists

#Node creation class
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
            print current.data
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

my_list.insert_node('Mohan')
my_list.insert_node('kumar')
my_list.insert_node('t')
my_list.print_list()
#print((my_list.search('kwewumar')).data)
print(my_list.list_size())
my_list.delete_node('Mohan')
my_list.print_list()

