import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='latexSAK',  
     version='0.1.3',
     scripts=['latexSAK'] ,
     author="Géry Casiez",
     author_email="gery.casiez@gmail.com",
     description="Swiss army knife for LaTeX files.",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://gitlab.inria.fr/casiez/latexSAK",
     packages=setuptools.find_packages(),
     install_requires=[ 'argparse', 'texsoup'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: MacOS",
     ],

 )