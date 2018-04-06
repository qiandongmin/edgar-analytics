#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/sessionization.py ./input/log.csv ./input/inactivity_period.txt ./output/sessionization.txt

GRADER_ROOT=$(dirname ${BASH_SOURCE})

PROJECT_PATH=${GRADER_ROOT}

python ${GRADER_ROOT}/src/sessionization.py
