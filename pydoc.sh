#!/bin/sh
rm -rf docs
lazydocs \
    --ignored-modules tests \
    --overview-file=README.md \
    --validate \
    src
rm docs/.pages
