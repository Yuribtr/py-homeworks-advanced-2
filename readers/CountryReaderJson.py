import json


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
