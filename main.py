import hashlib
import json
from readers.CountryReaderJson import CountryReaderJson
from readers.CountryReaderLines import CountryReaderLines

if __name__ == '__main__':

    counter = 0
    country_reader = CountryReaderJson('countries.json')
    with open('result.txt', 'w', encoding='utf8') as file:
        for country in country_reader:
            counter += 1
            file.write(f'{country} - https://wikipedia.org/wiki/{country.replace(" ", "_")}\n')
    print(f'Found {counter} lines')

    counter = 0
    country_reader = CountryReaderLines('countries.json')
    with open('result2.txt', 'w', encoding='utf8') as file:
        for country in country_reader:
            counter += 1
            file.write(f'{country} - https://wikipedia.org/wiki/{country.replace(" ", "_")}\n')
    print(f'Found {counter} lines')

    def countryReaderIter(filename: str):
        """
        This iterator returns country names from parsed JSON file
        """
        with open(filename, 'r', encoding='utf8') as json_file:
            tmp = json_file.readline()
            while tmp:
                yield json_file.readline()
                tmp = json_file.readline()

    for country in countryReaderIter('result.txt'):
        print(hashlib.md5(country.encode('utf8')).hexdigest())
    print(f'Processed {counter} lines')
