
# lookit

This project automatically adds static search to a `pkgdown` site. It's not a hack...it's 5 hacks. But it might possibly be useful.

## Step 1. Generate a pkgdown site and put it in the `_site` folder here

```
cp -R docs/* _site/
```

## Step 2. Go get tipuesearch if you don't have it already

```
TIPUESEARCH_ZIP=http://www.tipue.com/search/tipuesearch.zip
wget ${TIPUESEARCH_ZIP} -O search.tar.gz && \
    tar -zxf search.tar.gz && \
    rm -rf search.tar.gz && \
    rm -rf __MACOSX/ && \
    mv Tipue\ Search\ 6.1/ search_js && \
    mv search_js/tipuesearch/ . && \
    rm -rf search_js
```

## Step 3. Go do that hockey

```
bash add_search.sh
```

# References

1. http://www.tipue.com/search/docs/?d=1