#ReviewParser.py
#Scripted by: Austin Moss-Ennis
#Description: Grabs a pitchfork review and parses the Artist, Album Name,
# Release Date, Genre, Review Score, Review Author, and Review Date
def reviewParser():
    import requests
    from bs4 import BeautifulSoup
    #Grabs html information from the Pitchfork website
    req = requests.get('http://pitchfork.com/reviews/albums/22835-homogenic/')
    #Parses the information to make it more easily traversable
    soup = BeautifulSoup(req.text, "html.parser")
    #Gets the part of HTML with the information needed
    article = soup.article

    #Grabs the full class tag with the album name
    album = str(article.h1)
    #Grabs the full class tag with the artist name
    artist = str(article.h2.a)
    #Grabs the full class tag with the release year
    year = str(article.span)
    #Grabs the full class tag with the genre
    genre = str(article.find_all(class_="genre-list__link"))
    #Grabs the full class tag with the review score
    score = str(article.find_all(class_="score"))
    #Grabs the full class tag with the review date
    date = str(article.time)
    #Grabs the full class tag with the author name
    author = str(article.find_all(class_="authors-detail__display-name"))
    
    #Removes surrounding text from artist name
    artist = artist.split("\">")[1]
    artist = artist.rsplit("</")[0]
    artist = artist.decode("utf-8")
    
    #Removes surrounding text from album name
    album = album.split("\">")[1]
    album = album.rsplit("</")[0]
    album = album.decode("utf-8")
    
    #Removes surrounding text from release year
    year = year.rsplit("<!-- /react-text --></span>")[0]
    year = year[(len(year)-4):(len(year))]
    
    #Removes surrounding text from first genre listed in review
    genre = genre.rsplit("\">")[1]
    genre = genre.split("</")[0]
    genre = genre.decode("utf-8")
    
    #Removes surrounding text from score
    score = score.split("\">")[1]
    score = score.rsplit("</")[0]
    
    #Removes surrounding text from author's name
    author = author.split("\">")[1]
    author = author.rsplit("</")[0]
    author = author.decode("utf-8")

    #Removes surrounding text from review date
    date = date.split("\">")[1]
    date = date.rsplit("</")[0]
    dateList = date.split(" ")
    date = dateList[0] + " " + dateList[2]

    print album
    print artist
    print year
    print genre
    print score
    print date
    print author
    
reviewParser()
