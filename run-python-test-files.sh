#!/bin/bash

# Run Python test files. Assume they are executable.
for file in $@; do
    echo $file
    $file
done
