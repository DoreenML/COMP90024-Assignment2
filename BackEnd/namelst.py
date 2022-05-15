import os
import io

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

FILE_NAME = 'location_name.txt'

def read_txt():
    lst = []
    with io.open(os.path.join(__location__, FILE_NAME), 'r',encoding='utf-8') as lines:
        for line in lines:
            start = line.index(':')
            lst.append(line[start+1:-1])
    return lst

lst = read_txt()
print(lst)