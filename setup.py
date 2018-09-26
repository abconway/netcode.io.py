from setuptools import setup, find_packages


__version__ = '0.0.1'
__requirements__ = [
    'pysodium==0.7.0.post0',
]


setup(
    name='netcode',
    version=__version__,
    description='Python 3 implementation of Netcode.io',
    author='Alex Conway',
    author_email='abconway2@gmail.com',
    url='https://github.com/abconway/netcode.io.py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=__requirements__,
)