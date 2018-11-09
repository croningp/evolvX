wt = open("WildType.txt","r").readlines()[0].strip()

import operator

sequences = [i.split()[0].strip() for i in open("GenerationA.txt","r").readlines()]
counts = {}

seenSequences = set()
for i in sequences:
	seenSequences.add(i)


for sequence in sequences:
	sequence = sequence.strip()
	i = 0
	for allele in sequence:
		wts = wt[i]
		if allele != wts:
			build = "%d:%s"%(i,allele)
			if not build in counts:
				counts[build] = 0
			counts[build] += 1
		i+=1

sortedCounts = list(reversed(sorted(counts.items(), key=operator.itemgetter(1))))

for mutation in sortedCounts:
	wtc = list(wt)
	pos,al = mutation[0].split(":")
	pos = int(pos)
	wtc[pos] = al
	build = "".join(wtc)
	#if not build in seenSequences:
	print(build)
