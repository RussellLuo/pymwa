PyMWA
=====

MetaWeblog API (MWA) implemented in Python.

1| Motivation
-------------

It's boring and inefficient to deliver posts in a WYSIWYG editor of the blog system. We should enjoy our lives by using MetaWeblog API (MWA). Now this is implemented in Python, you can use the scripts here to publish an article just in seconds.

2| Configuration
----------------

Just open `config.py`, then modify the dictionary `config` with your own information.

3| Usage
--------

Make `publish.py` executable:

    $ chmod +x publish.py
    
If you have a Markdown-format post (e.g. `hello_world.md`), you can publish it locally by one command:

    $ ./publish.py -md hello_world.md

If you have a HTML-format post (e.g. `hello_world.html`), you can also publish it locally by one command:

    $ ./publish.py -html hello_world.html

4| Feedback
-----------

Advices and improvements are appreciated.
