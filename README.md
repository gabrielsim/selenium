# Getting started with Selenium

This is a template for a Selenium Project with several enhancements:

* Uses a random proxy provided by [gimmeproxy](https://gimmeproxy.com/) each time it is run

* Selenium Chrome Driver with [uBlock](https://www.ublock.org/) to get rid of annoying ads

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Ensure you have [Python 2.7.*](https://www.python.org/downloads/) on your machine with pip installed.

2. Install [Selenium](https://www.seleniumhq.org/download/) with pip
```
pip install selenium
```

3. Intall [requests](https://pypi.python.org/pypi/requests) with pip
```
pip install requests
```

4. Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) to the root of this project folder

5. uBlock Chrome extension [uBlock-Origin_v1.14.24.crx](uBlock-Origin_v1.14.24.crx) has been added for you in this project, but feel free to replace/upgrade it.

## Running Selenium
```
python run.py
```

## Contributing
Please feel free to submit pull requests.

## Acknowledgments

* [Selenium with Python](http://selenium-python.readthedocs.io/)

* [Official Selenium Documentation](https://seleniumhq.github.io/selenium/docs/api/py/api.html)
