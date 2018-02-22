#!/usr/bin/env python

import sys

HEADER = """
<!doctype html>
<html>
    <head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

	<title>reveal.js</title>

	<link rel="stylesheet" href="css/reveal.css">
	<link rel="stylesheet" href="css/theme/black.css">

	<!-- Theme used for syntax highlighting of code -->
	<link rel="stylesheet" href="lib/css/zenburn.css">

	<!-- Printing and PDF exports -->
	<script>
	    var link = document.createElement( 'link' );
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
document.getElementsByTagName( 'head' )[0].appendChild( link );
	</script>
    </head>
    <body>
	<div class="reveal">
	    <div class="slides">
"""

FOOTER = """
	    </div>
	</div>

	<script src="lib/js/head.min.js"></script>
	<script src="js/reveal.js"></script>

	<script>
	    // More info about config & dependencies:
	    // - https://github.com/hakimel/reveal.js#configuration
	    // - https://github.com/hakimel/reveal.js#dependencies
	    Reveal.initialize({
			      dependencies: [
				  { src: 'plugin/markdown/marked.js' },
				  { src: 'plugin/markdown/markdown.js' },
				  { src: 'plugin/notes/notes.js', async: true },
				  { src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } }
			      ]
	    });
	</script>
    </body>
</html>
"""

f = open("middle.html", "r")
middle = f.read()
f.close()

from twisted.web import microdom
changes = False
dom = microdom.parseString("<xml>" + middle + "</xml>", beExtremelyLenient=1)
orig_middle = middle
dom = dom.childNodes[0].childNodes
if "last" in sys.argv:
    dom = [dom[-1]]
    changes = True
if "last-inner" in sys.argv:
    dom = [dom[0].childNodes[-1]]
    changes = True
middle = '\n'.join([i.toxml() for i in dom])
if not changes:
    middle = orig_middle
data = HEADER + middle + FOOTER
f = open("index.html", "w")
f.write(data)
f.close()
