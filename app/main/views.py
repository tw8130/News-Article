from flask import render_template,redirect,url_for,request
from . import main
from ..request import get_sources,get_articles,everything, search_everything

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''

    title = 'Home- Welcome News Highlights Website'
    # Getting the news sources
    news_sources = get_sources()
    print(news_sources)
    return render_template('index.html', title=title, sources=news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_id} page"
    #title = "Hello"
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)

@main.route('/everything&<int:per_page>')
def all_news(per_page):
    '''
    Function that returns top headlines articles
    '''
    # per_page = 40
    everything_news = everything(per_page)
    title = 'All News'
    
    search_articles = request.args.get('search_query')

    if search_articles:
        return redirect(url_for('main.search',topic=search_articles))
    else:
        return render_template('everything.html', title=title, name='All News', news=everything_news)

@main.route('/search/<topic>')
def search(topic):
    '''
    function that returns the results of search request
    '''
    limit = 40
    search_name = topic.split(" ")
    search_name_format = "+".join(search_name)
    search_every = search_everything(limit,search_name_format)

    title = '{search_name_format} Results'

    return render_template('search.html',title=title,news = search_every)

