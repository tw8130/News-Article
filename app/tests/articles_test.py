import unittest
from app.models import Articles

class ArticleTest(unitttest.TestCase):
    '''
    Test class to test behaviours of article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Harry Domanski','Samsung`s next smartphone could have a pop-up selfie camera - TechRadar India','Leaked renders show every angle of potential new handset','https://cdn.mos.cms.futurecdn.net/9W2JuazWDRjWaRMUi2dCPc-1200-80.jpg','https://www.techradar.com/news/samsungs-next-smartphone-could-have-a-pop-up-selfie-camera','2020-04-27T03:16:00Z')
    
    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue(isinstance( self.new_article, Articles ))
    
    def test_init(self):
        '''
        Test case to check if the Article class is initialized
        '''

        self.assertEqual( self.new_article.author, 'Harry Domanski')
        self.assertEqual( self.new_article.title, 'Samsung`s next smartphone could have a pop-up selfie camera - TechRadar India')
        self.assertEqual( self.new_article.description, 'Leaked renders show every angle of potential new handset')
        self.assertEqual( self.new_article.urlToImage,'https://cdn.mos.cms.futurecdn.net/9W2JuazWDRjWaRMUi2dCPc-1200-80.jpg')
        self.assertEqual( self.new_article.url, 'https://www.techradar.com/news/samsungs-next-smartphone-could-have-a-pop-up-selfie-camera')
        self.assertEqual( self.new_article.publishedAt, '2020-04-27T03:16:00Z')
    
    def test_publish_date_format(self):
        '''
        Test case to check if UTC date format is converted to a display-friendly format
        '''
        display_friendly_format = self.new_article.publish_date_format(self.new_article.publishedAt)
        self.assertEqual( display_friendly_format, '2020-04-27')


if __name__ == '__main__':
    unittest.main(verbosity=2)