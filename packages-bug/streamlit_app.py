import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import MACCSkeys, Draw

# try:
#     from rdkit import Chem
#     from rdkit.Chem import Draw
#     from rdkit.Chem import MACCSkeys, Draw
#     st.write('Success!')
# except:
#     st.write('Failed to install dependencies from packages.txt :(')
