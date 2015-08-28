import os
from setuptools import setup

# yamlcfg
# Hierarchical YAML configuration utility for Python

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yamlcfg",
    version = "0.4.0",
    description = "Hierarchical YAML configuration utility for Python",
    author = "Johan Nestaas",
    author_email = "johan@riskiq.net",
    license = "BSDv2",
    keywords = "config, configuration, cfg, yaml, yml",
    url = "https://github.com/RiskIQ/pyyamlcfg",
    packages=['yamlcfg'],
    package_dir={'yamlcfg': 'yamlcfg'},
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
        'pyyaml',
    ],
    entry_points = {
        'console_scripts': [
            'yamlcfg = yamlcfg.bin:yamlcfg',
        ],
    },
    #package_data = {
        #'yamlcfg': ['catalog/*.edb'],
    #},
    #include_package_data = True,
)
