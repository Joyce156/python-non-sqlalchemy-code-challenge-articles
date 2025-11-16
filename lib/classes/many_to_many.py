class Author:
    # keep track of all authors (not required but useful)
    all = []

    def __init__(self, name):
        # name must be a string with length > 0
        if type(name) == str and len(name) > 0:
            self._name = name      # underscore means “private”
        else:
            raise Exception("Name must be a non-empty string")

        Author.all.append(self)

    @property
    def name(self):
        # name cannot change → immutable
        return self._name
    
    # no setter for name → prevents changing it
    @name.setter
    def name(self, value):
    # name is immutable → ignore any attempt to change it
       pass


    # return all articles written by this author
    def articles(self):
        result = []
        for article in Article.all:
            if article.author == self:
                result.append(article)
        return result

    # return unique magazines this author has written for
    def magazines(self):
        mags = []
        for article in Article.all:
            if article.author == self:
                if article.magazine not in mags:
                    mags.append(article.magazine)
        return mags

    # create a new Article for this author
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    # return unique categories for magazines this author wrote for
    def topic_areas(self):
        mags = self.magazines()
        if len(mags) == 0:
            return None
        
        categories = []
        for mag in mags:
            if mag.category not in categories:
                categories.append(mag.category)
        return categories



class Magazine:
    # track all magazines
    all = []

    def __init__(self, name, category):
        # validate name
        if type(name) == str and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Magazine name must be a string 2–16 characters")

        # validate category
        if type(category) == str and len(category) > 0:
            self._category = category
        else:
            raise Exception("Category must be a non-empty string")

        Magazine.all.append(self)

    # name is mutable → has getter and setter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # validate again
        if type(value) == str and 2 <= len(value) <= 16:
            self._name = value

    # category is mutable → getter + setter
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) == str and len(value) > 0:
            self._category = value

    # list of articles for this magazine
    def articles(self):
        result = []
        for article in Article.all:
            if article.magazine == self:
                result.append(article)
        return result

    # unique authors for this magazine
    def contributors(self):
        authors = []
        for article in Article.all:
            if article.magazine == self:
                if article.author not in authors:
                    authors.append(article.author)
        return authors

    # list of titles of all articles in this magazine
    def article_titles(self):
        article_list = self.articles()
        if len(article_list) == 0:
            return None
        
        titles = []
        for a in article_list:
            titles.append(a.title)
        return titles

    # authors with more than 2 articles in this magazine
    def contributing_authors(self):
        authors = self.contributors()
        result = []

        for author in authors:
            count = 0
            for article in Article.all:
                if article.magazine == self and article.author == author:
                    count += 1
            
            if count > 2:
                result.append(author)

        if len(result) == 0:
            return None

        return result

    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
        
        biggest = None
        max_count = 0

        for magazine in cls.all:
            count = len(magazine.articles())
            if count > max_count:
                max_count = count
                biggest = magazine
        
        return biggest



class Article:
    # track all articles
    all = []

    def __init__(self, author, magazine, title):
        # author must be Author
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an Author")

        # magazine must be Magazine
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be a Magazine")

        # validate title
        if type(title) == str and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Title must be 5–50 chars")

        Article.all.append(self)

    # title is immutable
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
    # title is immutable → ignore any attempt to change it
       pass


    # author is mutable
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    # magazine is mutable
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
