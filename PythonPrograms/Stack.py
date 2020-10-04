class MyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    # Dobbel lenket liste

    def __init__(self, data):
        self._size = 0
        self._head = None
        self._tail = None

        self.header = None
        self._data = data
        self._next = None
        self._previous = None

    def __getitem__(self, index):
        index = self._size + index if index < 0 else index
        if 0 <= index < self._size:
            for i, item in enumerate(self):
                if i == index:
                    return item
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, item):
        index = self._size + index if index < 0 else index
        if 0 <= index < self._size:
            i = 0
            node = self._head
            while i < index:
                node = node._next
                i += 1
            node._value = item
        else:
            raise IndexError('list assignment index out of range')

    def __add__(self, list):
        if isinstance(list, MyNode):
            if self.head is None:
                self.head = list
                list.previous = None
                list.next = None
                self.tail = list
            else:
                self.tail.next = list
                list.previous = self.tail
                self.tail = list
        return

    def __delitem__(self, index):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == index:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.item == index:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == index:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == index:
                n.pref.nref = None
            else:
                print("Element not found")

    def __eq__(self, other):
        current_self = self
        current_other = other
        while type(current_self) is type(current_other) and \
                current_self and current_other and \
                current_self.value == current_other.value:
            current_self = current_self.next_
            current_other = current_other.next_
        if not current_self and not current_other:
            return True
        else:
            return False

    def __iter__(self):
        self.current = self.header
        return self

    def __len__(self):
        return self._size

    def __contains__(self, m):
        if self._data:
            return True

    def __str__(self):
        if self._data:
            return self._data.__str__()
        else:
            return 'Empty Node'

    def append(self, value):
        n = MyNode(value)

        if self.tail is None:
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            n.prev = self.tail
            self._tail = n
        self._size += 1

    def insert(self, index, item):
        if index is None:
            print("This node doesn't exist")
            return


def insert(self, item, index):
    if self._previous is None:
        print("The given previous node cannot be NULL")
        return

    new_node = MyNode()

    # 4. Make net of new node as next of prev node
    new_node.next = prev_node.next

    # 5. Make prev_node as previous of new_node
    prev_node.next = new_node

    # 6. Make prev_node ass previous of new_node
    new_node.prev = prev_node

    # 7. Change previous of new_nodes's next node
    if new_node.next is not None:
        new_node.next.prev = new_node
