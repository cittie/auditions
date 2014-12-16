import quicksort as qs
import unittest

class FunctionTestCase(unittest.TestCase):
    
    def setUp(self):
        print("Starting unit test...")
        
    def test_quicksort_function(self):
       
        int_list = []
        for i in range(62, 0, -2):
            int_list.append(i)
        sorted_list = sorted(int_list)
        
        self.assertEqual(qs.quickSort(int_list), sorted_list)
        
        float_list = []
        for i in range(62, 0, -2):
            float_list.append(i - 0.02)
        sorted_list = sorted(float_list)
        
        self.assertEqual(qs.quickSort(float_list), sorted_list)
        
        char_list = "Manaburn"
        sorted_list = sorted(char_list)
        
        self.assertEqual(qs.quickSort(char_list), sorted_list)
        
            
    def test_quicksort_special_function(self):
        empty_list = []
        
        self.assertEqual(qs.quickSort(empty_list), empty_list)
        
        single_list = [1]
        
        self.assertEqual(qs.quickSort(single_list), single_list)    