#!/bin/bash

line="---------------------------------"
echo "Starting at: $(date)" ; echo $line
echo

echo "UPTIME"
uptime ; echo $line
echo

echo "FREE"
free ; echo $line
echo

echo "WHO" ; echo 
who ; echo $line
echo

echo "Finishing at : $(date)" ; echo $line