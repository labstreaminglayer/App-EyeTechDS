from setuptools import setup, find_packages
from shutil import copyfile
import os


def get_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md')) as f:
        long_description = f.read()
        return long_description


def copy_docs():
    docs_dir = "eyetechlsl/docs"
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    copyfile("README.md", docs_dir + "/README.md")

copy_docs()
long_description = get_long_description()

setup(
    name="eyetechlsl",
    version="1.0.0",
    description="Stream Gaze and VideoRaw data from EyeTechDS Devices",
    keywords="eyetechds lsl eye tracker gaze",
    url="https://github.com/intheon/eyetechds-lsl",
    author="Itay Plavin",
    author_email="itay.plavin@intheon.io",
    license="GNU General Public License v3.0",
    entry_points={"console_scripts": ["eyetechlsl=eyetechlsl.__main__:main"]},
    packages=find_packages(),
    package_data={"eyetechlsl": ["docs/README.md", "docs/examples/*"]},
    include_package_data=True,
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy",
        "pylsl"
    ],
    extras_require={"Video": ["python-opencv"]},
    classifiers=[
        # How mature is this project?  Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
    ],
)