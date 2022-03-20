import os
import sys
import random

def replace_random():
    test_list = [2001, 2101]
    random_num = random.choice(test_list)
    return str(random_num)

def replace_word(infile, old_word, new_word):
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: " + infile)
        sys.exit(1)
    f1 = open(infile, 'r').read()
    f2 = open(infile, 'w')
    m = f1.replace(old_word, new_word)
    f2.write(m)


def creat_list_port(_random_):
    return _random_,str(int(_random_)+1),str(int(_random_)+2),"default"+_random_


if __name__ == '__main__':
    _random_ = replace_random()
    _ports_ = creat_list_port(_random_)
    os.system("kubectl create namespace "+_ports_[3])
    replace_word("kubernetes/fulltext-serarch-service.yaml", "2102", _ports_[0])
    replace_word("kubernetes/mongodb-service.yaml", "27017", _ports_[1])
    replace_word("kubernetes/random-demo-service.yaml", "2101", _ports_[2])
    replace_word("kubernetes/fulltext-search-deplyment.yaml", "default", _ports_[3])
    replace_word("kubernetes/mongodb-deplyment.yaml", "default", _ports_[3])
    replace_word("kubernetes/random-demo-deplyment.yaml", "default", _ports_[3])
    replace_word("kubernetes/fulltext-serarch-service.yaml", "fulltext-serarch-service","fulltext-serarch-service-"+ _ports_[0])
    replace_word("kubernetes/mongodb-service.yaml", "mongodb-service", "mongodb-service-"+_ports_[0])
    replace_word("kubernetes/random-demo-service.yaml", "fulltext-serarch-service", "fulltext-serarch-service-"+ _ports_[0])
