import requests
from pprint import pprint

def main():
    url = 'https://api.sejm.gov.pl/eli/acts/DU/2023/1590'
    response = requests.get(url).json()
    fields = {'ELI': ('identyfikator_aktu', True)}
    pass

if __name__ == '__main__':
    main()