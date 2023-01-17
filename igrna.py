#!/usr/bin/env python
# coding: utf-8

# In[ ]:



TableS3 = 'https://raw.githubusercontent.com/YQLic/data/main/data/Table%20S3.csv'
TableS4 = 'https://raw.githubusercontent.com/YQLic/data/main/data/Table%20S4.csv'
TableS6 = 'https://raw.githubusercontent.com/YQLic/data/main/data/Table%20S6.csv'
TableS7 = 'https://raw.githubusercontent.com/YQLic/data/main/data/Table%20S7.csv'

get_ipython().system('jupyter nbextension enable --py widgetsnbextension')
get_ipython().system('jupyter labextension install @jupyter-widgets/jupyterlab-manager')
import ipywidgets as widgets
from ipywidgets import interact,interactive, interact_manual
from IPython.display import display
import pandas as pd

def f(N20,indicators,libraries):
    display(N20,indicators,libraries)
    if libraries == 'pathogenic' :
      if indicators == 'case1 max':
        data = pd.read_csv(TableS3)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        # print(subdata)
        print('\nResults:')
        print('Case1 max_gRNA/igRNA_ID:', subdata['Csae1 max_gRNA/igRNA_ID'].values[0])
        print('Case1max_igRNA sequence:', subdata['Case1max_igRNA sequence'].values[0])
        print('Case1 max:', subdata['Csae1 max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == 'case3 min':
        data = pd.read_csv(TableS3)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('Case3 min_gRNA/igRNA_ID:', subdata['Case3 min_gRNA/igRNA_ID'].values[0])
        print('Case3 min_igRNA sequence:', subdata['Case3 min_igRNA sequence'].values[0])
        print('Case3 min:', subdata['Case3 min'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(case1-case3) max':
        data = pd.read_csv(TableS3)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1-case3) max_gRNA/igRNA_ID:', subdata['(case1-case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1-case3) max_igRNA sequence:', subdata['(case1-case3) max_igRNA sequence'].values[0])
        print('(case1-case3) max:', subdata['(case1-case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(case1/case3) max':
        data = pd.read_csv(TableS3)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1/case3) max_gRNA/igRNA_ID:', subdata['(case1/case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1/case3) max_igRNA sequence:', subdata['(case1/case3) max_igRNA sequence'].values[0])
        print('(case1/case3) max:', subdata['(case1/case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(igRNAcase1-original gRNAcase1) max':
        data = pd.read_csv(TableS6)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1/case3) max_gRNA/igRNA_ID:', subdata['(case1/case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1/case3) max_igRNA sequence:', subdata['(case1/case3) max_igRNA sequence'].values[0])
        print('(case1/case3) max:', subdata['(case1/case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(igRNAcase1-original gRNAcase1) max':
        data = pd.read_csv(TableS6)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(igRNAcase1-original gRNAcase1) max_ gRNA/igRNA_ID:', subdata['(igRNAcase1-original gRNAcase1) max_ gRNA/igRNA_ID'].values[0])
        print('(igRNAcase1-original gRNAcase1) max_ igRNA sequence:', subdata['(igRNAcase1-original gRNAcase1) max_ igRNA sequence'].values[0])
        print('(igRNAcase1-original gRNAcase1) max:', subdata['(igRNAcase1-original gRNAcase1) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(Original gRNAcase3-igRNAcase3) max':
        data = pd.read_csv(TableS6)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(original gRNAcase3-igRNAcase3) max_ gRNA/igRNA_ID:', subdata['(original gRNAcase3-igRNAcase3) max_ gRNA/igRNA_ID'].values[0])
        print('(original gRNAcase3-igRNAcase3) max_ igRNA sequence:', subdata['(original gRNAcase3-igRNAcase3) max_ igRNA sequence'].values[0])
        print('(original gRNAcase3-igRNAcase3) max:', subdata['(original gRNAcase3-igRNAcase3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '[(igRNAcase1-originalCase1) - (original gRNAcase3-igRNAcase3)] max':
        data = pd.read_csv(TableS6)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max_gRNA/igRNA_ID:', subdata['[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max_gRNA/igRNA_ID'].values[0])
        print('[(igRNAcase1-original case1) - (original gRNAcase3-igRNAcase3)] max_igRNA sequence:', subdata['[(igRNAcase1-original case1) - (original gRNAcase3-igRNAcase3)] max_igRNA sequence'].values[0])
        print('[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max:', subdata['[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

##################################
    if libraries == 'likely pathogenic' :
      if indicators == 'case1 max':
        data = pd.read_csv(TableS4)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('Case1 max_gRNA/igRNA_ID:', subdata['Csae1 max_gRNA/igRNA_ID'].values[0])
        print('Case1max_igRNA sequence:', subdata['Case1max_igRNA sequence'].values[0])
        print('Case1 max:', subdata['Csae1 max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return '\n '

      elif indicators == 'case3 min':
        data = pd.read_csv(TableS4)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('Case3 min_gRNA/igRNA_ID:', subdata['Case3 min_gRNA/igRNA_ID'].values[0])
        print('Case3 min_igRNA sequence:', subdata['Case3 min_igRNA sequence'].values[0])
        print('Case3 min:', subdata['Case3 min'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(case1-case3) max':
        data = pd.read_csv(TableS4)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1-case3) max_gRNA/igRNA_ID:', subdata['(case1-case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1-case3) max_igRNA sequence:', subdata['(case1-case3) max_igRNA sequence'].values[0])
        print('(case1-case3) max:', subdata['(case1-case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(case1/case3) max':
        data = pd.read_csv(TableS4)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1/case3) max_gRNA/igRNA_ID:', subdata['(case1/case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1/case3) max_igRNA sequence:', subdata['(case1/case3) max_igRNA sequence'].values[0])
        print('(case1/case3) max:', subdata['(case1/case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(igRNAcase1-original gRNAcase1) max':
        data = pd.read_csv(TableS7)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(case1/case3) max_gRNA/igRNA_ID:', subdata['(case1/case3) max_gRNA/igRNA_ID'].values[0])
        print('(case1/case3) max_igRNA sequence:', subdata['(case1/case3) max_igRNA sequence'].values[0])
        print('(case1/case3) max:', subdata['(case1/case3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(igRNAcase1-original gRNAcase1) max':
        data = pd.read_csv(TableS7)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(igRNAcase1-original gRNAcase1) max_ gRNA/igRNA_ID:', subdata['(igRNAcase1-original gRNAcase1) max_ gRNA/igRNA_ID'].values[0])
        print('(igRNAcase1-original gRNAcase1) max_ igRNA sequence:', subdata['(igRNAcase1-original gRNAcase1) max_ igRNA sequence'].values[0])
        print('(igRNAcase1-original gRNAcase1) max:', subdata['(igRNAcase1-original gRNAcase1) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '(Original gRNAcase3-igRNAcase3) max':
        data = pd.read_csv(TableS7)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('(original gRNAcase3-igRNAcase3) max_ gRNA/igRNA_ID:', subdata['(original gRNAcase3-igRNAcase3) max_ gRNA/igRNA_ID'].values[0])
        print('(original gRNAcase3-igRNAcase3) max_ igRNA sequence:', subdata['(original gRNAcase3-igRNAcase3) max_ igRNA sequence'].values[0])
        print('(original gRNAcase3-igRNAcase3) max:', subdata['(original gRNAcase3-igRNAcase3) max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

      elif indicators == '[(igRNAcase1-originalCase1) - (original gRNAcase3-igRNAcase3)] max':
        data = pd.read_csv(TableS7)
        subdata = data.loc[data['Target sequence (20 bp)']== N20]
        print('\nResults:')
        print('[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max_gRNA/igRNA_ID:', subdata['[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max_gRNA/igRNA_ID'].values[0])
        print('[(igRNAcase1-original case1) - (original gRNAcase3-igRNAcase3)] max_igRNA sequence:', subdata['[(igRNAcase1-original case1) - (original gRNAcase3-igRNAcase3)] max_igRNA sequence'].values[0])
        print('[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max:', subdata['[(igRNAcase1- original case1) - (original gRNAcase3-igRNAcase3)] max'].values[0])
        print('Definition of SNVs:', subdata['Definition of SNVs'].values[0])
        print('Mutation information:', subdata['Mutation information'].values[0])
        print('ClinVar Accession:', subdata['ClinVar Accession '].values[0])
        print('Target sequence (20 bp):', subdata['Target sequence (20 bp)'].values[0])
        print('Editing position:', subdata['Editing position'].values[0])
        print('Pathogenic nucleotide:', subdata['Pathogenic nucleotide'].values[0])
        print('Corrected nucleotide:', subdata['Corrected nucleotide'].values[0])
        return ' '

a = interact(f,N20='TGGAAAGTAAATGTTCATGT', indicators=['case1 max','case3 min','(case1-case3) max','(case1/case3) max','(igRNAcase1-original gRNAcase1) max','(Original gRNAcase3-igRNAcase3) max','[(igRNAcase1-originalCase1) - (original gRNAcase3-igRNAcase3)] max'],libraries=['pathogenic','likely pathogenic']);

