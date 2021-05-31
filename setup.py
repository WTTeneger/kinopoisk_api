
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='filmapis',
      version='0.2',
      description='The funniest joke in the world',
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/WTTeneger/kinopoisk_api',
      author='Amal Agishev',
      author_email='swintages@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)