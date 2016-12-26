# Everknown

Everknown is a command line tool which helps you search your `Evernote/印象笔记` and display notes in plain text.

# Install

```bash
pip install git+https://github.com/evernote/evernote-sdk-python.git
pip install git+https://github.com/Everley1993/Everknown.git
```

# Apply for Developer Token

Evernote: [https://www.evernote.com/api/DeveloperToken.action](https://www.evernote.com/api/DeveloperToken.action)

印象笔记: [https://app.yinxiang.com/api/DeveloperToken.action](https://app.yinxiang.com/api/DeveloperToken.action)

# Usage

```bash
everknown -h

optional arguments:
  -h, --help     show this help message and exit
  --host HOST    service host. Evernote: www.evernote.com, 印象笔记:
                 app.yinxiang.com
  --token TOKEN  developer token
  --words WORDS  words to search. For more search grammer, please see
                 https://dev.evernote.com/doc/articles/search_grammar.php

# example
everknown --host www.evernote.com --token "your token" --words "Hello World"

please enter the number of the note to display
1) 《C++ Hello World!》
2) 《Python Hello World!》
3) 《PHP Hello World!》
:2

《Python Hello World!》
...

# alias everknown for convenience
alias everknown='everknown --host "{service host}" --token "{developer token}" --words '

everknown "Hello World"
```
