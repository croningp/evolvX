


class SeqDatabase:
	def __init__(self, wt):
		self.seqs = SequenceList()
		self.wt = wt


	def buildMatrix(self, mutList):
		matrix = []
		allSeqs = [i for j in self.seqs for i in j]
		wt = self.wt
		for seq in allSeqs:
			buildSeq = ["0"]*len(mutList)
			for pos in range(len(wt)):
				build = "%d:%s"%(pos,seq[pos])
				if build in mutList:
					buildSeq[mutList.getIndex(build)] = "1"
			matrix.append(",".join(buildSeq))
		return matrix

from random import random


def roulette(weights):
	count = 0
	gr = random()
	for i in weights:
		if i < gr:
			count+=1
		else:
			break
	return count


		
	
	

class MutationList(list):
	def __init__(self):
		self.back = {}
		self.mutFit = {}
	def append(self, thing):
		self.back[thing] = len(self)
		super(SequenceList).append(thing)
	def myappend(self, thing):
		self.back[thing] = len(self)
		super(SequenceList).append(thing)
	def __contains__(self, thing):
		return thing in self.back
	def getIndex(self, idxer):
		return self.back[idxer]
	def filterOut(self, filterList):
		neonate = MutationList()
		filterSet = set(filterList)
		for i in self:
			if not i in filterSet:
				neonate.append(i)
		return neonate
	def loadFitnessData(self, fileName):
		iLines = open(fileName, "r").readlines()
		for line in iLines:
			me = line.split()
			mut,effect = me[0],float(me[1])
			self.mutFit[mut] = effect
		print("%d fitnesses loaded"%len(iLines))

	def generateRandomSeq(self, wt, countWeights, mutWeights):
		wtl = list(wt)
		scw = sum(countWeights)
		smw = sum(mutWeights)
	
		cw = [0]
		rs = 0
		for i in [i/scw for i in countWeights]:
			cw.append(rs+i)
			rs += i
		mw = []
		rs = 0
		for i in  [i/smw for i in mutWeights]:
			mw.append(rs+i)
			rs += i
		
		mutationCount = roulette(cw)
		for i in range(mutationCount):
			mut = self[roulette(mw)]
			pos,al = mut.split(".")
			pos = int(pos)
			wtl[pos] = al
		return "".join(wtl)

	def generateRandoms(self, number, countWeights, wt, allList = [[]], tuning=10):
		newAll = set()
		for i in allList:
			newAll = newAll.union(set(i))
		allList = newAll
		wtl = list(wt)
		mutWeights = []
		for mut in self:
			if mut in self.mutFit:
				if self.mutFit[mut] < 0 and tuning != 1:
					mutWeights.append(0)
				else:
					mutWeights.append(tuning**self.mutFit[mut])
			else:
				mutWeights.append(1)
		res = set()
		print(mutWeights)
		count = 0
		while len(res) < number:
			count += 1
			single = self.generateRandomSeq(wt, countWeights, mutWeights)
			if not single in allList:
				res.add(single)
		print("%d unqiue sequences picked from %d random sequences generated"%(len(res),count))
		m = SequenceList()
		m.append(list(res))
		return m

class SequenceList(list):
	def addSequenceData(self, iFileName):
		rawData = [i.split()[0].strip() for i in self.loadSequences(iFileName)]
		self.append(rawData)

	def add(self, sList):
		self.__iadd__(sList)

	def applyMutation(self, mut):
		neonate = SequenceList()
		for j in self:
			build = []
			for wtl in [list(i) for i in j]:
				pos,al = mut.split(".")
				pos = int(pos)
				wtl[pos] = al
				build.append("".join(wtl))
			neonate.append(build)
		return neonate

	def addSingles(self, mutList, wt):
		wtl = list(wt)
		build = []
		for mut in mutList:
			nw = list(wtl)
			pos,al = mut.split(".")
			pos = int(pos)
			nw[pos] = al
			build.append("".join(nw))
		print("%d singles generated"%len(build))
		self.append(build)

	def loadSequences(self, iFileName):
		iHandle = open(iFileName, "r")
		iData = iHandle.readlines()
		iHandle.close()
		iData = [i.strip() for i in iData]
		return iData

	def buildMutationList_Trevor_orig(self, wt):
		IDXToMut = MutationList()
		allSeqs = [i for j in self for i in j]
                print(allSeqs)
                print(len(allSeqs))
		for seq in allSeqs:
			for pos in range(len(wt)):
                                print(pos)
				if seq[pos] != wt[pos]:
                                        print "%d.%s"%(pos,seq[pos])
					build = "%d.%s"%(pos,seq[pos])
                                        print(build)
					if not build in IDXToMut:
						IDXToMut.myappend(build)
		return IDXToMut

	def buildMutationList(self, wt):
		IDXToMut = MutationList()
		allSeqs = [i for j in self for i in j]
                print(allSeqs)
                print(len(allSeqs))
		for seq in allSeqs:
			for pos in range(len(wt)):
                                print(pos)
				if seq[pos] != wt[pos]:
                                        print "%d.%s"%(pos,seq[pos])
					build = "%d.%s"%(pos,seq[pos])
                                        #print(build)
					if not build in IDXToMut:
						#IDXToMut.myappend(build)
                                                print("hoge")
                                                print(build)
		return IDXToMut

	def buildSeenSingles(self, mutList):
		seen = MutationList()
		allSeqs = [i for j in self for i in j]
		for seq in allSeqs:
			count = 0
			last = None
			for pos in range(len(seq)):
				build = "%d.%s"%(pos,seq[pos])
				if build in mutList:
					count += 1
					last = build
			if count == 1:
				seen.append(last)
		return seen

	def buildMatrix(self, mutList):
		matrix = []
		allSeqs = [i for j in self for i in j]
		for seq in allSeqs:
			buildSeq = ["0"]*len(mutList)
			for pos in range(len(seq)):
				build = "%d.%s"%(pos,seq[pos])
				if build in mutList:
					buildSeq[mutList.getIndex(build)] = "1"
			matrix.append(",".join(buildSeq))
		return matrix

	def mutationCount(self, wt):
		ff = []
		for j in self:
			build = []
			for seq in j:
				count =0
				for pos in range(len(wt)):
					if seq[pos] != wt[pos]:
						count += 1
				build.append(count)
			ff.append(build)
				
		return ff
		
	def writeOut(self, outputName):
		oHandle = open(outputName, "w")
		allSeqs = [i for j in self for i in j]
		for seq in allSeqs:
			oHandle.write(seq+"\n")
		oHandle.close()


