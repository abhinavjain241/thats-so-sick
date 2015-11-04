from sklearn.metrics.pairwise import cosine_similarity
# from scipy import spatial

hash = {}

with open("../Data/glove.6B.300d.txt") as infile:
	for line in infile:
		word, dim_string = line.split(' ', 1)
		dimension = dim_string.split('\n')[0].split(' ')
		hash[word] = dimension

# m = 0 # number of lines in old
# n = 0 # number of lines in new

matrix = []

with open("../Data/the_20022005_clusters_N200.txt") as new_data:
	with open("../Data/the_19091953_clusters_N200.txt") as old_data:
		for line_in_new in new_data:
			sl_n = line_in_new.split("\t")
			sl1_n = sl_n[2].split(", ")
			wlist_n = []
			for item in sl1_n:
				wlist_n.append(item.split("/")[0])		
			# We've got wordlist for new data
			row = []
			for line_in_old in old_data:
				sl_o = line_in_old.split("\t")
				sl1_o = sl_o[2].split(", ")
				wlist_o = []
				for item in sl_o:
					wlist_o.append(item.split("/")[0])

				# Compute Cosine similarity of each sense cluster
				result = 0 
				count = 0
				for word_new in wlist_n:
					for word_old in wlist_o:
						if ((word_new in hash) and (word_old in hash)):
							count = count + 1
							result += cosine_similarity(hash[word_new], hash[word_old])
				result = result / count
				# End of computation for one sense cluster
				row.append(result)

			matrix.append(row)

print matrix