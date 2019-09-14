# "TDD in Python with pytest" workshop

This is a Python package used for the "TDD in Python with pytest" workshop.
The `master` branch contains an empty project with no tests. The `develop` branch points to the full project, and each commit is a step in the workshop. The commit messages are prefixed with either "T" or "C", to show if that commit adds "Tests" or "Code".

The description of the project is the following:

``` txt
The goal is to write a class Calc that performs calculations: addition, subtraction,
multiplication, and division. Addition and multiplication shall accept multiple arguments.
Division shall return a float and division by zero shall return the string "inf".
Multiplication by zero must raise a ValueError exception. The class will also provide
a function to compute the average of an iterable. This function gets two optional upper
and lower thresholds to remove outliers.
```

(some of the requirements are silly but they help understanding some TDD concepts)

## Instructions

Windows users, please change all `/` to `\`

1. Clone the repository
2. 1. Create a virtual environment - pip: `python3 -m venv <venvname>` (where <venvname> is the name of the environment, e.g. `myvenv`)
   1. Create a virtual environment - Conda: `conda create --name <venvname>` (where <venvname> is the name of the environment, e.g. `myvenv`)
3. 1. Activate it - pip: `source <venvname>/bin/activate`
   1. Activate it - Conda: `conda activate <venvname>`
4. Shift directory to where the cloned repo is stored
5. Install requirements: `pip install -r requirements/dev.txt`
6. Edit the `pytest.ini` file and add the virtualenvironment to the `norecursedirs` option

``` ini
[pytest]
minversion = 2.0
norecursedirs = .git .tox requirements* <venvname>
python_files = test*.py
```

6. Run `pytest -svv` to check that everything has been correctly installed. You should get a result like

``` txt
==================================== test session starts ====================================
platform linux -- Python 3.6.6, pytest-3.0.7, py-1.7.0, pluggy-0.4.0 -- <PWD>
cachedir: .cache
rootdir: <PWD>, inifile: pytest.ini
plugins: cov-2.4.0
collected 0 items

=============================== no tests ran in 0.01 seconds ================================
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [lgiordani/cookiecutter-pypackage](https://github.com/lgiordani/cookiecutter-pypackage) project template.
