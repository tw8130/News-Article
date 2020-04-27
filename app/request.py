import urllib.request,json
from .models import Source,Articles

# Source = source.Source
api_key = None
base_url = None
base_url_articles=None

def configure_request(app):
    global api_key,base_url,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    base_url_articles=app.config["NEWS_API_ARTICLE_URL"]


def get_sources(source):

    """
    Function that gets the json response to our url request
    """

    get_sources_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):

    """
    Function that process  the sources result and transform them to a list of Objects

    Args:
    source_list:A list of dictionaries that contain  news source details

    Returns:
    source_results:A list of news source Objects
    """

    source_results=[]

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')



        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

        # print(source_list)

    return source_results

def get_articles(id):
    '''
    Function to get a source and it's articles
    '''
    get_articles_url = base_url_articles.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(article_list):
    '''
    Function that processes the article results and transform them to a list of objects

    Args:
        article_list: A list of dictionaries that contain article details
    Returns :
        article_results: A list of article objects
    '''
    article_results = []

    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        urlToArticle = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        article_object = Articles(source,author, title, description, urlToImage, urlToArticle, publishedAt)
        article_results.append(article_object)
    
    return article_results



