import unittest

class user:
    def __init__(self, name, address, phoneNo):
        self.name = name
        self.address = address
        self.phoneNo = phoneNo

    def returnName(self):
        return self.name
    
    def returnAddress(self):
        return self.address
    
    def returnNumber(self):
        return self.phoneNo


class testingUser(unittest.TestCase):
    def setUp(self):
        self.user_file = user("Souvik", "20/1/A BDC Lane", 8450042512)

    def test_returnName(self):
        self.assertEqual("Souvik",self.user_file.returnName())

    def test_returnAddress(self):
        self.assertEqual("20/1/A BDC Lane",self.user_file.returnAddress())

    def test_returnNumber(self):
        self.assertEqual(8450042512,self.user_file.returnNumber())


if __name__ == "__main__":
    unittest.main()