import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rconbot",
    version = "0.0.1",
    author = "James Bliss",
    author_email = "astronouth7303@gmail.com",
    description = "Framework to write 'bots' that use the Nexuiz rcon protocol.",
    license = "GPL",
    keywords = "nexuiz bot rcon",
    url = "https://github.com/astronouth7303/rconbot",
    packages=['rconbot'],
#    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Games/Entertainment :: First Person Shooters",
    ],
)
