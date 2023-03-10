#!/bin/bash

# Usage: ./replace_phrase.sh <file_path> <new_phrase>

# Check if the correct number of arguments are provided
if [ $# -ne 2 ]; then
  echo "Error: Invalid number of arguments."
  echo "Usage: ./replace_phrase.sh <file_path> <new_phrase>"
  exit 1
fi

FILE=$1
NEW=$2

BEG='To get ultimate' # CHANGE THIS
END='of secret text.' # CHANGE THIS

# Replace old phrase with new phrase in the file
sed "/${BEG}/,/${END}/ c${NEW}" $FILE
