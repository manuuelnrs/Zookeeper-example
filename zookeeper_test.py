from ast import Delete
import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    #UnitTests @author Juan Manuel Nava Rosales
    def test_eliminar_znode_root(self):
        tree = Ztree()
        self.assertTrue( tree.exist('/') )
        
        with self.assertRaises(Exception):
            tree.delete('/', 0)

    def test_eliminar_znode_efimero_sinServicio(self):
        tree = Ztree()
        tree.create('/node1', 'data1', True, True, 10, '/')
        tree.create('/node2', 'data2', True, False, 10, '/node1')
        self.assertFalse( tree.delete('/node2', 0) ) # return 0!!
    
    def test_cambiarDato_znode(self):
        tree = Ztree()
        tree.create('/node1', 'data1', False, True, 0, '/')
        tree.setData('/node1', 'changed data')
        self.assertEqual( tree.getData('/node1'), 'changed data')

    def test_crear_znode_padre_noexiste(self):
        tree = Ztree()
        with self.assertRaises(Exception):
            tree.create('/node2', 'data2', True, True, 0, '/node1')

    def test_buscar_znode(self):
        tree = Ztree()
        tree.create('/node1', 'data1', False, False, 10, '/')
        tree.create('/node2', 'data1_2', True, True, 10, '/node1')
        tree.create('/node3', 'data2_3', True, False, 10, '/node2')
        tree.create('/node4', 'data3_4', True, True, 10, '/node3')
        self.assertTrue( tree.exist('/node4') )


if __name__ == '__main__':
    unittest.main()

