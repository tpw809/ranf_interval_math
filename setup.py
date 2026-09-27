# pip install -e .

from setuptools import setup, find_packages
# from distutils.core import setup

setup(
    name='interval_math',
    version='0.0.1',  # major.minor[.patch[.sub]]
    description='basic tool for interval arithmetic',
    url='https://github.com/tpw809/ranf_interval_math',
    author='Timothy P Woodard',
    author_email='timothy.woodard.809@outlook.com',
    license='MIT',
    packages=['interval_math'],
    package_dir={'': 'src'},
    install_requires=[
        'numpy', 
    ]
)
