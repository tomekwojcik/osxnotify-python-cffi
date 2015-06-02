osxnotify-cffi
==============

No nonsense OS X notifications for Python scripts (CFFI wrapper).

About
-----

osxnotify-cffi is a wrapper for libosxnotify_. It allows Python scripts to
display native OS X notifications.

This module uses CFFI to interface *libosxnotify*. For a native C extension
based module see `osxnotify`_.

Requirements
------------

* OS X >= 10.9.4 - should work on Mountain Lion but it's not tested,
* Python 2.7 or 3.4,
* libosxnotify >= 1.0,
* Xcode and command line utilities.

Installation
------------

To install osxnotify-cffi from PyPI, issue the following command:

.. sourcecode:: console

    $ pip install osxnotify-cffi

Alternatively, you can install from the source code:

.. sourcecode:: console

    $ git clone https://github.com/tomekwojcik/osxnotify-python-cffi.git
    $ cd osxnotify-python-cffi
    $ python setup.py install

Usage
-----

.. sourcecode:: python

    import osxnotify-cffi

    osnotify-cffi.notify('Title', subtitle='Subtitle', informative_text='Informative text')

Issues and limitations
----------------------

UTF-8 is the only supported text encoding.

Project status
--------------

This project should be considered **beta**. Proceed with caution if you decide
to use osxnotify-cffi in production.

License
-------

osxnotify-cffi is licensed under MIT License.

Author
------

osxnotify-cffi was written by `Tomek Wójcik`_.

Source code and issues
----------------------

Source code is available on GitHub at: `tomekwojcik/osxnotify-python-cffi`_.

To file issue reports and feature requests use the project's issue tracker on
GitHub.

.. _libosxnotify: http://tomekwojcik.github.io/libosxnotify/
.. _osxnotify: https://pypi.python.org/pypi/osxnotify
.. _Tomek Wójcik: http://www.tomekwojcik.com/
.. _tomekwojcik/osxnotify-python-cffi: https://github.com/tomekwojcik/osxnotify-python-cffi
