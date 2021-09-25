from setuptools import setup, find_packages

with open('./requirements.txt', 'r') as f:
    reqs = f.read().splitlines()
    install_requires = [req.split('=')[0] for req in reqs]

setup(
    name="raw2jpg",
    author="I Kit Cheng",
    author_email="matthewkit@gmail.com",
    description="Python package for converting raw images to jpg images.",
    version="1.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=install_requires,
    setup_requires=(
        'pytest-runner',
        ),
    tests_require=(
            'pytest-cov',
        ),

    entry_points={
       'console_scripts': [
           'raw2jpg = raw2jpg.raw2jpg:raw2jpg_command',
       ]
    },
)
