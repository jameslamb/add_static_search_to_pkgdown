
from bs4 import BeautifulSoup
import sys

with open("_site/index.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')

# We are going to build up this page by hand....god help us all
page_content = "<!DOCTYPE html>\n"
page_content += "<html>\n\n"

# Grab head of the index page
head_txt = str(soup.head)

# Add the tipuesearch content to the header
search_header = """
    <!-- Search result thing -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400">
    <link rel="stylesheet" href="tipuesearch/css/normalize.css">

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>

    <script type="text/javascript" src="tipuesearch/tipuesearch_set.js"></script>
    <script type="text/javascript" src="tipuesearch/tipuesearch_content.js"></script>
    <link rel="stylesheet" type="text/css" href="tipuesearch/css/tipuesearch.css">
    <script type="text/javascript" src="tipuesearch/tipuesearch.js"></script>
    <!-- end search result thing -->
    """

head_txt = head_txt.replace("</head>", "\n" + search_header + "\n</head>")
page_content += head_txt
page_content += "\n"

# Add the body
page_content += "<body>\n"

# Add all the navbar stuff to the body
navbar = str(soup.header)

page_content += navbar
page_content += "\n"

# Add some additional body content
tipuesearch_body = """
<div class="block" style="padding-top: 31px;">
<div id="tipue_search_content"></div>

</div>

<script>
$(document).ready(function() {
     $('#tipue_search_input').tipuesearch({
          'show': 6
     });
});
</script>
"""

page_content += tipuesearch_body
page_content += "\n"

# close it out
page_content += "</body>\n"
page_content += "</html>\n"

sys.stdout.write(page_content)
