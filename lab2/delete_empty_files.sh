#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

dir=$1

if [ ! -d "$dir" ]; then
    echo "Error: '$dir' is not a directory"
    exit 1
fi

deleted=$(find "$dir" -maxdepth 1 -type f -empty -print -delete)

if [ -z "$deleted" ]; then
    echo "No empty files found in $dir"
else
    echo "Deleted files:"
    echo "$deleted"
fi
