# COMPLAI Web Crawler

TODO: addd GitHub Actions Badge
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setup

1. Activate the Python version you want to use with [pyenv](https://github.com/pyenv/pyenv)

To create a clean Python environment use pyenv, which is a tool to manage different Python versions. If you do not have it on your system already, follow [this](https://realpython.com/intro-to-pyenv/) great guide by Real Python. Then simply run the following commands:

```bash
pyenv install 3.7.7
pyenv global 3.7.7
```

2. Install dependencies with [Poetry](https://python-poetry.org)
Install Poetry by following the install instructions for your OS on their [website](https://python-poetry.org/docs/#installation). Then run the following commands to install the dependecies:

```bash
poetry install
```

3. Install [pre-commit](https://pre-commit.com) hooks from `.pre-commit-config.yaml`

```bash
poetry run pre-commit install
```

## Useful Scrapy Commands

Taken from the excellent
[Scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) from their Docs.

### Creating a project

```shell script
poetry run scrapy startproject tutorial
```

### Create a new spider

```shell script
poetry run scrapy genspider example example.com
```

### Run a spider from the project's top level directory

```shell script
poetry run scrapy crawl example -a kwarg=value -o examples.jl
```

### Use the Scrapy shell to learn how to extract data

- Start the shell

```shell script
poetry run scrapy shell 'http://quotes.toscrape.com/page/1/' --nolog
```

- Select elements from the response

```shell script
response.css('title::text').get()
```

- Open the response page from the shell in your web browser

```shell script
view(response)
```

## Run a spider

From `root/complai_web_crawler dir` run:

```shell script
poetry run spider eur_lex
```

Use `--help` option to see avalaible flags.

## Useful tools and tutorials

- [Scrapy docs tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Using your browser’s Developer Tools for scraping](https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools)
- [SelectorGadget](https://selectorgadget.com/)
- [XPath 1.0 Tutorial](http://zvon.org/comp/r/tut-XPath_1.html)
- [Concise XPath](http://plasmasturm.org/log/xpath101/q)

## TODOs

- Extract more metadata
- Use Scrapinghub
- Add new datasource


## MongoDB

- [Installation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [M001: MongoDB Basics](https://university.mongodb.com/courses/M001/about)
