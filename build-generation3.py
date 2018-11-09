from seq import *


swt = SequenceList()
swt.addSequenceData("seq-data/WildType.txt")
wt = swt[0][0]
seqs = SequenceList()
seqs.addSequenceData("seq-data/Experiment/GA.txt")
seqs.addSequenceData("seq-data/Experiment/GB.txt")
seqs.addSequenceData("seq-data/Experiment/G1.txt")
seqs.addSequenceData("seq-data/Experiment/G2.txt")
seqs.addSequenceData("seq-data/Generation3-bad.txt")
ml = seqs.buildMutationList(wt)
mat = "\n".join(seqs.buildMatrix(ml))


sls = SequenceList()

ml.loadFitnessData("effect-data/G2.txt")
g1wt = swt.applyMutation("12.F")
g2wt = g3wt.applyMutation("5.K")
g3wt = g4wt.applyMutation("9.R")
g3wt = g5wt.applyMutation("1.L")
rl = ml.generateRandoms(90,[5,4,1], g3wt[0][0],tuning=5)




sls.add(swt)
sls.add(swt)
sls.add(swt)
sls.add(g3wt)
sls.add(g3wt)
sls.add(g3wt)
sls.add(rl)

sls.writeOut("seq-data/Generation3.txt")
