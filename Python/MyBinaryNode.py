class MyBinaryNode:
    def __init__(self, value, lefttree=None, righttree=None):
        self.value = value
        self.lefttree = lefttree
        self.righttree = righttree

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, lefttree):
            self.__left = lefttree

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, righttree):
            self.__right = righttree

        def __eq__(self, node):
            if node == None:
                return False
            elif not isinstance(node, MyBinaryNode):
                raise Exception("Equality are only for object og equal types")
            else:
                return self.value == node.value

        def __str__(self):
            return self.value

        def hasRight(self):
            return self.right != None

        def hasLeft(self):
            return self.left != None

        def info(self):
            retval = self.value + " : ( "
            if isinstance(self.left, MyBinaryNode):
                retval += self.left.value
            else:
                retval += "none"
            retval += " , "
            if isinstance(self.right, MyBinaryNode):
                retval += self.right.value + " )"
            else:
                retval += "none )"
            return retval


leftNode = MyBinaryNode('+', MyBinaryNode('a'), MyBinaryNode('b'))
rightNode = MyBinaryNode('-', MyBinaryNode('a'), MyBinaryNode('b'))
rootNode = MyBinaryNode('*', leftNode, rightNode)


def prefixOrder(self):
    print(self, ' ', end='')
    if self.hasLeft():
        self.left.prefixOrder()
    if self.hasRight():
        self.right.prefixOrder()


def infixOrder(self):
    if self.hasLeft():
        self.left.infixOrder()
    print(self, ' ', end='')
    if self.hasRight():
        self.right.infixOrder()


def postfixOrder(self):
    if self.hasLeft():
        self.left.postfixOrder()
    if self.hasRight():
        self.right.postfixOrder()
    print(self, ' ', end='')


def levelOrder(self):
    from queue import SimpleQueue
    FIFOQueue = SimpleQueue()
    FIFOQueue.put(self)
    self.levelOrderEntry(FIFOQueue)
    while not FIFOQueue.empty():
        node = FIFOQueue.get()
        print(node, " ", end='')


def levelOrderEntry(self, queue):
    if queue.empty():
        return
    node = queue.get()
    print(node, " ", end='')
    if node.hasLeft():
        queue.put(node.left)
    if node.hasRight():
        queue.put(node.right)
    if node.hasLeft() or node.hasRight:
        self.levelOrderEntry(queue)
