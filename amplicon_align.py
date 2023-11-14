#!/usr/bin/env python
import argparse
import magnumopus

def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp_seq = ''.join(complement[base] for base in dna_sequence[::-1].replace("\n", ""))
    return reverse_comp_seq


def main():
    parser = argparse.ArgumentParser(description="Perform in-silico PCR on two assemblies and align the amplicons")
   
    parser.add_argument('-1', dest='assembly1', required=True, help="Path to the first assembly file")
    parser.add_argument('-2', dest='assembly2', required=True, help="Path to the second assembly file")
    parser.add_argument('-p', dest='primers', required=True, help="Path to the primer file")
    parser.add_argument('-m', dest='max_amplicon_size', type=int, required=True, help="Maximum amplicon size for isPCR")
    parser.add_argument('--match', type=int, required=True, help="Match score to use in alignment")
    parser.add_argument('--mismatch', type=int, required=True, help="Mismatch penalty to use in alignment")
    parser.add_argument('--gap', type=int, required=True, help="Gap penalty to use in alignment")
   
    args = parser.parse_args()

    # Perform isPCR on both assembly files
    amplicon1 = magnumopus.ispcr(args.primers, args.assembly1, args.max_amplicon_size)
    amplicon2 = magnumopus.ispcr(args.primers, args.assembly2, args.max_amplicon_size)
   
    # strip the header
    amplicon1 = "\n".join(amplicon1.split("\n")[1:])
    amplicon2 = "\n".join(amplicon2.split("\n")[1:])

    # Align the amplicons
    all_comparisions = [[amplicon1, amplicon2], [amplicon1, reverse_complement(amplicon2)]]
    all_scores = []
    for a1, a2 in all_comparisions:
        alignment, score = magnumopus.needleman_wunsch(a1, a2, args.match, args.mismatch, args.gap)
        all_scores.append([alignment, score])
   
    best_alignment, best_score = sorted(
        all_scores, key=lambda x: x[1], reverse=True
    )[0]
   
    # Print the alignment and score to the terminal
    for line in best_alignment:
        print(line)
    print(best_score)

if __name__ == "__main__":
    main()