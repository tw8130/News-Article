from flask import render_template
from . import main
from ..requests import get_sources

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''
    
    title = 'Home- Welcome News Highlights Website'
    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)
