import subprocess



def sequence(hit_pairs, assembly_file):
    bed_path = "tormaaergud.bed"
    bed_file = open(bed_path, "w")
    for hit_pair in hit_pairs:


        start=int(hit_pair[0][9])
        end=int(hit_pair[1][9])

        if start < end: 
            bed_file.write(f"{hit_pair[0][1]} {start} {end}\n")
    bed_file.close()
    seqtk_command=f"seqtk subseq {assembly_file} {bed_path}"
    seqtk_output=subprocess.check_output(seqtk_command,shell=True, universal_newlines=True)

    return seqtk_output

