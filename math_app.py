# sum of 2 numbers
def sum(a,b):
    c = a+b
    return c
#difference
def difference(a,b):
    c = a-b
    return c
#multiplication
def mul(a,b):
    c = a*b
    return c

import geometry
import streamlit as st
import base64

main_bg = "background.png"
main_bg_ext = "png"
side_bg = "bg-sidebar.jpeg"
side_bg_ext = "jpeg"
#code to copy and recycle for making backgrounds
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar.sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

template = """<div style = "background-color:blue; padding:1px;">
                <h2 style = "color=:white; text-align:center">Maths app </h2>
                <img src="background.png">
                </div>""" #allows multiple lines of html
#css colour codes available online, basic css
st.markdown(template,unsafe_allow_html=True) #tells streamlit to run the home written "unsafe" html above
st.title("Maths app")
 #add image command where you want it to appear") #add image command where you want it to appear
st.sidebar.title("Select your type of maths module:")
dropdown = st.sidebar.selectbox("Select one",["","Arithmetic","Geometry",])
if dropdown == "Arithmetic":
    radio_button1 = st.sidebar.radio("Select your choice of calculation: ",["Sum","Difference","Multiplication"])
    x = st.number_input("Enter your number1")
    y = st.number_input("Enter your number2")
    if radio_button1 == "Sum":
        #result_sum
        result_sum = sum(x,y)
        if st.button("Get result"):
            st.success("The sum of the entered numbers is {}".format(result_sum)) #{} is a placeholder and then after format enter what is to display there
            st.balloons()
    elif radio_button1 == "Difference":
        if st.button("Get result"):
            result_diff = difference(x,y)
            st.success("The difference of the entered numbers is {}".format(result_diff))
    elif radio_button1 =="Multiplication":
        if st.button("Get result"):
            result_mul = mul(x,y)
            st.success("The product of the entered numbers is {}".format(result_mul))
    else:
        st.write("please select a calculation")
elif dropdown == "Geometry":
    radio_button2 = st.sidebar.radio("Select your the shape you want to calculate the area of: ", ["Circle", "Rectangle", "Triangle"])
    if radio_button2 == "Rectangle":
        x = st.number_input("Enter your the length")
        y = st.number_input("Enter your the breadth")
        rectangle = geometry.Area_rectagle(x, y)
        if st.button("Get result"):
            st.success("The area of the rectangle is {}".format(rectangle))
            st.balloons()
    elif radio_button2 == "Circle":
        x = st.number_input("Enter the radius of your circle")
        circle = geometry.area_circle(x)
        if st.button("Get result"):
            st.error("The area of the circle is {}".format(circle))
    elif radio_button2 == "Triangle":
        x = st.number_input("Enter the breadth of the triangle")
        y = st.number_input("Enter the height of the triangle")
        triangle = geometry.area_triangle(x, y)
        if st.button("Get result"):
            result_triangle = geometry.area_triangle(x, y)
            st.warning("The area of the triangle is {}".format(triangle))
    else:
        st.write("please select a calculation")
elif dropdown == "":
    st.sidebar.write("Please select a module first")
col1, col2, col3 = st.columns(3)
temp = """<h3> <div style = "color:cyan; text-align:center">This app is developed by code2change students </h3>
                    </div>""" #allows multiple lines of html
#css colour codes available online, basic css

col1.markdown(temp,unsafe_allow_html=True)
col2.write("Copyright@code2change")
col3.write("Streamlit is awesome")