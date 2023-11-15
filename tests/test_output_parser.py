import sys
# setting path
# print(sys.path)

import unittest
from output_parser import OutputParser

class testOutputParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.text = '**Option 1:** {"action": "Look Up Graph", "action_input": "https://www.google.com/search?q=graph"}'


        cls.parsed_text = '{"action": "Look Up Graph", "action_input": "https://www.google.com/search?q=graph"}'
                    
    
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_parsing(self) -> None:

        result = OutputParser.parse(text=self.text)
        print(result.log)
        self.assertEquals(result.log, self.parsed_text)

if __name__ == '__main__':
    unittest.main()