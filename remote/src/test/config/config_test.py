""" 
config_test.py: Config test class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
sys.path.append('../')
from config.config import Nors_Configuration

import unittest


class Test_Config(unittest.TestCase):
    def setUp(self):
        pass

    def test_config_read_content(self):
        self.assertEqual(config.ReadConfig('main_section', 'par1'), '10' )
        self.assertEqual(config.ReadConfig('main_section', 'par2'), 'test parameter' )
        self.assertEqual(config.ReadConfig('other_section', 'par3'), "{'asd':'der'}" )
        self.assertEqual(config.ReadConfig('wrong_section', 'parWrong'), None )

    def test_config_write_content(self):
        value = config.ReadConfig('new_section', 'new_par')
        self.assertEqual(value,'old_value')
        config.SaveConfig('new_section', 'new_par' , 'new_value')
        self.assertEqual(config.ReadConfig('new_section', 'new_par'), 'new_value' )
        
        # restoring last state
        config.SaveConfig('new_section', 'new_par' , 'old_value')
        self.assertEqual(config.ReadConfig('new_section', 'new_par'), 'old_value' )

    def tearDown(self):
        pass
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg1 = sys.argv.pop()
        arg2 = sys.argv.pop()
    config = Nors_Configuration()
    unittest.main()
    