# this script converts Riak docs to OLM

# -*- coding: utf-8 -*-
import re

def convertRiak2Olm(oldfile, newfile, metadataString):
    '''\
    Filter away all the Riak specific syntax
    '''

    reDoublebracketLinkRem = re.compile(r'\[\[([^\|]+)\|[^\]]+\]\]')
    # remove links of these types
    # [[description|link]]
    reJSDocLinkRem = re.compile(r'{@link \S+ (.+)}')
    # remove links of these types
    # {@link ng.directive:ngApp ngApp}
    reMarkdownLinkRem = re.compile(r'\[(.+)\]\(.*\)')
    # remove links of these types (used for external links)
    # [description](link)
    reOtherLinkRem = re.compile(r'\[(.+)\]\[.*\]')
    # remove links of these types
    # [description][link]
    reImgSub = re.compile(r'<img(.+)src=\"img/tutorial/(.+)')
    # find image references of this type:
    # <img class="diagram" src="img/tutorial/tutorial_00.png">
    # and remove "img/tutorial/" from the path
    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
        outfile.write(metadataString)
        headerLimiterCount = 0
        while headerLimiterCount < 2:
            nextLine = infile.readline()
            if nextLine[0:3] == '---':
                headerLimiterCount += 1
        for line in infile:
            if line[0:3] == '## ': # add sections after every h2 heading
                outfile.write("<!-- @section -->\n\n")
            if line[0] == '#': # remove one '#'-character from each heading
                line = line[1:]
            if reDoublebracketLinkRem.search(line):
                print line
                m = reDoublebracketLinkRem.search(line)
                line = reDoublebracketLinkRem.sub(m.group(1), line)
            # # if reMarkdownLinkRem.search(line): # do not remove external links
            # #     m = reMarkdownLinkRem.search(line)
            # #     line = reMarkdownLinkRem.sub(m.group(1), line)
            # if reOtherLinkRem.search(line):
            #     m = reOtherLinkRem.search(line)
            #     line = reOtherLinkRem.sub(m.group(1), line)
            # if reImgSub.search(line):
            #     m = reImgSub.search(line)
            #     line = reImgSub.sub('<img'+m.group(1)+'src=\"https://raw.githubusercontent.com/outlearn-content/angular-tutorial/master/assets/'+m.group(2), line)
            # if "<ul doc-tutorial-nav" in line:
            #     continue
            # if "<div doc-tutorial-reset" in line:
            #     continue
            outfile.write(line)

generalMetadata = """homepage : "https://github.com/basho/basho_docs/tree/master/source/languages/en/riak"
author : "Basho Technologies, Inc."
license : "CC Attribution 3.0"
url : "http://basho.com"
twitter : "basho"
-->
"""
files = []
files.append({
'infile' : './theory/why-riak.md',
'outfile' : '/Users/teppo/Content/taste-of-riak/modules/why-riak.olm',
'metadataString' : """<!--
name: why-riak
version : "0.1"
title : "Why Riak"
description: "Explain what Riak is and what problems it is designed to solve."
""" + generalMetadata
})

convertRiak2Olm(files[0]['infile'], files[0]['outfile'], files[0]['metadataString'])

#     reJSDocLinkRem = re.compile(r'{@link \S+ (.+)}')
#     # remove links of these types
#     # {@link ng.directive:ngApp ngApp}
#     reOtherLinkRem = re.compile(r'\[(.+)\]\[.*\]')
#     # remove links of these types
#     # [description][link]
#     reImgSub = re.compile(r'<img(.+)src=\"img/tutorial/(.+)')
#     # find image references of this type:
#     # <img class="diagram" src="img/tutorial/tutorial_00.png">
#     # and remove "img/tutorial/" from the path
#     with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
#         for i in range(5): #remove first 5 lines that include ngdoc tags
#             infile.next()
#         for line in infile:
#             if "<ul doc-tutorial-nav" in line:
#                 continue
#             if "<div doc-tutorial-reset" in line:
#                 continue
#             if reJSDocLinkRem.search(line):
#                 m = reJSDocLinkRem.search(line)
#                 line = reJSDocLinkRem.sub(m.group(1), line)
#             if reOtherLinkRem.search(line):
#                 m = reOtherLinkRem.search(line)
#                 line = reOtherLinkRem.sub(m.group(1), line)
#             if reImgSub.search(line):
#                 m = reImgSub.search(line)
#                 line = reImgSub.sub('<img'+m.group(1)+'src=\"https://raw.githubusercontent.com/outlearn-content/angular-tutorial/master/assets/'+m.group(2), line)
#             outfile.write(line)
#
#
#
#
# # indices = ['00','01','02','03','04','05','06','07','08','09','10','11','12']
# # for index in indices:
# #     oldfile = 'step_'+index+'.ngdoc'
# #     newfile = 'step_'+index+'.md'
# #     convertNgdoc2Md(oldfile, newfile)
#
# convertNgdoc2Md('index.ngdoc', 'index.md')
# # convertNgdoc2Md('the_end.ngdoc', 'the_end.md')
