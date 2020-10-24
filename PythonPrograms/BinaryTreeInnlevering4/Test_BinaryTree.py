import unittest
from collections import namedtuple
from PythonPrograms.BinaryTreeInnlevering4.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering4.BinaryTreeNode import BinaryTreeNode


class Test_BinaryTree(unittest.TestCase):
    def setUp(self):
        self.personer = []
        self.person = namedtuple('person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
        list_personer = ["AGA;ALI HAIBEH;LARS 97;6879;SOLVORN",
                         "AKSELSEN;MORTEN DAGFINN;SLUSEVEGEN 32;0386;OSLO",
                         "ALFREDSEN;MARIELLE;SØTEREN NEDRE 98;2007;KJELLER",
                         "ARNASON;HANS EDVARD;KRINGSTADVEGEN 32;4069;STAVANGER",
                         "ASAIPPILLAI;JO GUDBRAND;BERGERUD 68;4371;EGERSUND",
                         "DALLAGER;MARIA;AARVOLD 116;5522;HAUGESUND",
                         "EVJEN;LENA;ÅKERHAUGEN 29;3678;NOTODDEN",
                         "HEITMANN;PER-GUNNAR;ELVATUNET 45;8483;ANDENES",
                         "HØGBAKK;HELENA;SKJERVOLDSTEIGEN 98;5105;EIDSVÅG",
                         "KAROLIUS;BÅRD-VIDAR;ØVERLI 4;1388;BORGEN",
                         "KJØPSNES;CAMILLA;GRANDMO 35;6977;BYGSTAD",
                         "NØSTAHL;MARIUS BJUGN;SOMMERSTUBAKKEN 110;6085;LARSNES",
                         "LYNGØY;KARIANN;WALLEY 35;9616;HAMMERFEST",
                         "RØNNING;KIRUPANITHY;BØ GARD 66;6953;LEIRVIK I SOGN",
                         "SAKARIASSEN;SICKAN;OLABORG 89;6882;ØVRE ÅRDAL",
                         "SINNATHAMBY;ANN-KARIN;GULLSTJERNEVEIEN 117;2857;SKREIA",
                         "SIVAKUMAR;GEIR-KYRRE;RUBO 85;4352;KLEPPE",
                         "STORLIEN;HANS-MAGNUS;TALLSLETTA 57;3849;VRÅLIOSEN",
                         "TRAN QUYEN;RIGMOR;ØYENG 91;1812;ASKIM",
                         "TOLLEFSEN;ZULFIQAR ALI;EIRIK JARLS GATE 79;1305;HASLUM",
                         "VERIASKINE;MARINA;ROTLI 73;8641;HEMNESBERGET",
                         "WIKLEM;WIKLEM;EIDSTUN 119;6592;LEIRA PÅ NORDMØR"]
        for line in list_personer:
            p = line.strip("\n").split(";")
            p1 = self.person(p[0], p[1], p[2], p[3], p[4])
            self.personer.append(p1)

        self.binaryTree = BinaryTree()
        for person in self.personer:
            self.binaryTree.insert(value=person)

        #print(self.binaryTree.findLeftMost().value)

    def test_findLeftMost(self):
        mostLeftValue = self.person('AGA', 'ALI HAIBEH', 'LARS 97', '6879', 'SOLVORN')
        mostLeftValue_node = BinaryTreeNode(mostLeftValue)
        self.assertEqual(mostLeftValue_node, self.binaryTree.findLeftMost(treenode=self.binaryTree._root))

    def test_findMin(self):
        minimum_value = self.person('AGA', 'ALI HAIBEH', 'LARS 97', '6879', 'SOLVORN')
        node = BinaryTreeNode(minimum_value)

        self.assertEqual(node, self.binaryTree.findMin())

    def test_findRightMost(self):
        mostRightValue = self.person('WIKLEM', 'WIKLEM', 'EIDSTUN 119', '6592', 'LEIRA PÅ NORDMØR')
        mostRightValue_node = BinaryTreeNode(mostRightValue)
        self.assertEqual(mostRightValue_node, self.binaryTree.findRightMost(treenode=self.binaryTree._root))

    def test_findMax(self):
        maximum_value = self.person('WIKLEM', 'WIKLEM', 'EIDSTUN 119', '6592', 'LEIRA PÅ NORDMØR')
        node = BinaryTreeNode(maximum_value)

        self.assertEqual(node, self.binaryTree.findMax())

    def test_find(self):
        value = self.person('RØNNING', 'KIRUPANITHY', 'BØ GARD 66', '6953', 'LEIRVIK I SOGN')
        node = BinaryTreeNode(value)

        self.assertEqual(node, self.binaryTree.find(value))

    def test_insert(self):
        value = self.person('KESER', 'HALIL IBRAHIM', 'Strømmen 007', '2010', 'Strømmen')
        node = BinaryTreeNode(value)
        self.binaryTree.insert(value=value)

        value1 = self.person('HANSEN', 'JØRGEN', 'Maura 007', '2450', 'Maura')
        node1 = BinaryTreeNode(value1)  # this one not inserted

        self.assertEqual(node, self.binaryTree.find(value))
        self.assertNotEqual(node1, self.binaryTree.find(value1))

    def test_deleteMin(self):
        minimum = self.person('AGA', 'ALI HAIBEH', 'LARS 97', '6879', 'SOLVORN')
        node = BinaryTreeNode(minimum)

        self.assertEqual(node, self.binaryTree.find(minimum))
        self.binaryTree.deleteMin()
        self.assertEqual(None, self.binaryTree.find(minimum))

    def test_deleteMax(self):
        maximum = self.person('WIKLEM', 'WIKLEM', 'EIDSTUN 119', '6592', 'LEIRA PÅ NORDMØR')
        node = BinaryTreeNode(maximum)

        self.assertEqual(node, self.binaryTree.find(maximum))
        self.binaryTree.deleteMax()
        self.assertEqual(None, self.binaryTree.find(maximum))

    def test_delete(self):
        value = self.person('ALFREDSEN', 'MARIELLE', 'SØTEREN NEDRE 98', '2007', 'KJELLER')
        node = BinaryTreeNode(value)

        self.assertEqual(node, self.binaryTree.find(value))
        self.binaryTree.delete(value)
        self.assertEqual(None, self.binaryTree.find(value))


if __name__ == "__main__":
    import sys

    sys.argv = ['', 'Test_BinaryTree']
    unittest.main()
    exit(Test_BinaryTree)
