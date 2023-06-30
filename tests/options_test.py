import unittest
from shared.options_enum import Options

class OptionsTestClass(unittest.TestCase):

    def test_assertCreateCode(self):
        expectedCreateValue = 1

        createValue = Options.CREATE.value

        self.assertEqual(expectedCreateValue, createValue)
    
    def test_assertGetOneCode(self):
        expectedGetOneValue = 2

        getOneValue = Options.GETONE.value

        self.assertEqual(expectedGetOneValue, getOneValue)
    
    def test_assertGetAllCode(self):
        expectedGetAllValue = 3

        getAllValue = Options.GETALL.value

        self.assertEqual(expectedGetAllValue, getAllValue)
    
    def test_assertDeleteOneCode(self):
        expectedDeleteOneValue = 4

        deleteOneValue = Options.DELETEONE.value

        self.assertEqual(expectedDeleteOneValue, deleteOneValue)
    
    def test_assertExitCode(self):
        expectedExitValue = 5

        exitValue = Options.EXIT.value

        self.assertEqual(expectedExitValue, exitValue)
    
if __name__ == "__main__":
    unittest.main()