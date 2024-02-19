from setuptools import setup, find_packages

setup(
    name='inauconf',
    version='1.2.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crypt=crypt'
        ]
    },
    install_requires=[
        'argparse',
        #'hashlib'
    ],
)