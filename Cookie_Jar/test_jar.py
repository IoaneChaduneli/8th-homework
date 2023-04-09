import unittest
from jar import Jar 

class TestJar(unittest.TestCase):

    def test_init(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)
        self.assertEqual(jar.size,0)

    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)
        jar.deposit(2)
        self.assertEqual(jar.size,7)

        with self.assertRaises(ValueError):
            jar.deposit(-2)

        with self.assertRaises(ValueError):
            jar.deposit(30)

    
    def test_withdraw(self):
        jar = Jar()
        jar.deposit(10)
        jar.withdraw(2)
        self.assertEqual(jar.size, 8)
        
        
        with self.assertRaises(ValueError):
            jar.withdraw(-2)

        with self.assertRaises(ValueError):
            jar.withdraw(11)


    def test_str_representation(self):
        jar = Jar()
        jar.deposit(4)
        self.assertEqual(str(jar), "🍪🍪🍪🍪")


if __name__ == '__main__':
    unittest.main()