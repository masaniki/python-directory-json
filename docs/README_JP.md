# 概要
ディレクトリの入れ子構造をJSONやYAMLで出力します。

# インストール方法
`pip install treejson-cli`

# 実行方法
`treejson <directory>`

ディレクトリの構造をJSONに纏めて、標準出力する。

## Options
`[-f|--file] <output_file>`

".json"(".yaml")ファイルを出力する。

`[-y|--yaml]`

YAML形式で出力する。

`[-a|-all]`

隠しファイル('.'から始まるファイル)を表示する。

## 例
- `treejson tests/root`
  ```
  {"root": [{"parent01": [{"child01_01": ["grandchild01.txt"]}, {"child01_02": []}, "child01_03.txt"]}, {"parent02": [{"child02_01": []}]}]}
  ```
- `treejson tests/root -f tests/output.json`

  [tests/output.json](tests/output.json)

- `treejson tests/root -yf tests/output.yaml`

  [tests/output.yaml](tests/output.yaml)
