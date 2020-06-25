import os

from setuptools import find_namespace_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    """
    Get package version (without import the package, which may or may not work)
    :return: version info in maj.min.bld.0 format
    """
    version_dict = {}
    exec(open("src/aspire/version.py").read(), version_dict)
    return version_dict['version']


setup(
    name='aspire',
    version=get_version(),

    description='Algorithms for Single Particle Reconstruction',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license="GPLv3",
    url='https://github.com/ComputationalCryoEM/ASPIRE-Python',
    author='Joakim Anden, Yoel Shkolnisky, Itay Sason, Robbie Brook, Vineet Bansal, Junchao Xia',
    author_email='devs.aspire@gmail.com',

    install_requires=[
        'click',
        'finufftpy',
        'importlib_resources>=1.0.2',
        'joblib',
        'jupyter',
        'matplotlib',
        'mrcfile',
        'numpy==1.16',
        'numpydoc==0.7.0',
        'pandas==0.25.3',
        'pyfftw',
        'python-box',
        'pytest',
        'pytest-cov',
        'python-box',
        'scipy==1.3.0',
        'scikit-learn',
        'scikit-image==0.14.0',
        'sphinxcontrib-bibtex',
        'sphinx-rtd-theme>=0.4.2',
        'tqdm',
    ],

    # Here we can call out specific extras,
    #   for example gpu packages which may not install for all users,
    #   or developer tools that are handy but not required for users.
    extras_require = {
        'gpu': ['pycuda', 'cupy'],
        'dev': ['bumpversion', 'flake8', 'isort', 'pyflakes', 'pydocstyle', 'snakeviz'],
    },

    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    package_data={'aspire': ['config.ini'], 'aspire.data': ['*.*']},

    zip_safe=True,
    test_suite='tests',

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
