# 仕様

- 指定するディレクトリ名は相対パスでも絶対パスでもOK.

- 隠しファイルとは`.`から始まるファイルやディレクトリのことである。

- 空のディレクトリは`{directory_name: []}`で表す。

- 深さ0の時はカレントディレクトリのみを表示する。

# EBNF

## 前提

`?string?`は文字列を表す。

`?decimal?`は10進数の数字を表す。

## 構文

treejson_command = "treejson" args

args = help_or_version | directory_args

help_or_version = "-h" | "-v"

directory_args = ["-a"] ["-y"] ["-f" file] ["-d" depth] directory_name

directory_name = ?string?

file = ?string?

depth = ?decimal?
