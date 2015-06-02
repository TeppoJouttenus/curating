# this script converts general files to OLM

# -*- coding: utf-8 -*-
import re
import files

files = files.ng_files

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

reDoublebracketSingleLinkRem = re.compile(r'\[\[([^\]\|]+)\]\]')
# remove:  [[description]] -> description
reDoublebracketLinkRem = re.compile(r'\[\[([^\|]+)\|[^\]]+\]\]')
# remove: [[description|link]] -> description
reOtherLinkRem = re.compile(r'\[(.+)\]\[[^\]]*\]')
# remove: [description][link] -> description
reDoublebracketHTTPLink2MdLink = re.compile(r'\[\[([^\|]+)\|http([^\]]+)\]\]')
# convert: [[description|http...]] -> [description](http...)

# JSDoc / ngdoc

reJSDocLinkRem = re.compile(r'{@link \S+ (.+)}')
# remove: {@link link description} -> description
reJSDocExampleTagRem = re.compile(r'</?example[^>]*>')
# remove: <example ... > and </example>
reJSDocCodeOpenConvert = re.compile(r'<file name="([^"]*)">')
# convert: <file name="index.html"> ->
# Sample file name: index.html\n```js
reJSDocCodeCloseConvert = re.compile(r'</file>')
# convert: </file> -> ```

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

def convertJSDoc2olm(oldfile, newfile, header):
    '''\
    Filter away unwanted syntax
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:

        outfile.write(header)
        fileAsString = infile.read()
        fileAsString = fileAsString.split('\n',4)[4]
            # remove first 4 lines which have header info
        fileAsString = re.sub(reJSDocLinkRem, r'\1', fileAsString)
        # fileAsString = re.sub(reJSDocExampleTagRem, r'', fileAsString)
        # fileAsString = re.sub(reJSDocCodeOpenConvert,
        #     r'_Example file_: \1\n```js', fileAsString)
        # fileAsString = re.sub(reJSDocCodeCloseConvert, r'```', fileAsString)
        fileAsString = cleanUpExampleCode(fileAsString)
        outfile.write(fileAsString)

def cleanUpExampleCode(input):
    '''\
    Turn angular example code blocks into Markdown
    '''

    counter = 0
    modifiedInput = input
    while True:
        # Find a location with example code
        start = modifiedInput.find('<example')
        end = modifiedInput.find('</example') + 10
        # indent code between <example> tags
        indentedCode = "FIX THIS"

        modifiedInput = modifiedInput[:start] + indentedCode + modifiedInput[end:]
        counter += 1
        # modifiedInput = re.sub(reJSDocExampleTagRem, r'', modifiedInput)
        # if modifiedInput.find('<example') == -1 or counter > 7:
        #     break
        if counter > 2:
            break
        # else:
        #     counter += 1
        #     print counter

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
        fileAsString = re.sub(reMDNcodeOpenRep, r"```javascript\n", fileAsString)
        fileAsString = re.sub(reMDNcodeCloseRep, r"```", fileAsString)
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
        fileAsString = re.sub(reMDNcodeOpenRep, r"```javascript\n", fileAsString)
        fileAsString = re.sub(reMDNcodeCloseRep, r"```", fileAsString)
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



for i in range(len(files)):
    convertJSDoc2olm(files[i]['infile'], files[i]['outfile'], files[i]['header'])
