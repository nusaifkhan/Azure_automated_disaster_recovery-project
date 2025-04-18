import unittest
from python_scripts.backup_creator import create_snapshot

class TestBackup(unittest.TestCase):
    def test_create_snapshot(self):
        try:
            # Run the snapshot creation function
            create_snapshot("myResourceGroup", "myVM", "testSnapshot")
            result = True
        except Exception as e:
            print(f"Error: {e}")
            result = False
        
        # Assert that the result is True
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
# This test checks if the snapshot creation function runs without errors.
# It does not check the actual creation of the snapshot, as that would require
# integration with Azure services and proper authentication.        