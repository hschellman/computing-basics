---
title: Notes on building these pages on MACOS
permalink: How to build these pages
keypoints:
- can build a (flimsy) table of contents
- need a recent version of ruby
--- 

{% include howToBuild.toc.md %}

## Making a table of contents

The scripts `addtoc.sh` calls `code/tocgen.py` to make a table of contents for each episode based on the section headings.  That table is then added using an include of `_includes/<name>.toc.md`. 

The TOC script does not do a good job with named links yet and generally requires that section headings be reasonably simple.


### Things not to do:
- start a section heading with a number - instead use things like "Step 2."
- make very long headings
- put special characters like '()` in your heading

It also currently interprets headings within `<--  -->` comment syntax as real.  If you do make a comment, also indent it. 

## Ruby
on macs you need to use homebrew to install ruby
then you need to override the system version

`export PATH=/opt/homebrew/opt/ruby/bin:$PATH`
