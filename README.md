# Abstract
It shows the nested directory structure in JSON or YAML.

Japanse document is [here](docs/README_JP.md).

# How to install
`pip install treejson-cli`

## Package Dependencies

- [PyYAML](https://pypi.org/project/PyYAML/): Most popular YAML parser for Python.

# How to run
`treejson <directory>`

The directory structure is compiled into JSON and output to standard output.

## Options
`[-h|--help]`

show help message and exit.

`[-f|--file] <output_file>`

output as a file.

`[-y|--yaml]`

output as a YAML format.

`[-a|-all]`

visit hidden file.

## Examples
- `treejson tests/sample`
  ```
  {'sample': [{'parent01': [{'child01_01': ['grandchild01.txt']}, {'child01_02': ['grandchild02.txt']}, 'child01_03.txt']}, {'parent02': [{'child02_01': ['grandchild02_01.txt']}]}]}
  ```
- `treejson tests/sample -f tests/output.json`

  [tests/output.json](tests/output.json)

- `treejson tests/sample -yf tests/output.yaml`

  [tests/output.yaml](tests/output.yaml)
