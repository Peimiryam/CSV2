import os
from pathlib import Path
import sys
import csv

cwd = os.getcwd()

contents = []

class Reader:
    def __init__(self):
        self.contents = []

    def overwrite(self):
        arg_no = 0
        for arg in sys.argv[3:]:
            arg_list = arg
            arg_list = arg_list.split(",")
            x = int(arg_list[0])
            y = int(arg_list[1])
            value = ",".join(arg_list[2:])
            if len(arg_list) !=3:
                print("Wrong input")
                break
            if 0 >= y > len(self.contents):
                print("Wrong input")
                break
            if 0 >= x > len(self.contents[y]):
                print("Wrong input")
                break
            change = self.contents[y]
            change[x] = value
            arg_no += 1
            print("Successfully updated!")
        
class CsvReader(Reader):
    def read(self):
        self.contents = []
        with open(sys.argv[1]) as f:
            print("Open file...")
            reader = csv.reader(f)
            for line in reader:
                self.contents.append(line)
                self.overwrite()

class CsvWriter:
    def write(self):
        with open(sys.argv[2], 'w', newline='') as f:
            writer = csv.writer(f)
            for item in self.contents:
                writer.writerow(item)

def factory():
    source_dictionary = {".csv": CsvReader}
    source_path = os.path.join(cwd, sys.argv[1])
    source_type = Path(source_path).suffix
    if source_type not in source_dictionary:
        return None
    destination_path = os.path.join(cwd, sys.argv[2])
    destination_dictionary = {".csv": CsvWriter}
    destination_type = Path(destination_path).suffix
    if destination_type not in destination_dictionary:
        return None
    
    class Final(source_dictionary[source_type], destination_dictionary[destination_type]):
        pass
    return Final()

object = factory()
object.read()
object.write()


