import sys,os 

table = os.path.join('_includes','all_toc.md')
out = open(table,'w')
files = os.listdir('./_includes')
files.sort()
for file in files:
    print (file)
    if file.endswith('.toc.md'):
        filename = os.path.basename(file)
        out.write("%s\n" % '{% include '+filename+' %}')
        