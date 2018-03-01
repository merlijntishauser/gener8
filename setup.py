# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='gener8',
    version='0.1',
    description='  A little tool to generate commonly used ci/cd templates like Dockerfiles.',
    author='Merlijn Tishauser',
    author_email='merlijn@gargleblaster.org',
    url='https://github.com/merlijntishauser/gener8',
    download_url='https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
    keywords=['templates', 'docker', 'Dockerfile'],
    classifiers=[],
    packages=[
        'gener8',
        'gener8.templates',
        'gener8.templates.docker',
        'gener8.scripts'
    ],
    package_data={
        'gener8.templates': ['*.jinja2'],
        'gener8.templates.docker': ['*.jinja2'],
        'gener8.scripts': ['*.sh']
    },
    scripts=['bin/gener8'],
    install_requires=[
        "certifi",
        "click",
        "click-log",
        "chardet",
        "Jinja2",
        "idna",
        "MarkupSafe",
        "pip",
        "requests",
        "setuptools",
        "urllib3",
        "wheel"
    ],
    extras_require={
        'test': [
            "mock",
            "pytest",
            "pytest-mock",
            "pytest-cov",
            "tzlocal"
        ]
    },
    zip_safe=False
)
