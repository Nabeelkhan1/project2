from setuptools import setup,find_packages

def get_requirements(file_path):
    requirements=[]
    with open(file_path,'r')as f:
        requirements=f.readlines()
        requirements=[r.replace('\n','') for r in requirements]
    return requirements



setup(
    name='project2',
    version='0.0.1',
    description='this is test project for ml pipeline',
    author='nabeel',
    author_email='nabeelkhan5849@gmail.com',
    packages=find_packages(),
    install_requir=get_requirements('requirements.txt')

)