from setuptools import setup, find_packages

long_desc = """
Process items in batches rather than one-by-one.
"""
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for classifiers

setup(
    name='python-batcher',
    version='0.0.2',
    description="Process items in batches rather than one-by-one.",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    keywords='batch,database insert',
    author='Paul M Furley',
    author_email='paul@paulfurley.com',
    url='https://github.com/paulfurley/python-batcher',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
    ],
    tests_require=[],
)
