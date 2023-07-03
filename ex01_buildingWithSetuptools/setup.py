from setuptools import setup,find_packages


setup(
    name='Python Addition Calculator',
    version='1.0.0',
    description='simple setuptools exercise',
    long_description='nothin',
    author='Ella Adeka',
    author_email='eoadeka@gmail.com',
    license='MIT',
    classifiers= [
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='simple Python addition calculator',
    packages=find_packages(),
    install_requires=['requests>=2'],
    entry_points={
        'console_scripts':[
            'addition-calculator=buildAProjectWithSetUpTools.command_line:main'
        ]
    }
)