import urllib.request,json
from .models import Source,Article

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

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):

    """
    Function that process  the sources result and transform them to a list of Objects

    Args:
    source_list:A list of dictionaries that contain  news source details

    Returns:
    source_results:A list of news source Objects
    """

    sources_results=[]

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')



        source_object = Sources(id,name,description,url,category)
        sources_results.append(source_object)

        # print(source_list)

    return sources_results


