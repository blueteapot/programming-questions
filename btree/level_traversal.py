from btree import Node, Tree

def level_traversal(root):
    queue = [root]
    level = 0

    while len(queue) > 0:
        level+= 1
        size = len(queue)
        print("level = ", level)
        while size > 0:
            node = queue.pop(0)
            print(node.v)
            if node.l:
                queue.append(node.l)
            if node.r:
                queue.append(node.r)

            size -= 1

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

level_traversal(tree.getRoot())
