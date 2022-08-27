$ restcli_

  restcli is a simple REST client (same as curl).

### Setup

```
cd rest-cli
pipenv --python=3.9
pipenv shell
pipenv install --editable .
```

### Usage:

```
$ restcli hello --help
Usage: restcli hello [OPTIONS] NAME

  Say Hello for given NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --help           Show this message and exit.
```

References

- https://click.palletsprojects.com/en/8.1.x/quickstart/
- https://pymbook.readthedocs.io/en/latest/click.html
- https://requests.readthedocs.io/en/latest/
- https://zetcode.com/python/configparser/
- https://click.palletsprojects.com/en/8.1.x/options/
