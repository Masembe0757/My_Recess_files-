#Importing key libraries
from bs4 import BeautifulSoup
import requests
import csv

#Scrapping bird spacies from xeno-canto site


def bird_species():
    # Declaring the website url which is the end point where bird species are going
    #to be extracted
    url = 'https://xeno-canto.org/collection/species/latest'
    
    #using the get method of response package to scoop data about birds
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Scrapping script
        
        species_list = soup.find_all('table', class_='results')
        #Created a list to store bird species data
        
        bird_species_data = []
        for species_table in species_list:
            #looping to get common names of species
            
            species_common_names = species_table.find_all(
                'span', class_='common-name')
            #looping to get scientific names of species
            
            species_scientific_names = species_table.find_all(
                'span', class_='sci-name')
            
            
            #For loop to add collected data to the species list data list with lables
            for common_name, sci_name in zip(species_common_names, species_scientific_names):
                bird_species_data.append(
                    {'common_name': common_name.text.strip(), 'sci_name': sci_name.text.strip()})
        return bird_species_data
    else:
        print('Failed to scrap data from the url provided !')
        return []

# Converting bird_species_data list to a csv file


def generate_csv(data):
    my_file = 'bird_species.csv'
    
    #opening the file for writting
    with open(my_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['common_name', 'sci_name']
        file_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        file_writer.writeheader()
        file_writer.writerows(data)

