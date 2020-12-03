# Домашнее задание к лекции 2.«Iterators. Generators. Yield»

## Solution
- Made 2 classes. First one parses data file via JSON library, another one reads data file line by line.
- Made iterator for navigating through JSON file.

*** Warning. Due to encoding errors of some strings, second class which reads file line by line - doesn't see all strings.
 

1. Написать класс итератора, который по каждой стране из файла [countries.json](https://github.com/mledoze/countries/blob/master/countries.json) ищет страницу из википедии.   
Записывает в файл пару: страна – ссылка.
Ссылку формировать самостоятельно.

2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
