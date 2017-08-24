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
    clean = BeautifulSoup(req.text, "html.parser")
    print clean
    
reviewParser()