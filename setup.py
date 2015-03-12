import os
from setuptools import setup

# treeconf
# Hierarchical configuration parser

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "treeconf",
    version = "0.0.1",
    description = "Hierarchical configuration parser",
    author = "Johan Nestaas",
    author_email = "johan@riskiq.net",
    license = "BSDv2",
    keywords = "config, configuration, cfg, yaml, yml",
    #url = "https://www.github.com/RiskIQ/treeconf
    packages=['treeconf'],
    package_dir={'treeconf': 'treeconf'},
    long_description=read('README.md'),
    classifiers=[
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],
    install_requires=[
    ],
    entry_points = {
        'console_scripts': [
            'treeconf = treeconf.bin:treeconf',
        ],
    },
    #package_data = {
        #'treeconf': ['catalog/*.edb'],
    #},
    #include_package_data = True,
)