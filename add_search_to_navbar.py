
import argparse
import sys

fname = "reference/DegreeToMeters.html"

parser = argparse.ArgumentParser(description='Add tipuesearch stuff to Bootstrap navbar')
parser.add_argument('-f',
                    type=str,
                    help='Path to the HTML file to change')
args = parser.parse_args()

# Add in search content
search_navbar_content = """
    <!-- Search stuff -->
    <li>
      <a>search:</a>
    </li>
    <li>
      <form action="search.html">
        <div class="tipue_search_right" style="padding-top:10px;">
          <input type="text" name="q" id="tipue_search_input" pattern=".{3,}" title="At least 3 characters" required>
        </div>
        <div style="clear: both;"></div>
      </form>
      <div id="tipue_search_content"></div>
    </li>
    <!-- -->
    """

with open(args.f, "r") as f:
    html_content = f.read()
    new_content = html_content.replace(
        '<ul class="nav navbar-nav navbar-right">',
        '<ul class="nav navbar-nav navbar-right">\n' + search_navbar_content
    )

with open(args.f, "w") as f:
    f.write(new_content)
