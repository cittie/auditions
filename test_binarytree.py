import binarytree as bt
import unittest

class BTreeFunctionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.btree = bt.BinaryOrderedTree()
        self.root = self.btree.addNode(23)
        
        elements = [7, 22, 14, 25, 33, 18, 9, 4, 73, 21]

        for ele in elements:
            self.btree.insert(self.root, ele)
            
        self.btree.printTree(self.root)

        
    def test_binarytree_functions_from_root(self):
        
        true_data = 18
        false_data = 255
        
        result = self.btree.lookup(self.root, true_data)
        self.assertEqual(result, True)
        
        result = self.btree.lookup(self.root, false_data)
        self.assertEqual(result, False)
        
        minValue = self.btree.minValue(self.root)
        self.assertEqual(minValue, 4)
                
        maxDepth = self.btree.maxDepth(self.root)
        self.assertEqual(maxDepth, 6)
        
        size = self.btree.size(self.root)
        self.assertEqual(size, 11)
        