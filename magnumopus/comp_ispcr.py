from .Subprocess_q1 import blast1
from .Subprocess_q1 import filter_blast
from .primer import valid_ht
from .sequence import sequence


def step_one(primer_file, assembly_file):
	
	blast_output = blast1(primer_file, assembly_file)

	filtered = filter_blast(blast_output,80)

	return filtered


def step_two(sorted_hits, max_amplicon_size):

	pair = valid_ht(sorted_hits, max_amplicon_size)

	print("post valid_ht", pair)
	return pair


def step_three(hit_pairs, assembly_file):
	seqs = sequence(hit_pairs, assembly_file)
	print("Post sequence", seqs)
	return seqs