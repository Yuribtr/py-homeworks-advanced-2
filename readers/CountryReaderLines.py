import re


class CountryReaderLines:
    """
    Class reads text file line by line in text mode. Consumes less memory comparing to JSON.
    Does not recognize broken strings.
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
