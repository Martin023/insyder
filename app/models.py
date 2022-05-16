from shlex import quote


class Quote:
    #class that defines the qoutes(creates quote)
    def __init__(self,quote,author,link):
        self.quote=quote
        self.author=author
        self.link=link

        