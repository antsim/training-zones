from setuptools import setup

setup(
    name='Training Zones',
    version='0.1',
    py_modules=['trainingzones'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        trainingzones=trainingzones:cli
    ''',
)