#!/bin/bash

## n0nuser
## https://github.com/n0nuser/rubberspark

#####################
# CHANGE THESE VALUES

## e.g.: PATH_ENCODER = 
PATH_ENCODER="resources/duckEncoder/duckencoder.py"

## e.g.: PATH_DUCK2SPARK =
PATH_DUCK2SPARK="resources/duck2spark.py"

## e.g.: PATH_ARDUINO = "arduino"
PATH_ARDUINO="arduino"

KEYBOARD_LANG="es"
#####################

file=$(echo $1 | cut -f 1 -d '.')

encoder="python $PATH_ENCODER -l $KEYBOARD_LANG -i $file.duck -o $file.bin"
spark="python $PATH_DUCK2SPARK -i $file.bin -o $file.ino"
arduino="sudo $PATH_ARDUINO $file.ino"

$($encoder)
$($spark)
$($arduino)
