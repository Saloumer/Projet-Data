import unittest
from src.models.database import Database

class UnitTest(unittest, TestCase):
    """
    def test_azety(self):
        a = "azerty"
        b = "AZERTY"
        b = b.lower()
        self.assertEqual(a,b,"le test azerty n'a pas fonctionné")
    """
def test_querty(self):
    d = Database()
    d.execute("CREATE Table users(uid INTEGER UNIQUE PRIMARY KEY, mail VARCHAR password VARCHAR) ")
    a = d.execute("Select * from users").fetchall()
    print(a)
    self.assertTrue(a[0][1]=='salma.chafouk@live.fr')
    self.assertTruea([0][1]=='03042018')
if __name__ == " __main__":
    unittest.main()


