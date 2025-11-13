# 概要
ディレクトリの入れ子構造をJSONやYAMLで出力します。

# インストール方法
`pip install treejson-cli`

## パッケージ依存性

以下のpackageをインストールしないと正しく機能しない場合があります。

- [PyYAML](https://pypi.org/project/PyYAML/): 最も人気なPyhton用のYAMLパーサーです。

# 実行方法
`treejson <directory>`

ディレクトリの構造をJSONに纏めて、標準出力する。

## Options

詳細仕様は[ここ](formal_document_JP.md)にあります。

`[-h|--help]`

helpを表示する。

`[-v|--version]`

versionを表示する。

`[-y|--yaml]`

YAML形式で出力する。

`[-a|--all]`

隠しファイル('.'から始まるファイル)を表示する。

`[-d|--depth] <depth>`

探索の深さを指定する。

深さ0の時はカレントディレクトリのみを表示する。

`[-f|--file] <output_file>`

".json"(".yaml")ファイルを出力する。

## 例
- `treejson tests/sample`
  ```
  {'sample': [{'parent01': [{'child01_01': ['grandchild01.txt']}, {'child01_02': ['grandchild02.txt']}, 'child01_03.txt']}, {'parent02': [{'child02_01': ['grandchild02_01.txt']}]}]}
  ```
- `treejson tests/sample -f tests/output.json`

  [tests/output.json](../tests/output.json)

- `treejson tests/sample -yf tests/output.yaml`

  [tests/output.yaml](../tests/output.yaml)

# 追記

`tree -J`というコマンドでJSON表示できるらしい。

