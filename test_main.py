import unittest
import main

class TestMain(unittest.TestCase):

    def test_get_platform_runtime_info(self):
        info = main.get_platform_runtime_info()
        self.assertIn("python_version", info)
        self.assertIn("os", info)
        self.assertIn("architecture", info)
        self.assertIn("kernel release", info)
        self.assertIn("full system info", info)
        self.assertIn("platform release", info)
        self.assertIn("container", info)
        self.assertIn("cloud_provider", info)
        self.assertIn("ip_addresses", info)

if __name__ == "__main__":
    unittest.main()
