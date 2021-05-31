import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='kinopoisk_api',  
     version='0.1',
     scripts=['API_kinopoisk'] ,
     author="Amal Agishev",
     author_email="amalagishev.ru",
     description="Api for working with data on kinopoisk",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/WTTeneger/kinopoisk_api",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )