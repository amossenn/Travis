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
    album = article.h1
    #Grabs the full class tag with the artist name
    artist = article.h2
    #Grabs the full clas tag with the release year
    year = article.span
    #Grabs the full class tag with the genre
    genre = article.find_all(class_="genre-list__link")
    #Grabs the full class tag with the review score
    score = article.find_all(class_="score")
    #Grabs the full class tag with the review date
    date = article.time
    #Grabs the full class tag with the author name
    author = article.find_all(class_="authors-detail__display-name")


    print album
    print artist
    print year
    print genre
    print score
    print date
    print author
    
reviewParser()
