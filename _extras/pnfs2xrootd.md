---
title: pnfs2xrootd
permalink: pnfs2xrootd
--- 

~~~
#!/bin/sh

# This takes a path that you could "ls" in
# /pnfs and puts it in a format that ROOT or ART can understand. Can accept
# multiple arguments.

while true
do
echo -n `readlink -f $1` | sed -e 's%/pnfs%root://fndca1.fnal.gov:1094//pnfs/fna
l.gov/usr%'
shift
if [ x$1 == x ]; then break; fi
echo -n ' '
done

echo
~~~
{: ..language-bash}