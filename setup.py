from setuptools import setup

setup(
    name='peanut',
    version='0.0.1',
    packages=['peanut/'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': [
            'peanut=peanut.main:main',
        ],
    },
    description='crawler for peanut daily price',
    install_requires=[
        'requests_html>=0.10.0',
    ],
)
