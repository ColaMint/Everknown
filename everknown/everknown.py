#!/usr/bin/python
# -*- coding:utf-8 -*-

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from lxml import html
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
    print "please enter the number of the note to display:"
    i = 1
    for note in note_list:
        print "%d) %s" % (i, note.title)
        i += 1
    n = input(":")
    print n
    if type(n) == int and n >= 1 and n <= len(note_list):
        return note_list[n-1]

    return None

def plain_note_content(note_content):
    content = [""]
    root = html.fromstring(note_content)
    def parse_node(node):
        br = False
        printed = False

        if node.tag == "br":
            content[0] += "\n"
            br = True
            printed = True
        elif node.text:
            content[0] += node.text
            printed = True

        for child in node:
            last_br, last_printed =  parse_node(child)

            if last_br:
                br = True

            if last_printed:
                printed = True

        if node.tag == "div" and not br and printed:
            content[0] += "\n"

        return br, printed

    parse_node(root)

    return content[0]

def display_content(content):
    if type(content) == unicode:
        content = content.encode("utf-8")
    process=subprocess.Popen(['less'], stdin=subprocess.PIPE)
    process.communicate(input=content)

def main():
    parser = argparse.ArgumentParser(description="EverKnown")
    parser.add_argument(
        "--host",
        required=True,
        dest="host",
        help="service host")
    parser.add_argument(
        "--token",
        required=True,
        dest="token",
        help="developer token")
    parser.add_argument(
        "--words",
        required=True,
        dest="words",
        help="words to search")
    args = parser.parse_args()

    everknown = EverKnown(args.host, args.token)
    note_list = everknown.search_notes(args.words)
    note_metadata = choose_note(note_list.notes)
    note = everknown.get_note(note_metadata.guid)
    content = plain_note_content(note.content)
    display_content(content)

if __name__ == "__main__":
    # python everknown.py --host app.yinxiang.com --token "S=s51:U=abc2b9:E=1608719cd46:C=1592f68a018:P=1cd:A=en-devtoken:V=2:H=3c70ebbd4f60ba301e00b23ad92dab4d" --words "练习"
    main()
