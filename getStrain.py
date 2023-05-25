import requests
import json
from bs4 import BeautifulSoup

def main():
    getStrain()

def getStrain():
    r = requests.get('https://www.aznaturalselections.com/education/strains/list/')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    
    for strain in soup.find_all('div', class_='wp-show-posts-inner'):
        name = strain.find('h3', class_='wp-show-posts-entry-title').text.strip()
        strainType = strain.find('div', class_='wp-show-posts-entry-summary').text.strip()
        print(name, strainType)
        print()
        strainData = { 'name': name, 'strainType': strainType }
        
        #export all of the data to a json file
        with open('strainData.json', 'a') as outfile:
            json.dump(strainData, outfile)
            outfile.write('\n')
            

if __name__ == '__main__':
    main()