import setuptools

setuptools.setup(
    name="minimalcryptocurrency",
    version="0.1.2",
    url="https://github.com/Aixa98/CryptoMaster.git",

    author=u"Aixa Benitez",
    author_email="aixabenitez2@gmail.com",

    license='GPL-3',

    description="This package implements a basic Blockchain and a Cryptocurrency",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['ecdsa>=0.13'],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
