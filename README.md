**********************************************************
			Comparative genomics assignment
				(Lucie Červenková, 2022)
**********************************************************
File content description:
1) bbh.py 
	- script used for generating BBH from BLAST results
2) bbh.txt
	- list of BBH (sequence IDs)
3) bbh.out
	- bbh.py output, contains basic information such as number of BBH etc.
4) blast_query_*_db_*
	- BLAST results (using option -outfmt 6), header values can be seen in bbh.py
5) entropy.py
	- script used to calculate Shannon entropy from MSA results
6) entropy.txt
	- entropy.py output, each line contains Shannon entropy for corresponding column in MSA
7) protein_msa.aln
	- MSA results in CLUSTALW format
8) rrna_msa_input.fa
	-  FASTA file used as an input for CLUSTALW when generating species tree
9) species-tree.png
	- species tree
10) tree_bootsrapped.png
	- phylogenetic tree