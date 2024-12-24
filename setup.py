'''
The setup.py file is an essential part of packaging distributing 
Python projects. It is used by setuptools (or disutils in older python versions)
to define the configuration of your projet, such as its metadata, dependencies and more

'''
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirements_list:List[str]=[]

    try: 
        with open('requirements.txt','r') as file: 
            # Read lines from the file
            lines = file.readlines()
            ## Process each line 
            for line in lines:
                requirements= line.strip()
                ## ignore empty lines and -e .
                if requirements and requirements!= '-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list

setup(
    name = "Network Security",
    version = "0.0.1",
    author="DHruv Tyagi ",
    packages=find_packages(),
    install_requires=get_requirements()
)