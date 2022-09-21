from treelib import Node,Tree


tree = Tree()
tree.create_node("hola1",1)
tree.create_node("hola2",2, parent= 1)
tree.create_node("hola3",3, parent= 1)
tree.create_node("hola4",4, parent= 2)
tree.show()
