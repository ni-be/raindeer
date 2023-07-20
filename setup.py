from setuptools import setup, find_packages


setup(
    name='Raindeer',
    version='1.0.0',
    author='Nikolas Bertrand, Julian Bruns, Josephine Funken, Timo Wedding',
    packages=find_packages(),
    install_requires=[
        'pandas~=2.0.3',
        'matplotlib~=3.7.1',
        'numpy~=1.25.0',
        'PyYAML~=6.0',
        'requests~=2.31.0'],
    entry_points={
        'console_scripts': [
            'raindeer = raindeer.raindeer:main']})
