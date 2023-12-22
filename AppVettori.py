
import streamlit as st
from latexifier import latexify

import numpy as np
from sympy import *
import re



initial_vectors="A(20,30,34) \nB(12,11,10) \nC(45,34,30)"

st.sidebar.text("Inserisci  un punto per riga.\nPunti nella forma: \nA(1,2,3) \nB(4,5,6) \nC(7,8,9)")
vettori=st.sidebar.text_area('',
    # 'Inserisci un punto per riga.\n Punti nella forma A(1,2,3) \n B(4,5,6) \n C(7,8,9)',
    value=initial_vectors,height=100)

def extract_input(user_input):

    points_pattern="[A-Z]\(.+\)"
    points_name_pattern="([A-Z])"
    points_coord_pattern="\(([-]?\d+),([-]?\d+),([-]?\d+)\)"
    points_string=re.findall(pattern=points_pattern,string=user_input, flags=re.MULTILINE)


    points_dict={}
    for str_point in points_string:
        print(str_point)
        point_name=re.findall(pattern=points_name_pattern,string=str_point)
        point_coord=re.findall(pattern=points_coord_pattern,string=str_point)
        coord_array=np.array([int(point_coord[0][0]),int(point_coord[0][1]),int(point_coord[0][2])])
        points_dict[point_name[0]]=coord_array
    return points_dict



try:
    points=extract_input(vettori)
except:
    st.sidebar.error("Errore nell'input")
    points=extract_input(initial_vectors)
else:
    #st.sidebar.success("Input corretto, punti aggiornati")
     pass   
points['O']=np.array([0,0,0])




def get_vector_components(start_name,end_name):
    start=points[start_name]
    end=points[end_name]
    result=end -start
    return result

def show_vector(start_name,end_name, points=points, show_latex=False):
    start=points[start_name]
    end=points[end_name]
    result=end -start
  
    ret_string='\\overrightarrow{{{}{}}}={}'.format(start_name,end_name,latexify(result),show_latex=False)
    #ret_string='\\overrightarrow{'+ start_name + end_name +"}="+ latexify(result)

    #
    if show_latex:
        print(ret_string)
    return ret_string
    
    
def show_vector_norm(start_name,end_name, points=points,show_latex=False):
    start=points[start_name]
    end=points[end_name]
    result=end -start
    norm=np.round(np.linalg.norm(result),2)
    exact_square_sum=np.sum(result**2)
    ret_string='||\\overrightarrow{{{}{}}}||= \sqrt{{{}}} \\approx {}'.format(start_name,end_name,latexify(exact_square_sum),norm)
    # display(Math(ret_string))
    if show_latex:
        print(ret_string)
    return ret_string
        
def show_dot_product(start_name1,end_name1, start_name2,end_name2, points=points,show_latex=False):
    vector1=points[end_name1]-points[start_name1]
    vector2=points[end_name2]-points[start_name2]
    dot_product=np.dot(vector1,vector2)
    ret_string=('\\overrightarrow{{{}{}}} \\cdot \\overrightarrow{{{}{}}}={} \\cdot {} = {}'
                .format(start_name1,end_name1,start_name2,end_name2,latexify(vector1),latexify(vector2),latexify(dot_product)))
    
    if show_latex:
        print(ret_string)
    return ret_string

def show_angle(start_name1,end_name1, start_name2,end_name2, points=points,show_latex=False):
    vector1=points[end_name1]-points[start_name1]
    vector2=points[end_name2]-points[start_name2]
    vector1_norm=np.linalg.norm(vector1)
    vector2_norm=np.linalg.norm(vector2)
    dot_product=np.dot(vector1,vector2)
    if vector1_norm!=0 and vector2_norm!=0:
        angle=np.rad2deg(np.arccos(dot_product/(vector1_norm * vector2_norm)))
    else:
        angle='NAN'
    ret_string='\\alpha={:.4f} °'.format(angle)
    # display(Math(ret_string)   )
    if show_latex:
        print(ret_string)
    return ret_string
               
def show_cross_product(start_name1,end_name1, start_name2,end_name2, points=points,show_latex=False):
    vector1=points[end_name1]-points[start_name1]
    vector2=points[end_name2]-points[start_name2]
    cross_product=np.cross(vector1,vector2)
    ret_string=('\\overrightarrow{{{}{}}} \\times \\overrightarrow{{{}{}}}={} \\times {} = {}'
                .format(start_name1,end_name1,start_name2,end_name2,latexify(vector1),latexify(vector2),latexify(cross_product)))
    # display(Math(ret_string))
    if show_latex:
        print(ret_string)
    return ret_string

def show_cross_product_norm(start_name1,end_name1, start_name2,end_name2, points=points,show_latex=False):
    vector1=points[end_name1]-points[start_name1]
    vector2=points[end_name2]-points[start_name2]
    cross_product=np.cross(vector1,vector2)
    exact_norm=np.sum(np.square(cross_product))
    norm=np.round(np.linalg.norm(cross_product),2)
    ret_string=('||\\overrightarrow{{{}{}}} \\times \\overrightarrow{{{}{}}}||=\\left|\\left|{} \\times {} \\right|\\right| = \\sqrt{{ {} }} \\approx{}'
                .format(start_name1,end_name1,start_name2,end_name2,latexify(vector1),latexify(vector2),str(exact_norm),str(norm)))
    # display(Math(ret_string))
    if show_latex:
        print(ret_string)
    return ret_string

if 'choices_end1' not in st.session_state:
    st.session_state.choices_end1=list(points.keys())
if 'choices_end2' not in st.session_state:
    st.session_state.choices_end2=list(points.keys())
    # st.write(type(st.session_state.end1))
    # st.write(list(points.keys()))
    
def update_choices(vector_name):

    choices = list(points.keys())
    choices.remove(st.session_state[vector_name])
    if vector_name=='start1':
        st.session_state.choices_end1=choices
    if vector_name=='start2':
        st.session_state.choices_end2=choices

    # st.session_state

#     return None
    
side_left, side_right =st.sidebar.columns(2)

with side_left:
    st.write("Vettore 1")
    start1=st.selectbox("Start",list(points.keys()),key='start1', on_change=update_choices, args=('start1',))
    update_choices('start1')
 
    p_end1=st.empty()
    with p_end1:
       end1=st.selectbox("End",list(st.session_state.choices_end1),key='end1')    
with side_right:
    st.write("Vettore 2")

    start2=st.selectbox("Start",list(reversed(points.keys())),key='start2',on_change=update_choices, args=('start2',))
    update_choices('start2')
    p_end2=st.empty()
    with p_end2:
        end2=st.selectbox("End",list(st.session_state.choices_end2),key='end2')

            
   
pos_vec=st.expander("Vettori posizione",expanded=False) 
with pos_vec:
    num_col=len(points.keys())-1 #Do not count O
    necessary_rows=num_col//4+1
    columns=[st.columns(4) for i in range(necessary_rows)]
    for i,key in enumerate(list(points.keys())):
        current_row=i//4         
        if key !='O':
            with columns[current_row][i%4]:
                st.latex(show_vector('O',key,show_latex=False))  
   
      
      


          
left,right=st.columns(2)

with left:
    vec1_expander=st.expander("Vettore 1",expanded=True)
    with vec1_expander:
     

        st.latex(show_vector(start1,end1,show_latex=False))
        st.latex(show_vector_norm(start1,end1,show_latex=False))

    
with right:
    
    vec2_expander=st.expander("Vettore 2",expanded=True)
    with vec2_expander:
        
        st.latex(show_vector(start2,end2,show_latex=False))
        st.latex(show_vector_norm(start2,end2,show_latex=False))


dot_expander=st.expander("Prodotto scalare e angolo",expanded=True)
with dot_expander:
    st.latex(show_dot_product(start1,end1,start2,end2,show_latex=False))
    st.latex(show_angle(start1,end1,start2,end2,show_latex=False))


cross_expander=st.expander("Prodotto vettoriale e norma",expanded=True)
with cross_expander:
    st.latex(show_cross_product(start1,end1,start2,end2,show_latex=False))
    st.latex(show_cross_product_norm(start1,end1,start2,end2,show_latex=False))





