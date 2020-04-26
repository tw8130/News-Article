class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
    
class Articles:
    '''
    Article class to define Articles objects
    '''
    def __init__(self,author,title,description,urlToImage,url,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt