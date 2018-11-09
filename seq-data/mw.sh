#!/usr/bin/bash
curl --data "txtRawPeptide=$1&btnCalculate=Calculate" -XPOST http://www.biopeptide.com/PepCalc/Calculate 2>/dev/null | grep "M\\.W\\.:" | sed "s/.*mono\">//" | sed "s/<.*//"
