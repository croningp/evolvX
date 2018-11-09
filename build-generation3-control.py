from seq import *


swt = SequenceList()
swt.addSequenceData("seq-data/WildType.txt")
wt = swt[0][0]
seqs = SequenceList()
seqs.addSequenceData("seq-data/Experiment/GA.txt")
seqs.addSequenceData("seq-data/Experiment/GB.txt")
seqs.addSequenceData("seq-data/Generation1-control.txt")
seqs.addSequenceData("seq-data/Generation2-control.txt")
ml = seqs.buildMutationList(wt)
mat = "\n".join(seqs.buildMatrix(ml))

seenSingles = seqs.buildSeenSingles(ml)

mls = ml.filterOut(seenSingles)
sls = SequenceList()

ml.loadFitnessData("effect-data/GB.txt")
g1wt = swt.applyMutation("12.F")
g2wt = g1wt.applyMutation("9.R")
g3wt = g2wt

rl = ml.generateRandoms(90,[5,4,1], g2wt[0][0], allList = seqs, tuning=1)

sls.add(swt)
sls.add(swt)
sls.add(swt)
sls.add(g3wt)
sls.add(g3wt)
sls.add(g3wt)
sls.add(rl)

sls.writeOut("Generation3-control.txt")


