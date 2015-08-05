# this script has several functions to produce OLP
# olpFromToc converts Node.js TOC to olp sections
# removeLinks removes all the links from the markdown files

# -*- coding: utf-8 -*-
import re
import os

def olpFromToc():
    '''\
    Create outlearn.json from toc
    '''

    reExtractTitleFile = re.compile(r'\* \[(.+)\]\((.+).html\)')
    # extract titles and filenames of different sections
    # * [About these Docs](documentation.html)

    with open('output.json', 'w') as outfile, open('_toc.md', 'r') as infile:
        for line in infile:
            if reExtractTitleFile.search(line):
                m = reExtractTitleFile.search(line)
                lines = [
                "{\n",
                "  \"title\": \""+m.group(1)+"\",\n",
                "  \"location\": \"sections/"+m.group(2)+".md\"\n",
                "},\n"
                ]
            outfile.writelines(lines)

def cleanMarkdown(oldfile, newfile):
    '''\
    Filter away all the ngdoc specific syntax
    '''

    reLinkRem = re.compile(r'\[(.+)\]\([a-z_]*\.html.*\)')
    # remove links of these types
    # [web server](http.html)
    # [kMaxLength](smalloc.html#smalloc_smalloc_kmaxlength)

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
        for i in range(1): # remove title line
            infile.next()
        for line in infile:
            if reLinkRem.search(line):
                m = reLinkRem.search(line)
                line = reLinkRem.sub(m.group(1), line)
            outfile.write(line)


files = os.listdir('.')
for oldfile in files: # loop over all the files in the directory
    if 'markdown' in oldfile: # clean .markdown files
        newfile = oldfile[:-8]+'md'
        cleanMarkdown(oldfile, 'output/'+newfile)

# olpFromToc()
