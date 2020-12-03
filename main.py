import json
import re


class CountryReaderJson:
    """
    Class reads JSON file with json library. Consumes a lot of memory for parsing whole file at once.
    """
    def __init__(self, filename: str):
        self.__cursor = -1
        with open(filename, 'r', encoding='utf8') as json_file:
            self.__countries = json.load(json_file)

    def __iter__(self):
        # this needed if previous iterations cycle was not ended or if we run iterator more than one time
        self.__cursor = -1
        return self

    def __next__(self):
        self.__cursor += 1
        if self.__cursor >= len(self.__countries):
            raise StopIteration
        return self.__countries[self.__cursor]['name']['common']


class CountryReaderText:
    """
    Class reads text file line by line. Consumes less memory comparing to JSON. Does not recognize broken strings.
    """
    def __init__(self, filename: str):
        self.__file = open(filename, 'r', encoding='utf8')
        self.__pattern = '\s*\"common\":\s*\"(\w*)\",\s*'

    def __iter__(self):
        # this needed if previous iterations cycle was not ended or if we run iterator more than one time
        self.__file.seek(0)
        return self

    def __next__(self):
        while True:
            line = self.__file.readline()
            if not line:
                raise StopIteration
            res = re.search(self.__pattern, line)
            if res:
                return res.group(1)


if __name__ == '__main__':

    counter = 0
    country_reader = CountryReaderJson('countries.json')
    with open('result.txt', 'w', encoding='utf8') as file:
        for country in country_reader:
            counter += 1
            file.write(f'{country} - https://wikipedia.org/wiki/{country.replace(" ", "_")}\n')
    print(f'Found {counter} lines')

    counter = 0
    country_reader = CountryReaderText('countries.json')
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
            countries = json.load(json_file)
            for country in countries:
                yield country['name']['common']

    counter = 0
    with open('result3.txt', 'w', encoding='utf8') as file:
        for country in countryReaderIter('countries.json'):
            counter += 1
            file.write(f'{country} - https://wikipedia.org/wiki/{country.replace(" ", "_")}\n')
    print(f'Found {counter} lines')
