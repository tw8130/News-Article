import unitttest
from app.models import Articles

class ArticleTest(unitttest.TestCase):
    '''
    Test class to test behaviours of article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Jeremy Bogaisky','Boeing-Embraer Deal Collapses - Forbes','Boeing has abandoned a deal to buy 80% of Embraer’s commercial aircraft business for $4.2 billion, stating Saturday morning that the Brazilian company didn’t satisfy necessary conditions of the agreement','null','"https://www.forbes.com/sites/jeremybogaisky/2020/04/25/boeing-embraer-deal-collapses/','2020-04-25T15:16:58Z')
    
    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue(isinstance( self.new_article, Articles ))
    
    def test_init(self):
        '''
        Test case to check if the Article class is initialized
        '''

        self.assertEqual( self.new_article.author, 'Jeremy Bogaisky')
        self.assertEqual( self.new_article.title, 'Boeing-Embraer Deal Collapses - Forbes')
        self.assertEqual( self.new_article.description, 'Boeing-Embraer Deal Collapses - Forbes','Boeing has abandoned a deal to buy 80% of Embraer’s commercial aircraft business for $4.2 billion, stating Saturday morning that the Brazilian company didn’t satisfy necessary conditions of the agreement')
        self.assertEqual( self.new_article.urlToImage,'null')
        self.assertEqual( self.new_article.url, 'https://www.forbes.com/sites/jeremybogaisky/2020/04/25/boeing-embraer-deal-collapses/')
        self.assertEqual( self.new_article.publishedAt, '2020-04-25T15:16:58Z')
    
    def test_publish_date_format(self):
        '''
        Test case to check if UTC date format is converted to a display-friendly format
        '''
        display_friendly_format = self.new_article.publish_date_format(self.new_article.publishedAt)
        self.assertEqual( display_friendly_format, '2020-04-25')


if __name__ == '__main__':
    unittest.main(verbosity=2)