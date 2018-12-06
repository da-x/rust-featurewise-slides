#!/bin/bash

set -e

sed -E 's#`([^`]*)`#<code class="hljs-i">\1</code>#g' -i $1
