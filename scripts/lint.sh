#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJ_DIR="$THIS_DIR/.."
RC_FILE="$PROJ_DIR/conf/pylintrc"

PYTHONPATH=$PYTHONPATH:. pylint --rcfile=$RC_FILE $PROJ_DIR
