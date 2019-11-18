from bs4 import BeautifulSoup
import requests, re, json, sys, os

url = sys.argv[1]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
response = requests.get(url, headers)    #Perform GET request to command-line argument specified URL
if response == 0:
    input('Unable to get response. Press enter to quit...')
    sys.exit()
    
status_codes = [404, 403, 429]
if response.status_code in status_codes:    #If negative staus code received, exit
    print("Error: Status code {} received.".format(response.status_code))
    input("Press enter to exit...")
    sys.exit()
    
html_doc = response.text    #Convert to html and pass into BeautifulSoup constructor
soup = BeautifulSoup(html_doc, "lxml")

terms = []
definitions = []
cards = soup.find('div', class_=re.compile('SetPage-setDetailsTerms'))  #Isolate cards

def parseCards(z):  #Return either a list of terms, or a list of definitions
    a = []
    for x in cards.find_all('a', class_=re.compile(z)):
        x = str(x).replace('<br/>','\n')
        x = BeautifulSoup(x, 'lxml').get_text()
        a.append(x)
    return a

terms = parseCards('SetPageTerm-wordText')
definitions = parseCards('SetPageTerm-definitionText')

title = soup.find('div', class_=re.compile('SetPage-setTitle')).get_text()  #Get title
user = soup.find('span', class_=re.compile('UserLink-username')).get_text() #Get username

invalid_chars = ['/','\\',':','?','\"','<','>','|']
for i_ in invalid_chars:    #Remove any characters from title and username that don't play nicely with the Windows filesystem
    title = title.replace(i_,'')
    uesr = user.replace(i_,'')

cards = []
data = []   #Will contain all data to be output in JSON format
data.append({"title":title})    #Add title object to data
data.append({"user":user})      #Add user object to data

for i in range(0, len(terms)):  #Add all terms and definitions as corresponding members
    cards.append({terms[i]:definitions[i]})
data.append({"cards":cards})



jsondir = "{}/{}/".format(sys.argv[2],user) #Set output directory

try:
    os.mkdir(jsondir)   #Create download directory
except FileExistsError: #If the download directory already exists, pass
    pass
except:
    print("Unexpected error: ", sys.exc_info()[0])

with open(jsondir+title+".json", "w+") as fp: #Ouput all data in JSON format
    json.dump(data,fp,sort_keys=True,indent=4)
