from .pcr import (
	step_one,
	step_two,
	step_three
)

import numpy as np



def ispcr(primer_file, assembly_file, max_amplicon_size):

	hits=step_one(primer_file, assembly_file)
	pair=step_two(hits, max_amplicon_size)
	amplicon=step_three(pair, assembly_file)
	return amplicon

def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
    # Initialize the score matrix and traceback matrix
    len_a, len_b = len(seq_a), len(seq_b)
    score_matrix = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    traceback_matrix = [[None] * (len_b + 1) for _ in range(len_a + 1)]

    # Initialize the first row and column of the score matrix
    for i in range(len_a + 1):
        score_matrix[i][0] = i * gap
    for j in range(len_b + 1):
        score_matrix[0][j] = j * gap

    # Fill in the score and traceback matrices
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            match_score = match if seq_a[i - 1] == seq_b[j - 1] else mismatch
            diagonal_score = score_matrix[i - 1][j - 1] + match_score
            left_score = score_matrix[i][j - 1] + gap
            up_score = score_matrix[i - 1][j] + gap
            max_score = max(diagonal_score, left_score, up_score)
            score_matrix[i][j] = max_score

            # Set the traceback direction
            if max_score == diagonal_score:
                traceback_matrix[i][j] = "diagonal"
            elif max_score == left_score:
                traceback_matrix[i][j] = "left"
            else:
                traceback_matrix[i][j] = "up"

    # Trace back to find the optimal alignment
    i, j = len_a, len_b
    aligned_seq_a, aligned_seq_b = [], []

    while i > 0 or j > 0:
        if traceback_matrix[i][j] == "diagonal":
            aligned_seq_a.append(seq_a[i - 1])
            aligned_seq_b.append(seq_b[j - 1])
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == "left":
            aligned_seq_a.append("-")
            aligned_seq_b.append(seq_b[j - 1])
            j -= 1
        else:
            aligned_seq_a.append(seq_a[i - 1])
            aligned_seq_b.append("-")
            i -= 1

    # Reverse the aligned sequences to get the correct order
    aligned_seq_a = "".join(reversed(aligned_seq_a))
    aligned_seq_b = "".join(reversed(aligned_seq_b))

    return (aligned_seq_a, aligned_seq_b), score_matrix[len_a][len_b]








