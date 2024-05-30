#!/usr/bin/env python

import sys
from os import path
import re

class StringUtils:
    strings = ""
    wordlists = []

    def __init__(self):
        pass

    def setString(self, strings):
        self.strings = strings

    def splitStringBySpaces(self, strings):
        self.wordlists = strings.strip().split()
        return self.wordlists, [x.span() for x in re.finditer('[^\s]+', strings)]


# test
# sentence = "Saya makan bakso bersama dia di Malioboro."
# s = StringUtils()

# print(s.splitStringBySpaces(sentence))
