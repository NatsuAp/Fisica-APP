# import streamlit as st
# from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
# import time
# from threading import Thread


# class WorkerThread(Thread):
#     def __init__(self, delay, target):
#         super().__init__()
#         self.delay = delay
#         self.target = target

#     def run(self):
#         # runs in custom thread, but can call Streamlit APIs
#         start_time = time.time()
#         time.sleep(self.delay)
#         end_time = time.time()
#         self.target.write(f"start: {start_time}, end: {end_time}")


# delays = [5, 4, 3, 2, 1]
# result_containers = []
# for i, delay in enumerate(delays):
#     st.header(f"Thread {i}")
#     result_containers.append(st.container())

# threads = [
#     WorkerThread(delay, container)
#     for delay, container in zip(delays, result_containers)
# ]
# for thread in threads:
#     add_script_run_ctx(thread, get_script_run_ctx())
#     thread.start()

# # for thread in threads:
# #     thread.join()

# st.button("Rerun")

import streamlit as st
import pandas as pd
import numpy as np
import time
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx


#Si esta conectado al arduino y recibio los datos correctamente
def checkvalid():
    return True
def runData():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

def Title():
        title = "Para iniciar el experimento conecta el arduino"

        for x in title.split(" "):
            yield x + " "
            time.sleep(0.02)
       
def func(st):
     i = 0
     while(True):
          time.sleep(3)
        
          st.write(i)
          i+=1
          print(i)
          if i > 7:
            st.write("se acabo")
            st.session_state.task_done = True
            break
#Revisa si el segundo thread corrio
if "task_started" not in st.session_state:
    st.session_state.task_started = False
if "task_done" not in st.session_state:
    st.session_state.task_done = False      
#si no ha iniciado entra
if not st.session_state.task_started:
     
        st.session_state.task_started = True
        thread1 = threading.Thread(target=func, args=(st.container(), ))
        thread1.start()
#Si ya entro una vez, solo entra en el else las proximas veces que corra el codigo        
else:
    if not st.session_state.task_done:
        st.info("Task is running...")
    else:
        st.success("Task completed!")
        st.write("🎉 Here is the new component added after the background task finished!")
        st.button("Reset", on_click=lambda: st.session_state.update({"task_started": False, "task_done": False}))   

#Suprimir problema de context
add_script_run_ctx(thread1, get_script_run_ctx())


st.title("***Para iniciar el experimento conecta el arduino***")
st.image("Resources\loading.gif")

if st.button('Iniciar') and checkvalid:
    runData()
    

     
       
        
