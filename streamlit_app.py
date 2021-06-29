import streamlit as st

try:
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import MACCSkeys, Draw
    st.write('Success')
except:
    st.write('Failed')

