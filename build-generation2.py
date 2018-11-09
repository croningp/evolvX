from seq import *

## Load the wild-type sequence for reference
swt = SequenceList()
swt.addSequenceData("seq-data/WildType.txt")
wt = swt[0][0]

## Load the prior experimental sequences
seqs = SequenceList()
seqs.addSequenceData("seq-data/Experiment/GA.txt")
seqs.addSequenceData("seq-data/Experiment/GB.txt")
seqs.addSequenceData("seq-data/Experiment/G1.txt")

## Convert the sequences to a list of mutations
ml = seqs.buildMutationList(wt)
mat = "\n".join(seqs.buildMatrix(ml))

## This will contain the output sequences
sls = SequenceList()

## Load the fitness data for each mutation as derived
## from the generation 3 model
ml.loadFitnessData("effect-data/G1.txt")

## Apply the mutation chain to reach generation 2
## centroid sequence (best sequence from gen 2)
g1wt = swt.applyMutation("12.F")
g2wt = g1wt.applyMutation("5.K")

## Sample 90 sequences based on the effect data
## [7,3] shows the probabilities of each number of mutations
## 70% chance of 1 mutation
## 30% chance of 2 mutations
rl = ml.generateRandoms(90,[7,3], g2wt[0][0],allList=seqs, tuning=5)

## Add 3 x wildtype sequences and 3 x gen2 centroid
## Then the 90 random sequences for a 96 well experiment
sls.add(swt)
sls.add(swt)
sls.add(swt)
sls.add(g2wt)
sls.add(g2wt)
sls.add(g2wt)
sls.add(rl)

## Write out the generation 2 sequences to file
sls.writeOut("Generation2-test.txt")

## Generate the mutation matrix for all mutations to date
with open("Generation2-test-matrix.csv","w") as oHandle:
    oHandle.write(",".join(["\"%s\""%i for i in ml])+"\n")
    oHandle.write(mat)
