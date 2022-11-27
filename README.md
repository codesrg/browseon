# Online

[![PyPI](https://img.shields.io/pypi/v/online)](https://pypi.python.org/pypi/online)
[![Pypi - License](https://img.shields.io/github/license/codesrg/online)](https://github.com/codesrg/online/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/online?color=red)](https://pypi.python.org/pypi/online)

To browse web.

## Installation

`pip install -U online`

## Usage

```
usage: online [options]

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show version number and exit.

to browse web:
  -q , --query    query to search
  -u , --url      url to open
  -e , --engine   search engine to search (Optional)
```

### Python Script

To browse web.

```python
from online import browse

browse.open('scheme://sub-domain.domain.top-level-domain/')  # to open url
browse.search("pypi online")  # to search query
```

### Command Line

To search in web browser.

```
$ online --query "pypi online"
```

## Issues:

If you encounter any problems, please file an [issue](https://github.com/codesrg/online/issues) along with a detailed
description.