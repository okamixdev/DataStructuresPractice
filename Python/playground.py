class Node:
    def __init__(self, data: None, next: None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_root(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        stringList = ""
        itr = self.head

        print()
        while itr:
            stringList += itr.data + " --> "
            itr = itr.next

        stringList += "|null|"
        print(stringList)
        print()

    def insert(self, data):

        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def pop(self):

        itr = self.head
        count = 0
        while itr.next:
            if count == self.getLength() - 2:
                temp = itr.next.data
                itr.next = None
                return temp
            count += 1
            itr = itr.next

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_root("Carlos")
    ll.insert_root("Ceniza")
    ll.insert_root("Arder")
    ll.insert_root("Informe")
    ll.insert_root("Forense")
    ll.insert("Eternidad")
    ll.insert("Eter")

    ll.print()
    print(ll.pop())
    ll.print()
