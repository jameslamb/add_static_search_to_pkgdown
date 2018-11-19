
from bs4 import BeautifulSoup
import re
import cgi
import os
import sys
import json

# Search for roxygen files
roxygen_files = os.listdir('_site/reference/')

# Set up the initial dictionary
tipuesearch_content = {
    "pages": []
}

for roxy_file in roxygen_files:

    # Read up and parse the docs
    with open("_site/reference/{}".format(roxy_file), 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')

    # Grab just the content div
    div_content = soup.findAll('div', class_="contents")[0]

    content = BeautifulSoup(str(div_content), 'html.parser').findAll('p')[0]

    # Remove well-formed tags, fixing mistakes by legitimate users
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    content = tag_re.sub('', str(content))

    # Clean up anything else by escaping
    content = cgi.escape(content)

    # Strip newlines and extra spaces
    content = content.replace("\n", " ")
    content = content.replace("\t", " ")
    multispace = re.compile(r'\s+')
    content = multispace.sub(' ', str(content))
    content = content.strip()

    # Create the content needed by tipuesearch.js
    object_name = roxy_file.replace(".html", "")

    search_entry = {
        "title": object_name,
        "text": content,
        "tags": object_name,
        "url": "reference/{}".format(roxy_file)
    }

    tipuesearch_content["pages"].append(search_entry)

# Oh god please don't stare at this directly
with open("_site/tipuesearch/tipuesearch_content.js", "w+") as f:
    f.write("\nvar tipuesearch = ")
    f.write(json.dumps(tipuesearch_content, indent = 4))
    f.write(";\n")

# Ref:
# [1] https://stackoverflow.com/a/19730306
# [2] http://www.tipue.com/search/docs/?d=1
