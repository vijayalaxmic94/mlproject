from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str] :
    '''
    This func will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT == '-e .':
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vijayalaxmi',
    author_email='vijayalaxmic94@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)