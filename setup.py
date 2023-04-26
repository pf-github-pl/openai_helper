from setuptools import setup

#python3 setup.py sdist

setup(
    name='openai_helper',
    version='0.1',
    description='Shorten and format code like a pro and add docstrings.',
    url='https://github.com/pf-github-pl/openai_helper',
    license='GNU GPL3',
    packages=['openai_helper'],
    install_requires=["python-dotenv==1.0.0", "openai==0.27.4"]
)