# Prefer Extension
A command line tool to filter a list of files with duplicates and only keep one filetype. It will use the preferred filetype if more than one exist.

## Usage

```
foo.bar
foo.exe
foo.txt
```

`cat test.txt | prefer-extension -p  '.txt'`

`foo.txt`


