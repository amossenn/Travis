#ReviewUploader.py
#Scripted by: Austin Moss-Ennis
#Description: Uploads the information from the pitchfork article to a Google
# sheets profile
def reviewUploader():
    import requests
    import ReviewParser
    from bs4 import BeautifulSoup
    
    #Want to access Pitchfork's first review page and iterate upwards
    currPage = 1
    p4k = "http://pitchfork.com"
    url = "http://pitchfork.com/reviews/albums/?page="
    
    #Currently using while loop to get to some static place. Will change
    #to make dynamic in the future
    while (currPage < 11):
        req = requests.get(url + str(currPage))
        soup = BeautifulSoup(req.text, "html.parser")
        
        #Gets HTML portion of the page that contains the 12 review links
        reviews = soup.find_all(class_="album-link")
        
        #Loops through the 12 review links on each page and sends the links to
        #the ReviewParser program
        for index in range(len(reviews)):
            
            #Converts HTML to usable string
            currRev = str(reviews[index])
            currLink = currRev.split("href=\"")[1]
            currLink = currLink.rsplit("\">")[0]
            ReviewParser.reviewParser(p4k + currLink)

            
        
        currPage += 1
reviewUploader()