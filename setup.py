from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''


    requirements = []
    with open(r'D:\Data_Science_Project\mymlproject\requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        
        # For removing \n from the above read line

        [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .') # To remove '-e .' from the list of packages

    return requirements



setup(
    name = 'myfirstmlproject',
    version = '0.0.1',
    author = "Subhrajyoti",
    author_email = "subhrajyotimay97@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)