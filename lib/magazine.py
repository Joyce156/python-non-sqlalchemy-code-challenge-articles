
from .article import Article

class Magazine:
    # store all Magazine instances so we can find the top publisher later
    all_magazines = []

    def __init__(self, name, category):
        # validate name and category
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be 2–16 characters.")
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) < 1:
            raise ValueError("Category must have at least 1 character.")

        self.name = name
        self.category = category

        # remember this magazine in the class-level registry
        Magazine.all_magazines.append(self)

    # name property (read/write with validation)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be 2–16 characters.")
        self._name = value

    # category property (read/write with validation)
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value) < 1:
            raise ValueError("Category must have at least 1 character.")
        self._category = value

    # Return all Article instances that belong to this magazine
    def articles(self):
        result = []
        for a in Article.all:
            if a.magazine == self:
                result.append(a)
        return result

    # Return unique list of Author instances who have written for this magazine
    def contributors(self):
        authors = []
        for a in self.articles():
            if a.author not in authors:
                authors.append(a.author)
        return authors

    # Return list of title strings for my articles; None if there are no articles
    def article_titles(self):
        my_articles = self.articles()
        if len(my_articles) == 0:
            return None
        titles = []
        for a in my_articles:
            titles.append(a.title)
        return titles

    # Return authors who wrote more than 2 articles for this magazine
    # Return None if none meet that threshold
    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            writer = a.author
            counts[writer] = counts.get(writer, 0) + 1

        result = []
        for author, count in counts.items():
            if count > 2:
                result.append(author)

        if len(result) == 0:
            return None
        return result

    # Classmethod: find the Magazine instance with the most articles
    # Return None if there are no articles at all
    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None

        top_mag = None
        top_count = 0
        for mag in cls.all_magazines:
            c = len(mag.articles())
            if c > top_count:
                top_count = c
                top_mag = mag
        return top_mag
