from sklearn.metrics.pairwise import cosine_similarity

gloveFilePath = "../Data/glove.6B.300d.txt"
newDataFilePath = "../Data/the_20022005_clusters_N200.txt"
oldDataFilePath = "../Data/the_19091953_clusters_N200.txt"

hash = {}

with open(gloveFilePath) as infile:
	for line in infile:
		word, dim_string = line.split(' ', 1)
		dimension = dim_string.split('\n')[0].split(' ')
		hash[word] = dimension

matrix = []

with open(newDataFilePath) as new_data:
	with open(oldDataFilePath) as old_data:
		for lineInNew in new_data:
			splitNew = lineInNew.split("\t")
			splitNewWords = splitNew[2].split(", ")
			wordListNew = []
			for item in splitNewWords:
				wordListNew.append(item.split("/")[0])		
			# We've got wordlist for new data
			row = []
			for lineInOld in old_data:
				sl_o = lineInOld.split("\t")
				splitOldWords = sl_o[2].split(", ")
				wordListOld = []
				for item in sl_o:
					wordListOld.append(item.split("/")[0])
				# We've got worlist for old data
				# Compute Cosine similarity of each sense cluster
				result = 0 
				count = 0
				for word_new in wordListNew:
					for word_old in wordListOld:
						if ((word_new in hash) and (word_old in hash)):
							count = count + 1
							result += cosine_similarity(hash[word_new], hash[word_old])
				result = result / count
				# End of computation for one sense cluster
				row.append(result)
			matrix.append(row)
print matrix