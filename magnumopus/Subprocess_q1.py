#!/usr/bin/env python



import subprocess

#primer_file = "primer.fna"

#assembly_file = "Assembly.fna"

#output_file="blast.txt"


def blast1(primer_file, assembly_file):
    blast_cmd = ['blastn', 
             '-query', primer_file,
             '-subject', assembly_file,
             '-task', 'blastn-short',
             '-outfmt', '6 std qlen'
             ]
    
    results = subprocess.check_output(blast_cmd, 
            universal_newlines=True)
    

    return results.strip().split("\n")

def filter_blast(output, min_per):
    lines=output

    filt=[]
    for line in lines:
        line_parts=line.split("\t")

        if((float(line_parts[2])>=min_per) and (line_parts[3]==line_parts[12])):
            if line_parts not in filt:
                filt.append(line_parts)  
    print(filt)            
    return filt







#def step_one (primer_file: str, assembly_file: str):

    
    
    