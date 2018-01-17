#!/bin/bash

# set vals
verbose='false'
pflag='false' # <optional> specifies port
sflag='false' # <optional> if given should use ssl encryped socket
hname="${@:(-2):1}" # <required> the hostname
nuid="${@:(-1):1}"  # <required> preston set this to be 1

# handle flags
if [ "$1" == '-p' ]; then pflag="$2"; fi
while getopts 'sp:v' flag; do
  case "${flag}" in
    s) sflag='true' ;;
  esac
done

# actually run shit
python client.py $pflag $sflag $hname $nuid