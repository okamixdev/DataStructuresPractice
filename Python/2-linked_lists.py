# Linked Lists
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_root(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert(data)

    def removeAt(self, idx):
        if idx < 0 or idx >= self.getLenght():
            raise Exception("Invalid Index")

        if idx == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

        itr = itr.next

    def insertAt(self, idx, data):
        if idx < 0 or idx > self.getLenght():
            raise Exception("Invalid Index")

        if idx == 0:
            self.insert_root(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                temp = itr.next
                itr.next = Node(data, temp)
                break

            count += 1
            itr = itr.next

    def print(self):
        if self.head is None:
            print("LinkedList is empty...")
            return

        iterator = self.head
        linkedLString = ""

        print(
            "------------------------------------------------------------------------------------"
        )
        while iterator:
            linkedLString += str(iterator.data) + " --> "
            iterator = iterator.next
        linkedLString += "|null|"
        print(linkedLString)
        print(
            "------------------------------------------------------------------------------------"
        )

    def getLenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def getIndex(self, data):

        if self.getLenght() == 0:
            print("LinkedList is empty")
            return

        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count

            count += 1
            itr = itr.next

    def removeValue(self, data):

        if self.getLenght() == 0:
            print("LinkedList is empty")
            return

        found = False
        itr = self.head
        while itr:
            if itr.next != None and itr.next.data == data:
                itr.next = itr.next.next
                found = True
                break

            itr = itr.next

        if found == False:
            print("NOT FOUND")


if __name__ == "__main__":
    linkedList = LinkedList()
    # linkedList.insert_root(5)
    # linkedList.insert_root(10)

    # linkedList.insert(13)
    # linkedList.insert_root(20)
    # linkedList.insert(23)
    # print(f"Lenght of list: {linkedList.getLenght()}")

    # linkedList.removeAt(2)

    linkedList.insert_values(["pan", "queso", "banana", "carne", "manzana"])
    linkedList.insertAt(2, "( 🙂‍↔️ )")
    linkedList.insertAt(0, "( 🤬 )")

    linkedList.print()

    print(f"Banana Index is at: {linkedList.getIndex("banana")}")

    linkedList.removeValue("queso")
    linkedList.print()
