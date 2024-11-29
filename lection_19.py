from dataclasses import dataclass
from typing import List
import yaml 

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

node_1 = Node("bbb")
node_2 = Node("aaa")
print(node_1.data)

print(node_1.next)

@dataclass
class StudebrntTupe:
    """
    Subdata fo GroupTupe Class
    """
    surname: str
    name: str
    rating: str
    rights: List[str]

def read_yml(path):
    with open(path, 'r', encoding="utf-8") as yaml_file:
        yaml_dict = yaml.load(yaml_file)