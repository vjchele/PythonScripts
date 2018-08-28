'''
This utility reads the core*.log (SOLR logs) files from a directory
scans for all JobPostings Collection logs and finds where
'''
import os
import re
termsDict = {} # Dictionary object to hold terms

for r,d,f in os.walk('//licmp072n8p0043/d$/Solr Logs'): # Reading Log location
    for file in f:
        loc = os.path.join(r,file)
        if ("core" in loc): # Excluding non "core" files
            with open(loc,encoding='utf8') as corefile:
                lines = corefile.readlines()
                for line in lines:
                    if line.find("core.SolrCore - [JobPostings]") > 0 and line.find("start=0") > 0:
                        m = re.search('(?<=&q=)[0-9a-zA-Z_+]+',line)
                        if m and m.group(0):
                            searchterm = m.group(0).replace('+',' ').lower() # replace '+' with ' ' and converting to lower
                            termsDict[searchterm] = termsDict.get(searchterm,0) + 1

with open('output.txt','w',encoding='utf-8') as output:
    for key in sorted(terms.items(), key=lambda x: x[1], reverse=True)[:100]: # Selecting top 100 terms
        output.write(key[0] +',' + str(key[1]) + '\n') # output the results





