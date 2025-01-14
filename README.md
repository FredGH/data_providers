# Project Title

Data Providers

## Description

Provides access to external data providers data, such as yahoo financial data.

## Getting Started

### Dependencies

* N/A

### Installing

* Git clone the project
    * git clone https://github.com/FredGH/data_providers.git
* Create the Python Env
    * rm -rf venv/
    * In Visual Studio Vode -> Ctrl+Shift+P -> select python 3.11.x
    * python3 -m venv venv
    * source ./venv/bin/activate
* Install Requirements:
    * python3 -m pip install --upgrade pip
* Build Package:    
    * pip3 install -U pip setuptools
    * python3 setup.py sdist bdist_wheel
    * pip3 install -e .
    * [optional] pip install -Iv urllib3==1.26.15
* Tag New Release & Push:
    * git tag 0.0.x -m "Release details"
    * git push origin 0.0.x
    * git push
* Install Package:
    *  Go to Settings > Developer Settings > Personal access tokens (classic) > Generate new token with note e.g. "Upload package"
    *  Ensure you check the write:packages scope to grant the necessary permissions.
    * Get the generated token, e.g. "12345"
    * Get your Github user name, e.g. "my_user_name"
    * Install the private package using the following:
        * Template:
            * pip install git+https://github.com/{{ username }}/{{ package name }}.git@{{ tag/version }}
            * [Optional] pip install git+https://{{ your access token }}@github.com/{{ username }}/{{ repository name}}.git@{{ tag/version }}#egg={{ package name }}
        * Example:
            * pip install git+https://github.com/{{ username }}/data_providers.git@0.0.x
            * [Optional] pip install git+https://12345@github.com/{{ username }}/data_providers.git@0.0.x#egg=data_providers    
    * [Optional] Deleting tags:
        * List tags: git tag -l
        * Delete origin: git push origin :refs/tags/{{tagname}} (e.g. 0.01)
        * Delete locally: git tag --delete {{tagname}} (e.g. 0.01)
### Executing program



* N/A

## Help

* N/A

## Authors

Contributors names and contact info
freddy.marechal@gmail.com

## Version History

* 0.0.1
    * TBC

## License

* There is no license.

## Acknowledgments

Inspiration, code snippets, etc.
* [Create and Release Private Python Package On Github](https://dev.to/abdellahhallou/create-and-release-a-private-python-package-on-github-2oae)
