from setuptools import setup

setup(
    name='reports',
    version='0.1',
    py_modules=['reports'],
    install_requires=[
        'click', 'openpyxl',
    ],
    entry_points = '''
        [console_scripts]
        reports=reports:cli
    '''
)
