#!/usr/bin/bash
while read i; do ./mw.sh $i >> Generation$1.weights; done < Generation$1.txt
