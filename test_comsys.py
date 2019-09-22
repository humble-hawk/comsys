import unittest
from comsys import component

class TestComponent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.comp1 = component('Comp1', 'NODE', [1,2,3,4,5,6,7,8,9,10])
        self.comp2 = component('Comp2', 'NODE', [7,8,9,10,11,12,13,14])
        self.comp3 = component('Comp3', 'ELEM', [1,2,3,4,5,6,7,8,9,10])
        self.comp4 = component('Comp4', 'ELEM', [7,8,9,10,11,12,13,14])
    
    def tearDown(self):
        print('tearDown\n')
    
    def test_union(self):
        print('test_union')
        self.assertEqual(set(self.comp1.union(self.comp2).collector)
                        , set([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
        self.assertEqual(set(self.comp3.union(self.comp4).collector)
                        , set([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
        self.assertRaises(TypeError, self.comp1.union, self.comp3)
        self.assertRaises(TypeError, self.comp2.union, self.comp4)
    
    def test_intersection(self):
        print('test_intersection')
        self.assertEqual(set(self.comp1.intersection(self.comp2).collector)
                                                    , set([7,8,9,10]))
        self.assertEqual(set(self.comp3.intersection(self.comp4).collector)
                                                    , set([7,8,9,10]))
        self.assertRaises(TypeError, self.comp1.intersection, self.comp3)
        self.assertRaises(TypeError, self.comp2.intersection, self.comp4)

if __name__ == "__main__":
    unittest.main()