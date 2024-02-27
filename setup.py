from setuptools import setup

setup(
      name='inauconf',
      version='1.2.3',
      description='hidden text',
      long_description= 'Inauconf is the script to hidden real Text Ce projet est une application Python qui effectue diverses opérations. Il est écrit en utilisant le langage de programmation Python.',
      author='Gabriel Ndjieudja',
      author_email='gabrielndjieudja@gmail.com',
      url='https://github.com/ndjieudja/inauconf.git',
      license='MIT',
      py_modules=['inauconf'],
      python_requires='>=3.8', #python version required
      install_requires = [
            'hashlib',
          'argparse'
      ],
      packages=['inauconf'],
            entry_points={
                    'console_scripts': [
                            'testscript = inauconf.__main__:main'
                    ]
            }
    )