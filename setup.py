from setuptools import setup, find_packages

setup(
    name='clockify-time-tracker',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'clockify-tracker=src.cli:main',
        ],
    },
    author='Votre Nom',
    description='Un outil de suivi des temps Clockify',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
