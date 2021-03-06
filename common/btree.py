class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    def __repr__(self):
        return str(self.val)

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def remove(self, val):
        _remove(self, val, self.root)

    def _remove(self, val, node):
        if node == None:
            return None

        if node.v < val:
            node.l = _remove(self, val, node.l)

        elif node.v > val:
            node.r = _remove(self, val, node.r)

        else:
            if node.l == None:
                return node.r
            if node.r == None:
                return node.l

            


    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def height(self):
        if self.root == None:
            return 0
        return self._height(self.root)

    def _height(self, node):
        l_val = 0 if node.l == None else self._height(node.l)
        r_val = 0 if node.r == None else self._height(node.r)

        return 1 + max(l_val, r_val)

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
