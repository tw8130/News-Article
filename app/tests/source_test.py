import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('bbc-news','BBC News','Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    

if__name__== '__main__':
    unittest.main()