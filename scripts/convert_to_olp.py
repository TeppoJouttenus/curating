# this script converts general files to OLM

# -*- coding: utf-8 -*-
import re
import files
import textwrap

files = files.ng_files

# Headers

reH2Find = re.compile(r'(\n##[^#\n]+\n)') # find every line beginning with h2 header ##
reH1Find = re.compile(r'(\n#[^#\n]+\n)') # find every line beginning with h1 header #
reNewlineFind = re.compile(r'\n') # find every newline
# reHeaderFind = re.compile(r'\n#')
"""find every line starting with # (includes come comments)
 DANGEROUS, affects code with # comments by removing one #
"""

# Markdown links

reMarkdownLinkRem = re.compile(r'\[([^\]]+)\]\([^\)]*\)')
# remove: [description](link) -> description
reMarkdownLocalLinkRem = re.compile(r'\[(.+)\]\(#[^\)]*\)')
# remove: [description](#local-link) -> description

# Other links

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
reMDNcodeOpenConvert = re.compile(r'<pre class=\"brush\: js\">')
# convert: <pre class="brush: js"> -> ```javascript
reMDNcodeCloseConvert = re.compile(r'</pre>')
# convert: <pre> -> ```
reMNDLocalLinkRem = re.compile(r'\[([^\]]+)\]\(/[^\)]*\)')
# remove: [description](/internal-link) -> description

# Leanpub

# reLeanpubCodeRemove = re.compile(r'\n(?:A|W)>([^\n])+')
reLeanpubCodeRemove = re.compile(r'\nW>([^\n])+')
# remove A>, W> from beginning of lines

# JSDoc / ngdoc

reJSDocLinkRem = re.compile(r'{@link\s+\S+\s+([^\}]+)}')
# remove: {@link link description} -> description
reJSDocLocalLinkRem = re.compile(r'<a name=[^>]+>([^<]+)</a>')
# remove: {@link link description} -> description
reJSDocExampleTagRem = re.compile(r'</?example[^>]*>\n')
# remove: <example ... > and </example>
reJSDocCodeOpenConvert = re.compile(r'<file[^>]*name="([^"]*)"[^>]*>\n')
# convert: <file name="index.html"> -> ``` etc.
reJSDocCodeCloseConvert = re.compile(r'</file>\n')
# convert: </file> -> ```
reJSDocAlertConvert = re.compile(r'<div class="alert[^>]*>\n')
# remove: <example ... > and </example>
reJSDocSpaceJsBlock = re.compile(r'\n```js')
# remove: <example ... > and </example>
reJSDocImgPath = re.compile(r'<img[^>]+src=\"([^\"]+)\"[^>]*>')
# convert <img ... src="path"> -> <img src="github path">






def convertJSDoc2olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        outfile.write(header)
        fileAsString = infile.read()
        fileAsString = fileAsString.split('\n',4)[4]
            # remove first 4 lines which have header info
        fileAsString = reH1Find.sub("\n\n<!-- @section -->\n" + r"\1", fileAsString)
        fileAsString = reH2Find.sub("\n\n<!-- @section -->\n" + r"\1", fileAsString)
        fileAsString = reJSDocLinkRem.sub(r'\1', fileAsString)
        fileAsString = reJSDocLocalLinkRem.sub(r'\1', fileAsString)
        fileAsString = cleanUpExampleCode(fileAsString)
        fileAsString = convertAlerts(fileAsString)
        fileAsString = reJSDocSpaceJsBlock.sub(r'\n\n```js', fileAsString)
        fileAsString = reJSDocImgPath.sub(r'<img src="https://raw.githubusercontent.com/outlearn-content/angular/master/\1">', fileAsString)
        outfile.write(fileAsString)


def cleanUpExampleCode(input):
    '''\
    Turn angular example code blocks into Markdown
    '''

    modifiedInput = input
    while modifiedInput.find('<example') != -1: # loop over all <example> tags
        startExample = modifiedInput.find('<example')
        endExample = modifiedInput.find('</example') + 11
        exampleBlock = modifiedInput[startExample:endExample]
        exampleBlock = reJSDocExampleTagRem.sub(r'', exampleBlock)
            # remove <example> tags from the block

        while exampleBlock.find('<file') != -1:
        # loop over all <file> tags inside the exampleBlock
            startFile = exampleBlock.find('<file')
            endFile = exampleBlock.find('</file') + 8
            fileBlock = exampleBlock[startFile:endFile]

            # if there is a <file> block, find the fileName and tags
            match = reJSDocCodeOpenConvert.search(exampleBlock)
            if match:
                fileName = match.group(1)
            else:
                break
            fileBlock = reJSDocCodeOpenConvert.sub(r'',fileBlock)
            fileBlock = reJSDocCodeCloseConvert.sub(r'',fileBlock)

            # recreate the code with markdown syntax
            exampleBlock = (exampleBlock[:startFile] + '\n_Example file_: `' +
                fileName + '`\n\n```javascript\n' +
                textwrap.dedent(fileBlock) + '```\n\n' + exampleBlock[endFile:])

        # recreate the code with the cleaned up exampleBlock
        modifiedInput = (modifiedInput[:startExample] + exampleBlock +
            modifiedInput[endExample:])

    return modifiedInput

def convertAlerts(input):
    '''\
    Turn angular alerts into block quotes
    '''

    modifiedInput = input
    while modifiedInput.find('<div class="alert') != -1: # loop over all alerts tags
        start = modifiedInput.find('<div class="alert')
        relativeEnd = modifiedInput[start:].find('</div>') + 7
        end = start + relativeEnd
        alertBlock = modifiedInput[start:end]
        alertBlock = reJSDocAlertConvert.sub(r'> ', alertBlock)
            # remove <example> tags from the block
        alertBlock = alertBlock[:-8] # remove </div> from the end
        alertBlock = reNewlineFind.sub(r'\n>', alertBlock)
        # recreate the input with cleaned up alertBlock
        modifiedInput = (modifiedInput[:start] + alertBlock + '\n' +
            modifiedInput[end:])

    return modifiedInput

def convert2olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        outfile.write(header)
        fileAsString = infile.read()
        fileAsString = re.sub(reMDNGlossaryRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefDoubleRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNcodeOpenConvert, r"```javascript\n", fileAsString)
        fileAsString = re.sub(reMDNcodeCloseConvert, r"```", fileAsString)
        fileAsString = re.sub(reMNDLocalLinkRem, r"\1", fileAsString)
        outfile.write(fileAsString)

def convertMDN_2olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        outfile.write(header)
        fileAsString = infile.read()
        fileAsString = re.sub(reMDNGlossaryRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefDoubleRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNjsxrefRem, r"\1", fileAsString)
        fileAsString = re.sub(reMDNcodeOpenConvert, r"```javascript\n", fileAsString)
        fileAsString = re.sub(reMDNcodeCloseConvert, r"```", fileAsString)
        fileAsString = re.sub(reMNDLocalLinkRem, r"\1", fileAsString)
        outfile.write(fileAsString)

def convertUnderstandingES6_2olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        outfile.write(header)
        fileAsString = infile.read()
        # fileAsString = fileAsString.split('---',2)[2]
        #     # remove header between two instances of '---'
        fileAsString = re.sub(reH2Find, "\n\n<!-- @section -->\n" + r"\1", fileAsString)
        fileAsString = re.sub(reMarkdownLocalLinkRem, r"\1", fileAsString)
        fileAsString = re.sub(reLeanpubCodeRemove, r"\1", fileAsString)
        print "need to debug removing A>, W> etc from code"
        # fileAsString = re.sub(reDoublebracketHTTPLink2MdLink, r"[\1](http\2)", fileAsString)
        # fileAsString = re.sub(reDoublebracketSingleLinkRem, r"\1", fileAsString)
        # fileAsString = re.sub(reDoublebracketLinkRem, r"\1", fileAsString)
        # fileAsString = re.sub(reDoublebraceTagRem, "", fileAsString)
        outfile.write(fileAsString)


"""
------------------------------
Start main code body
------------------------------
"""

for i in range(len(files)):
    convertJSDoc2olm(files[i]['infile'], files[i]['outfile'], files[i]['header'])
