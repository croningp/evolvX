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
sls.addSingles(mls,wt)

ml.loadFitnessData("effect-data/GB.txt")
nwt = swt.applyMutation("12.F")[0][0]
rl = ml.generateRandoms(68,[5,4,1], nwt)

sls.add(rl)

#sls.writeOut("Generation1.txt")

oHandle = open("seqMatrix-GB.csv","w")
oHandle.write(",".join(["\"%s\""%i for i in ml])+"\n")
oHandle.write(mat)
oHandle.close()
