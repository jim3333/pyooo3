from setuptools import setup, find_packages


setup(
    name='pyooo3',
    version='0.7.2',
    license='MIT',
    author="ppyaa",
    author_email='ppyaa@no.github.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jim3333/pyooo3',
    keywords='pyooo3',
    long_description="https://github.com/jim3333/pyooo3",
    install_requires=[
          'scikit-learn',
      ],

)
