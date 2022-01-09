import pandas as pd

# read blast results
df_A_vs_B = pd.read_csv('blast_query_clostridium_db_neisseria', sep='\t', header=None)
df_B_vs_A = pd.read_csv('blast_query_neisseria_db_clostridium', sep='\t', header=None)

# add header
colnames = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
df_A_vs_B.columns = colnames
df_B_vs_A.columns = colnames

# get number of protein coding genes in each genome
proteins_species_A = sorted(df_A_vs_B['qseqid'].unique())
proteins_species_B = sorted(df_B_vs_A['qseqid'].unique())

print("Number of protein coding genes")
print("Clostridium spiroforme: " + str(len(proteins_species_A)))
print("Neisseria mucosa: "+str(len(proteins_species_B)) + '\n')

# add new column with hits (potential orthologs)
df_A_vs_B['orthologs'] = "" + df_A_vs_B['qseqid'] + ", " + df_A_vs_B['sseqid']
df_B_vs_A['orthologs'] = "" + df_B_vs_A['sseqid'] + ", " + df_B_vs_A['qseqid']

# get number of shared hits in both BLAST results
shared_hits = list(set(df_A_vs_B['orthologs']).intersection(set(df_B_vs_A['orthologs'])))
print("Number of shared hits: " + str(len(shared_hits)))

# get number of BBH
bbh_orthologs = []
for pair in shared_hits:
    A_protein = pair.split(", ")[0]
    top_hit_orthologs_A = df_A_vs_B[df_A_vs_B["qseqid"] == A_protein].iloc[0]["orthologs"]
    top_hit_orthologs_B = df_B_vs_A[df_B_vs_A["sseqid"] == A_protein].iloc[0]["orthologs"]
    if(top_hit_orthologs_A == top_hit_orthologs_B):
        bbh_orthologs.append(top_hit_orthologs_A)

print("Number of orthologs found by BBH: " + str(len(bbh_orthologs)))