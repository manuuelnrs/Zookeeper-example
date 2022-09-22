# Tarea

Escribir pruebas de unidad para Zookeeper

Este repositorio requiere `treelib`, asi que instalarlo:

```bash
pip install treelib
```

De ahi, pueden tomar el archivo `zookeeper_test.py` y agregar
pruebas.

Las pruebas deben utilizar los metodos `assert` que estan incluidos
en la clase `TestCase`.

Liga: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

Por ejemplo:

```
class TestZookeeper(unittest.TestCase):
  def test_simple_node(self):
    tree = Ztree()
    tree.create_node('/node1', 'mydata', ....)
    self.assertEqual(tree.getData('/node1'), 'mydata')
```

**Para correr las pruebas**, simplemente es necesario correr el archivo
de pruebas:

```bash
python zookeeper_test.py
```
