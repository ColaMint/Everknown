# EverKnown

EverKnown is a command line tool which helps you search your `EverNote` and display notes in plain text.

# Install

```bash
pip install git+https://github.com/Everley1993/EverKnown.git
```

# Apply for EverNote Developer Token

EverNote: [https://www.evernote.com/api/DeveloperToken.action](https://www.evernote.com/api/DeveloperToken.action)

印象笔记: [https://app.yinxiang.com/api/DeveloperToken.action](https://app.yinxiang.com/api/DeveloperToken.action)

# Usage

```bash
everknown -h

optional arguments:
  -h, --help     show this help message and exit
  --host HOST    service host. EverNote: www.evernote.com, 印象笔记:
                 app.yinxiang.com
  --token TOKEN  developer token
  --words WORDS  words to search. For more search grammer, please see
                 https://dev.evernote.com/doc/articles/search_grammar.php

# example
everknown --host www.evernote.com --token "S=s51:U=abc2b9:E=1608719cd46:C=1592f68a018:P=1cd:A=en-devtoken:V=2:H=3c70ebbd4f60ba301e00b23ad92dab4d" --words "Hello World"

please enter the number of the note to display
1) 《C++ Hello World!》
2) 《Python Hello World!》
3) 《PHP Hello World!》
:2

《Python Hello World!》
...
```

# Alias


```bash
# alias everknown for convenience
alias everknown='everknown --host {service host} --token {developer token} --words '

everknown "Hello World"
```
