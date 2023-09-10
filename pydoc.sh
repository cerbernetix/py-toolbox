#!/bin/sh
lazydocs --ignored-modules toolbox.files.test --overview-file=README.md --validate .
rm docs/.pages
