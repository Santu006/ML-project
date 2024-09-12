from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the given file path.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    
    return requirements

setup(
    name='ML_PROJEC',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
