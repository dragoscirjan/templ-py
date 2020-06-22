# Python Project

<img alt="Python logo" src="https://github.com/templ-project/python/blob/master/python_logo.png?raw=true" width="20%" align="right" />

> **python** is a template project, designed by [Templ Project](http://templ-project.github.io).
>
> **python** includes instructions for initializing a new [Pyhon](https://python.org) project, and configuring it for
> development, unit testing as well as code linting and analysis.
>
> **python** implements:
>
> - [flake8](https://gitlab.com/pycqa/flake8), [dead](https://github.com/asottile/dead), [radon](https://github.com/yunojuno/pre-commit-xenon) for code analisys
> - [autopep8](https://github.com/hhatto/autopep8), , [pep257](https://github.com/FalconSocial/pre-commit-mirrors-pep257) for code formatting
> - [pylint](https://github.com/PyCQA/pylint), [mypy](https://github.com/pre-commit/mirrors-mypy) for linting


![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3)
[![TravisCI](https://travis-ci.org/templ-project/go.svg?branch=master)](https://travis-ci.org/templ-project/go)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/templ-project/go/issues)

<!-- [![CircleCI](https://circleci.com/gh/templ-project/go.svg?style=shield)](https://circleci.com/gh/templ-project/go) -->

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=templ-project_python&metric=alert_status)](https://sonarcloud.io/dashboard?id=templ-project_python)
[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=templ-project_python&metric=coverage)](https://sonarcloud.io/component_measures/metric/coverage/list?id=templ-project_python)
[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=templ-project_python&metric=bugs)](https://sonarcloud.io/component_measures/metric/reliability_rating/list?id=templ-project_python)
[![SonarCloud Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=templ-project_python&metric=vulnerabilities)](https://sonarcloud.io/component_measures/metric/security_rating/list?id=templ-project_python)

<!--
[![Donate to this project using Patreon](https://img.shields.io/badge/patreon-donate-yellow.svg)](https://patreon.com/dragoscirjan)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UMMN8JPLVAUR4&source=url)
[![Donate to this project using Flattr](https://img.shields.io/badge/flattr-donate-yellow.svg)](https://flattr.com/profile/balupton)
[![Donate to this project using Liberapay](https://img.shields.io/badge/liberapay-donate-yellow.svg)](https://liberapay.com/dragoscirjan)
[![Donate to this project using Thanks App](https://img.shields.io/badge/thanksapp-donate-yellow.svg)](https://givethanks.app/donate/npm/badges)
[![Donate to this project using Boost Lab](https://img.shields.io/badge/boostlab-donate-yellow.svg)](https://boost-lab.app/dragoscirjan/badges)
[![Donate to this project using Buy Me A Coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg)](https://buymeacoffee.com/balupton)
[![Donate to this project using Open Collective](https://img.shields.io/badge/open%20collective-donate-yellow.svg)](https://opencollective.com/dragoscirjan)
[![Donate to this project using Cryptocurrency](https://img.shields.io/badge/crypto-donate-yellow.svg)](https://dragoscirjan.me/crypto)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://dragoscirjan.me/paypal)
[![Buy an item on our wishlist for us](https://img.shields.io/badge/wishlist-donate-yellow.svg)](https://dragoscirjan.me/wishlist)
-->

<!-- TOC -->

- [Python Project](#python-project)
  - [Getting Started](#getting-started)
    - [Prereqiusites / Dependencies](#prereqiusites--dependencies)
      - [For Windows](#for-windows)
      - [For Linux](#for-linux)
    - [Installation](#installation)
    - [Development](#development)
      - [Requirements](#requirements)
        - [For Windows](#for-windows-1)
        - [For Linux/Unix/OSX](#for-linuxunixosx)
    - [Testing](#testing)
      - [Single Tests](#single-tests)
  - [Authors](#authors)
  - [Issues / Support](#issues--support)
  - [License](#license)

<!-- /TOC -->

## Getting Started

### Prereqiusites / Dependencies

#### For Windows

```powershell
# Give Examples
```

#### For Linux

```bash
# Give Examples

apt-get install build-essential mono
npm install -y node-gyp
```

### Installation

- Clone the package, remove `.git` folder, and re-initialize git to your own project

```
git clone 
cd project_name
rm -rf .git
git init
git remote add origin https://github.com/your-user/your-project
```

- Use `make init` to initialize your project

```bash
make init PROJECT=your_project
```

- If you're targeting to write an application and not a module, use `make init MOD=app`

```
make init MODE=app PROJECT=your_project
```

### Development

#### Requirements

- Please install [Python](https://python.org). Project support **python 3.6 and above**.
- Please instal a GoLang IDE
  - [Visual Studio Code](https://code.visualstudio.com/) with [ITMCDev Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=itmcdev.python-extension-pack)
  - [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
  - [Vim](https://www.vim.org/) (see here a [tutorial](https://www.fullstackpython.com/vim.html) for making Vim a Python IDE)
  - Any other IDE you trust.

##### For Windows

- Please install [git-scm](https://git-scm.com/download/win) tool.
- Please install a form of make/cmake
  - Install [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm)
  - Install [make](https://sourceforge.net/projects/ezwinports/files/) from [ezwinports](https://sourceforge.net/projects/ezwinports/files/)
  - Install [chocolatey](https://chocolatey.org/), run `choco install make`
  <!-- - Install [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)
    - You will find it under `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.25.28610\bin\Hostx64` -->

##### For Linux/Unix/OSX

- Please install `git` and `make`

```bash
sudo apt-get install git make -y
```

### Testing

Run unit tests using `make test`.

Testing is currently set to use unittest.

- or you could use `make test TEST_LIB=pytest`
- or you could alter `Makefile.mod.include` to use pytest by default. Just change the commented line as showed:

```makefile
# TEST_LIB=unittest
TEST_LIB=pytest
```

#### Single Tests

Run single unit tests file, by calling `make test-single TEST_PATH=./path/to/file/...`

```bash
make test-single TEST_PATH=./your-project/test/hello.py
```

## Authors

- [Dragos Cirjan](mailto:dragos.cirjan@gmail.com) - Initial work - [Python Template](/templ-project/python)

See also the list of contributors who participated in this project.

## Issues / Support

Add a set of links to the [issues](/templ-project/python/issues) page/website, so people can know where to add issues/bugs or ask for support.

## License

(If the package is public, add licence)
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
