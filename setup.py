from setuptools import setup, find_packages

setup(
    name='PEC4',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'PEC4=tmdb.__main__:main'
        ]
    },
    package_data={
        '': ['Datos/*', 'testDatos/*', 'tests/Datos/test/*', 'tests/testDatos/*'],
    },
    author='balmore.lopez',
    author_email='blopez73sv@uoc.edu',
    description='Análisis de datos de series de televisión de TMDB',
    url='https://github.com/tu-usuario/tmdb_analysis',
    python_requires='>=3.6',
)
