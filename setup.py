from setuptools import setup, find_packages


setup(
    name='pyooo3',
    version='0.7',
    license='MIT',
    author="ppyaa",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jim3333/pyooo3',
    keywords='example project',
    long_description="example",
    install_requires=[
          'scikit-learn',
      ],

)
