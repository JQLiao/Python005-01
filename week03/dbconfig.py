from configparser import ConfigParser
import os
confpath = "C:\\JQL\\geektime\\Python005-01\\week03"
os.chdir(confpath)

def read_db_conf(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception(f'{section} not found in the {filename} file')
    return dict(items)

if __name__ == "__main__":
    print(read_db_conf())