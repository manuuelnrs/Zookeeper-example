from turtle import onscreenclick
from treelib import Node,Tree

class Ztree:
    def __init__(self):
        self.tree = Tree()
        self.tree.create_node("/","/")
    
    def get_tree(self):
        return self.tree

    def create(self,path,data,ephemeral,OnService):
        return Znode(path,data,ephemeral,OnService)

    def delete(self,path,version):
        pass




class Znode:
    def __init__(self,path,data,ephemeral,OnService):
        self.path = path
        self.ephemeral = ephemeral
        self.data = data
        self.node = Node(path,path)
        self.OnService = OnService 
        self.version = 0
        self.timeDead = 60
    
    def get_node_info(self):
        print("\t \t------ZNode information--------\t\t \n")
        print("Path = {path} \n".format(path = self.path))
        print("Ephemeral = {ephemeral} \n".format(ephemeral = self.ephemeral))
        print("Version = {version} \n".format(version = self.version))
        print("Data = {data} \n".format(data = self.data))

        
        
        
        
