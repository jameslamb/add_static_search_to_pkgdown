#!/bin/bash

# failure is a natural part of life
set -e

# Create a search results page
#curl -XGET https://raw.githubusercontent.com/JacquesMarais/TipueSearch/master/search.html > _site/search.html

# Copy tipusearch over into the site
echo "Adding tipuesearch as a static resource"
cp -R tipuesearch _site/
echo "Done"

# Parse roxygen into search entries
echo "Indexing site content"
python index_content.py > _site/tipuesearch/tipuesearch_content.js
echo "Done"

# Add a search results page
echo "Adding search results page"
python create_search_result_page.py > _site/search.html
echo "Done"

# Put content from "searchbar.html" in the <ul class="nav navbar-nav navbar-right"></ul>
# class in "index.html" and pretty much all of the other HTML files
# (the bootstrap navbar shit is copied across them)
for HTML_DIR in _site/ _site/reference; do
    for HTML_FILE in $(ls -R ${HTML_DIR}/*.html); do
        echo "Adding search to navbar: ${HTML_FILE}"
        python add_search_to_navbar.py -f ${HTML_FILE}
        echo "Done"
    done
done

# References
# [1] http://www.tipue.com/search/docs/?d=1
