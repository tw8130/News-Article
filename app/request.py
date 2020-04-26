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


def get_sources():

    """
    Function that gets the json response to our url request
    """

    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results



