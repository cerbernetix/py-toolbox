#!/bin/sh
rm -rf docs
lazydocs \
    --ignored-modules toolbox.files.test \
    --ignored-modules toolbox.logging.test \
    --overview-file=README.md \
    --validate .
rm docs/.pages
