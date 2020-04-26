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


