# Development Environment #

This chapter describes how to setup the development environment (DevEnv) properly.

[Visual Studio Code](https://code.visualstudio.com/) is used as default DevEnv.
Therefore this documentation is based on VSCode.
Of course all of these steps can be done in other environments, too.

## Extensions ##

You should install following extensions for VSCode.

|extension|author|ID|
|- |- |- |
|Python |Microsoft |ms-python.python |
|Python Debugger|Microsoft |ms-python.debugpy|
|Pylint| Microsoft| ms-python.pylint|
|Code Spell Checker| Stree Side Software| streetsidesoftware.code-spell-checker|
|autoDocstring| Nils Werner| njpwerner.autodocstring|

## Setup Python venv ##

A Python virtual environment is used to get an encapsulated environment to install
required pip packages in the specified version.
The following steps are taken from the VSCode [documentation](https://code.visualstudio.com/docs/python/environments).

1. open the Command Palette (*Ctrl+Shift+P*), search for the **Python: Create Environment** command, and select it
2. select **Venv** as environment type
3. select the python interpreter used as a base to create the new virtual environment
4. select **requirements.txt** and **requirements_devenv.txt** to install all required dependencies