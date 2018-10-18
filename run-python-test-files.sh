#!/bin/bash

# Run Python test files.
for file in $@; do
    echo $file
    python $file
done
