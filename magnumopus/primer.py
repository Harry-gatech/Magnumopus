def valid_ht(good_hits, max_amp_size):
	pairs = []
	for i in range(len(good_hits)-1):
		a_hit = good_hits[i]
		a_start, a_stop = [int(i) for i in a_hit[8:10]]
		a_dir = "fwd" if a_start < a_stop else "rev"
		for j in range(i+1, len(good_hits)):
			b_hit = good_hits[j]
			if a_hit[1] != b_hit[1]: # different contig
				continue

			b_start, b_stop = [int(i) for i in b_hit[8:10]]
			b_dir = "fwd" if b_start < b_stop else "rev"

			if a_dir == b_dir: # same direction
				continue

			if a_start < b_start: # a before b
				if not a_dir == "fwd": # wrong direction
					continue
				if not a_stop > b_start - max_amp_size: # too far
					break ############### continue

				pairs.append((a_hit, b_hit))
				continue

			if not b_dir == "fwd": # wrong direction
				continue
			if not b_stop > a_start - max_amp_size: # too far
				continue

			pairs.append((a_hit, b_hit))
	
	return pairs

def points(seq1,seq2):

	if int(seq2[8]) > int(seq2[9]) and int(seq1[9]) > int(seq1[8]) and ((seq1[0]) != (seq2[0])):
		return True

	return False


def cal_dist(seq1, seq2):

	start1=int(seq1[8])
	end1=int(seq1[9])
	start2=int(seq2[8])
	end2=int(seq2[9])

	dist=abs(start2 - end1)
	#print(dist)
	return dist