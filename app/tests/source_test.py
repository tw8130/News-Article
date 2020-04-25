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
        self.new_source = Source('bbc-news','BBC News','Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories','"http://www.bbc.co.uk/news"','general')

    def test_instance(self):
        '''
        Test case to check if self.news_source is an instance of Source
        '''
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        Test case to check if source class is initialized
        '''
        self.assertEqual(self.new_source.id, 'bbc-news')
        self.assertEqual(self.new_source.name,'BBC News')
        self.assertEqual(self.new_source.description,'Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories')
    

if__name__== '__main__':
    unittest.main(verbosity=2)