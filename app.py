import streamlit as st
import pandas as pd
import numpy as np
    #Si esta conectado al arduino y recibio los datos correctamente
def checkvalid():
    return True



def runData():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)
st.title(" ***Inicia tu experimento***")

if st.button('Iniciar') and checkvalid:
    runData()
    
        
       
        
