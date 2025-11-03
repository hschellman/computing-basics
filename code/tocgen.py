import os,sys,string

def dealwithline(input,toclines):
    for line in input:
        if line.startswith('{% include'): 
            print ("dealing with include",line)
            includename = line.split('%')[1].strip().split(' ')[1]
            newfile = os.path.join("_includes/",includename)
            newlines = open(newfile,'r').readlines()
            dealwithline(newlines,toclines)
            continue
        # remove any labels
        # if "<a" in line:
        # line = line.split(' <a')[0]
        level = 1
        name = ""
        indent = ''
        if line.startswith('####'):
            level = 3
            name = line[4:].strip()
            indent = '   '*2
        elif line.startswith('###'):
            indent = '   '*1
            name = line[3:].strip()
        elif line.startswith('##'):
            level = 1
            name = line[2:].strip()
        else:
            continue
        # if labeled get the label name
        if "<a" in line:
            linkname = line.split(' <a')[1].strip().split("name=\"")[1].split('"')[0]
        else: 
            linkname=name.lower().strip().replace('?','').replace(' ',"-")
        print (level,indent,name,linkname)


        newline = '%s- [%s](#%s)' % (indent,name,linkname)
        toclines.append(newline)
        print (newline)
    return toclines
mdname= sys.argv[1]
inputmd = open(mdname,'r')
newname = os.path.join("_includes/",os.path.basename(mdname[:-3])+'.toc.md')
newtoc = open(newname,'w')
input = inputmd.readlines()
inputmd.close()
toclines = []
toclines.append('## Table of Contents')
dealwithline(input,toclines)
newtoc.write('\n'.join(toclines))
newtoc.close()