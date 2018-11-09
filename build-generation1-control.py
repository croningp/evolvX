from seq import *


swt = SequenceList()
swt.addSequenceData("seq-data/WildType.txt")
wt = swt[0][0]
seqs = SequenceList()
seqs.addSequenceData("seq-data/Experiment/GA.txt")
seqs.addSequenceData("seq-data/Experiment/GB.txt")
ml = seqs.buildMutationList(wt)
mat = "\n".join(seqs.buildMatrix(ml))

seenSingles = seqs.buildSeenSingles(ml)

mls = ml.filterOut(seenSingles)
sls = SequenceList()

ml.loadFitnessData("effect-data/GB.txt")
g1wt = swt.applyMutation("12.F")
g2wt = g3wt.applyMutation("5.K")
g3wt = g4wt.applyMutation("9.R")
g3wt = g5wt.applyMutation("1.L")
gvladi = g5wt.applyMutation("10.K")
rl = ml.generateRandoms(87,[5,4,1], g1wt[0][0], allList = seqs, tuning=1)

sls.add(swt)
sls.add(swt)
sls.add(swt)
sls.add(g1wt)
sls.add(g1wt)
sls.add(g1wt)
sls.add(gvladi)
sls.add(gvladi)
sls.add(gvladi)
sls.add(rl)

sls.writeOut("Generation1-control.txt")


