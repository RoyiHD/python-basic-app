#### Python Backend App Setup
This suggested setup is designed for backend applications. It is mainly focused on 
testing routes and using the test clients.
It is recommended to use Python 3.10 and higher


### Installation 
Run the following command to install dependency into a virtual environment

```sh
pip install .
```

### TESTING
the -v increases verbosity, you can see the pytest commands with pytest --help

```sh
pytest -v
```

#### CLI

### Invoke cli with arguments
Invoking the cli with a required input

```sh
python project/cli/arguments.py helo.txt
```

### invoke cli with options
Invoking the cli passing in some input
```sh
python project/cli/options.py --file helo.txt
```

### invoke cli with groups
Groups allow us to package multiple cli commands in a single file
The first parameter is the command we want to invoke withint the group
The second paramenter is the options name 
The third paramenter is the input for ther option


```sh
python project/cli/group.py search -s hi
```

```sh
python project/cli/group.py run --run True
```

#### LINTING AND TYPING

### Run linter

This command will run all pylint on all .py files in your project. 
Note that pylint takes the configuration from .pylintrc but we can more the configuration to setup.cfg
https://pylint.readthedocs.io/en/latest/tutorial.html

```sh
pylint .
```

you can alos check specific files
```sh
pylint app.py
```

### Run type checking

This command will run type chekcing on your .py files
!! Mypy will not check unannotated python functions and variables. Make sure to annotate your code.
I recommend getting familir with Dynamic vs Static typing in Python as well as using Protocol
https://peps.python.org/pep-0544/

```sh
mypy .
```