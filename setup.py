import setuptools

if __name__ == "__main__":
    setuptools.setup(
        # Name of the project
        name='bsse',

        # Version
        version="0.1.0",

        # Description
        description='Evaluation tools for the audio source separation',
        url='https://github.com/sigsep/bsseval',

        # Your contact information
        author='Fabian-Robert Stoeter',
        author_email='mail@faroit.com',

        # License
        license='MIT',

        # Packages in this project
        # find_packages() finds all these automatically for you
        packages=setuptools.find_packages(),

        # Dependencies, this installs the entire Python scientific
        # computations stack
        install_requires=[
            'numpy',
            'scipy',
        ],

        extras_require={
            'tests': [
                'pytest',
                'pytest-pep8'
            ],
            'docs': [
                'sphinx',
                'sphinx_rtd_theme',
                'numpydoc',
            ]
        },

        tests_require=[
            'pytest',
            'pytest-pep8'
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: Plugins',
            'Intended Audience :: Telecommunications Industry',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Multimedia :: Sound/Audio :: Analysis',
            'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'
        ],

        zip_safe=False,
    )
