from __future__ import division
import random
from graphviz import Digraph
from distlib.compat import raw_input


# KODE FRA LÆREREN. JEG SKJØNNER IKKE HVORDAN JEG SKAL GÅ FRAM. LAGE EN NODE OG LESE MIN STRENG INNI DEN?
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


"""leftNode = MyBinaryNode('+', MyBinaryNode('a'), MyBinaryNode('b'))
rightNode = MyBinaryNode('-', MyBinaryNode('a'), MyBinaryNode('b'))
rootNode = MyBinaryNode('*', leftNode, rightNode)"""
# ----------------------------------------------------------------
# KODE FRA INTERNET SOM FUNGERER

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def infix_to_postfix(formula):
    stack = []  # only pop when the coming op has priority
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: output += stack.pop()
    print(output)
    return output


def postfix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in formula:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            if prev_op and len(a) > 1 and PRIORITY[ch] > PRIORITY[prev_op]:
                # if previous operator has lower priority
                # add '()' to the previous a
                expr = '(' + a + ')' + ch + b
            else:
                expr = a + ch + b
            stack.append(expr)
            prev_op = ch
    print(stack[-1])
    return stack[-1]


def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(ch)

            # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)
    print(exp_stack[-1])
    return exp_stack[-1]


def prefix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in reversed(formula):
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if prev_op and PRIORITY[prev_op] < PRIORITY[ch]:
                exp = '(' + a + ')' + ch + b
            else:
                exp = a + ch + b
            stack.append(exp)
            prev_op = ch
    print(stack[-1])
    return stack[-1]


def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[ch]
            stack.append(c)
    print(stack[-1])
    return stack[-1]


def evaluate_infix(formula):
    return evaluate_postfix(infix_to_postfix(formula))


def evaluate_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps) - 2):
            if exps[i] in OPERATORS:
                if not exps[i + 1] in OPERATORS and not exps[i + 2] in OPERATORS:
                    op, a, b = exps[i:i + 3]
                    a, b = map(float, [a, b])
                    c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[op]
                    exps = exps[:i] + [c] + exps[i + 3:]
                    break
        print(exps)
    return exps[-1]


# ----------------------------------------------------------------
if __name__ == '__main__':
    # prefixFromInput = str(raw_input("Please enter a prefix expression, comma separated: "))
    prefixFromInput = ['+', '+', '*', '4', '5', '6', '7']

    # disse fungerer på kode fra internett
    infix = prefix_to_infix(prefixFromInput)
    postfix = infix_to_postfix(infix)

    print("The infix form is: ", prefix_to_infix(prefixFromInput))
    print("The postfix form is: ", infix_to_postfix(prefix_to_infix(prefixFromInput)))
    print("The result is: ", evaluate_prefix(prefixFromInput))

    # disse fungerer ikke, kode fra lærer
    #print(prefixOrder(prefixFromInput))
