import os
import sys
from setuptools import setup, find_packages

f = open('README.rst')
readme = f.read()
f.close()

version = '0.0.1'

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='bengali-stemmer',
    version=version,
    description=('BanglaKit bengali-stemmer is a library for stemming'
                 'Bengali words into root words, removing inflections.'),
    long_description=readme,
    author='BanglaKit Project',
    author_email='banglakit@gmail.com',
    maintainer='BanglaKit Project',
    maintainer_email='banglakit@gmail.com',
    url='https://github.com/banglakit/bengali-stemmer/tree/master',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Bengali',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    zip_safe=False,
)
