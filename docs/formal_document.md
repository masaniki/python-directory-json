# Discription

- The directory name can be either a relative path or an absolute path.

- A hidden file or directory is a file or directory which starts with `.`. 

- An empty directory is represented by `{directory_name: []}`.

- If depth is 0, it shows only current directory.

# EBNF

## Special Symbols

- `?string?` represents character string.

- `?decimal?` represents decimal integer. It is not negative.

## Syntax

```
treejson_command = "treejson" args

args = help_or_version | directory_args

help_or_version = "-h" | "-v"

directory_args = ["-a"] ["-y"] ["-f" file] ["-d" depth] directory_name

directory_name = ?string?

file = ?string?

depth = ?decimal?
```
