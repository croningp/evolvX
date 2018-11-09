# Code repository for "Using Evolutionary Algorithms and Machine Learning to Explore Sequence Space for the Discovery of Antimicrobial Peptides" 

by Mari Yoshida, Trevor Hinkley, Soichiro Tsuda, Sabrina Galiñanes Reyes, Maria D. Castro, Leroy Cronin

Published: _Chem_ (Cell Press), February 8, 2018

https://www.cell.com/chem/fulltext/S2451-9294(18)30027-5

DOI: [10.1016/j.chempr.2018.01.005](https://doi.org/10.1016/j.chempr.2018.01.005)

Corresponding author: Prof Lee Cronin (Lee.Cronin@glasgow.ac.uk)

----- 

## Description 

This repository contains a set of small programs that we developed to perform the evolutionary optimisation experiments in the above paper. The programs were written in R/Python/Shell script.  

In a nutshell, the evolutionary optimisation was performed based on a simple genetic algorithm (GA) --- a "wild type" peptide sequence was used to generate a set of various peptide sequences, or "offsprings", _in silico_ by introducing mutations(=amino acid substitutions). No cross-over was applied to generate them. The sequences were chemically sythesised using a peptide synthesiser and their antimicrobial activities evalulated against _E. coli_.  

What makes our research distinctive from previous research is the use of machine learning (ML) prediction for the GA. When introducing mutations, predictive amino acid substitutions that are likely to improve the antimicrobial activity were introduced based on a ML model (generalised linear model).  
When we compared optimisations by the GA coupled with ML prediction with those by the GA with random mutation (i.e. no ML prediction). We observed significant increase in the antimicrobial activity after three rounds of the optimisation. This suggests our ML-coupled GA optimisation is effective to search and optimise any polymer sequences out of a massive number of possible combinations. 



