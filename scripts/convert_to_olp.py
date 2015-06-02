# this script converts general files to OLM

# -*- coding: utf-8 -*-
import re

# Headers

reH2Find = re.compile(r'(\n##[^#\n]+)')
# find every line beginning with h2 header ##
# reHeaderFind = re.compile(r'\n#')
# find every line starting with # (includes come comments)
# DANGEROUS, affects code with # comments by removing one 3

# Markdown links

reMarkdownLinkRem = re.compile(r'\[([^\]]+)\]\([^\)]*\)')
# remove: [description](link) -> description
reMarkdownLocalLinkRem = re.compile(r'\[(.+)\]\(#[^\)]*\)')
# remove: [description](#local-link) -> description

# Other links

reJSDocLinkRem = re.compile(r'{@link \S+ (.+)}')
# remove: {@link link description} -> description
reDoublebracketSingleLinkRem = re.compile(r'\[\[([^\]\|]+)\]\]')
# remove:  [[description]] -> description
reDoublebracketLinkRem = re.compile(r'\[\[([^\|]+)\|[^\]]+\]\]')
# remove: [[description|link]] -> description
reOtherLinkRem = re.compile(r'\[(.+)\]\[[^\]]*\]')
# remove: [description][link] -> description
reDoublebracketHTTPLink2MdLink = re.compile(r'\[\[([^\|]+)\|http([^\]]+)\]\]')
# convert: [[description|http...]] -> [description](http...)

# Metadata

reDoublebraceTagRem = re.compile(r'\{\{[#/][^\}]*\}\}')
# remove metadata of these types {{#content}}, {{/content}}

# MDN

reMDNGlossaryRem = re.compile(r'\{\{Glossary\(\"([^\"]+)\"\)\}\}')
# remove: {{Glossary("Term")}} -> Term
reMDNjsxrefDoubleRem = re.compile(r'\{\{jsxref\(\"[^\"]+\", \"([^\"]+)\"\)\}\}')
# remove: {{jsxref("Global_Objects/parseInt", "parseInt()")}} -> parseInt()
reMDNjsxrefRem = re.compile(r'\{\{jsxref\(\"([^\"]+)\"\)\}\}')
# remove: {{jsxref("Number")}} -> Number
reMDNcodeOpenRep = re.compile(r'<pre class=\"brush\: js\">')
# convert: <pre class="brush: js"> -> ```javascript
reMDNcodeCloseRep = re.compile(r'</pre>')
# convert: <pre> -> ```
reMNDLocalLinkRem = re.compile(r'\[([^\]]+)\]\(/[^\)]*\)')
# remove: [description](/internal-link) -> description

# source path

reImgSub = re.compile(r'<img(.+)src=\"img/tutorial/(.+)')
# find image references of this type:
# <img class="diagram" src="img/tutorial/tutorial_00.png">
# and remove "img/tutorial/" from the path

# Leanpub

# reLeanpubCodeRemove = re.compile(r'\n(?:A|W)>([^\n])+')
reLeanpubCodeRemove = re.compile(r'\nW>([^\n])+')
# remove A>, W> from beginning of lines

def convert2Olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''



    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        # BELOW FOR UNDERSTANDING ES6
        # outfile.write(header)
        # fileAsString = infile.read()
        # # fileAsString = fileAsString.split('---',2)[2]
        # #     # remove header between two instances of '---'
        # fileAsString = re.sub(reH2Find, "\n\n<!-- @section -->\n" + r"\1", fileAsString)
        # fileAsString = re.sub(reMarkdownLocalLinkRem, r"\1", fileAsString)
        # fileAsString = re.sub(reLeanpubCodeRemove, r"\1", fileAsString)
        # print "need to debug removing A>, W> etc from code"
        # # fileAsString = re.sub(reDoublebracketHTTPLink2MdLink, r"[\1](http\2)", fileAsString)
        # # fileAsString = re.sub(reDoublebracketSingleLinkRem, r"\1", fileAsString)
        # # fileAsString = re.sub(reDoublebracketLinkRem, r"\1", fileAsString)
        # # fileAsString = re.sub(reDoublebraceTagRem, "", fileAsString)
        # outfile.write(fileAsString)

        outfile.write(header)
        fileAsString = infile.read()
        fileAsString = re.sub(reMDNGlossaryRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefDoubleRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNcodeOpenRep, r"```javascript\n", fileAsString)
        fileAsString = re.sub(reMDNcodeCloseRep, r"```", fileAsString)
        fileAsString = re.sub(reMNDLocalLinkRem, r"\1", fileAsString)

        outfile.write(fileAsString)


generalHeader = """homepage : "http://docs.basho.com/riak/latest/dev/taste-of-riak/"
coverImage : "http://raw.githubusercontent.com/basho/basho_docs/master/source/images/riak-transparent-larger.png"
license : "CC Attribution 3.0"
url : "http://basho.com"
twitter : "basho"
-->
"""
files = []
# files.append({'infile' : '/Users/teppo/Content/understandinges6/manuscript/01-The-Basics.md',
# 'outfile' : '/Users/teppo/Content/nicholaszakas/modules/01-The-Basics.md',
# 'header' : ''})
files.append({'infile' : '/Users/teppo/Content/mdn/modules/re-introduction-raw.md',
'outfile' : '/Users/teppo/Content/mdn/modules/re-introduction.md',
'header' : ''})

for i in range(len(files)):
    convert2Olm(files[i]['infile'], files[i]['outfile'], files[i]['header'])



#
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
