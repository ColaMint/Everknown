#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from html2text import html2text
import subprocess
import argparse

class EverKnown(object):

    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.client = EvernoteClient(service_host=host, token=token)
        self.note_store = self.client.get_note_store()

    def search_notes(self, words):
        filter = NoteFilter(words=words)
        spec = NotesMetadataResultSpec()
        spec.includeTitle = True
        note_list = self.note_store.findNotesMetadata(self.token, filter, 0, 100, spec)
        return note_list

    def get_note(self, guid):
        note = self.note_store.getNote(self.token, guid, True, False, False, False)
        return note

def choose_note(note_list):
    print "please enter the number of the note to display"
    i = 1
    for note in note_list:
        print "%d) 《%s》" % (i, note.title)
        i += 1
    n = input(":")
    if type(n) == int and n >= 1 and n <= len(note_list):
        return note_list[n-1]

    return None

def display_note(note):
    title = note.title.encode("utf-8") \
            if type(note.title) == unicode \
            else note.title
    html = note.content.encode("utf-8") \
            if type(note.content) == unicode \
            else note.content
    plain_text = "《%s》\n\n%s" % (title, html2text(html))
    process=subprocess.Popen(['less'], stdin=subprocess.PIPE)
    process.communicate(input=plain_text)

def main():
    parser = argparse.ArgumentParser(description="EverKnown")
    parser.add_argument(
        "--host",
        required=True,
        dest="host",
        help="service host. EverNote: www.evernote.com, 印象笔记: app.yinxiang.com")
    parser.add_argument(
        "--token",
        required=True,
        dest="token",
        help="developer token")
    parser.add_argument(
        "--words",
        required=True,
        dest="words",
        help="words to search. For more search grammer, please see https://dev.evernote.com/doc/articles/search_grammar.php")
    args = parser.parse_args()

    try:
        everknown = EverKnown(args.host, args.token)
        note_list = everknown.search_notes(args.words)
        if not note_list.notes:
            print "No note matches."
            return
        note_metadata = choose_note(note_list.notes)
        if note_metadata is None:
            return
        note = everknown.get_note(note_metadata.guid)
        display_note(note)
    except KeyboardInterrupt as e:
		pass
    except Exception as e:
        print e


if __name__ == "__main__":
    main()
