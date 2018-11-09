from seq import *

swt = SequenceList()
swt.addSequenceData("seq-data/Centroid-G2.txt")
wt = swt[0][0]

seqs = SequenceList()
seqs.addSequenceData("seq-data/Experiment/GA.txt")
seqs.addSequenceData("seq-data/Experiment/GB.txt")
seqs.addSequenceData("seq-data/Experiment/G1.txt")
seqs.addSequenceData("seq-data/Experiment/G2.txt")
ml = seqs.buildMutationList(wt)
mat = "\n".join(seqs.buildMatrix(ml))


oHandle = open("seqMatrix-G2.csv","w")
oHandle.write(",".join(["\"%s\""%i for i in ml])+"\n")
oHandle.write(mat)
oHandle.close()
