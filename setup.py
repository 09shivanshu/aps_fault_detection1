from setuptools import find_packages,setup
from typing import List

Requirement_File_Name="requirements.txt"

def get_requirements() -> List[str]:
    with open(Requirement_File_Name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
    

setup(
    name ="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="shivanshu09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)