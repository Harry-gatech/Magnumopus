import numpy as np


#create Matrices

def matrix(seq1,seq2):

	main_matrix = np.zeros((len(seq1)+1,len(seq2)+1))
	match_checker_matrix=np.zeros((len(seq1),len(seq2)))
