# -*- coding: utf-8 -*-
# Copyright (c) 2015 Tomek Wójcik <tomek@bthlabs.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

import cffi

ffi = cffi.FFI()
ffi.cdef(
    """void notify(char *title, char *subtitle, char *informative_text);"""
)

lib = ffi.dlopen('libosxnotify')


def notify(title, subtitle=None, informative_text=None):
    """Display a notification with *title*, optional *subtitle* and optional
    *informative_text*."""
    title_arg = ffi.new('char[]', title.encode('utf-8'))

    subtitle_arg = ffi.NULL
    if subtitle is not None:
        subtitle_arg = ffi.new('char[]', subtitle.encode('utf-8'))

    informative_text_arg = ffi.NULL
    if informative_text is not None:
        informative_text_arg = ffi.new(
            'char[]', informative_text.encode('utf-8')
        )

    lib.notify(title_arg, subtitle_arg, informative_text_arg)
