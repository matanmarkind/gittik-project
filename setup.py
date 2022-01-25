from setuptools import setup, find_packages


setup(
    name = 'gittik-project',
    version = '0.1.0',
    author = 'Matan Markind',
    description = 'An example package.',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)