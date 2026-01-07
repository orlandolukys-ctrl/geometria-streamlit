import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="Geometría", layout="centered")

st.title("📐 App de Geometría")
st.markdown("**Desarrollado por Ing Orlando Ramirez Rodriguez**")


figura = st.selectbox(
    "Seleccione una figura:",
    ["Cuadrado", "Círculo"]
)

if figura == "Cuadrado":
    lado = st.number_input("Lado del cuadrado", min_value=0.0)
    area = lado ** 2
    perimetro = 4 * lado

    st.write(f"**Área:** {area}")
    st.write(f"**Perímetro:** {perimetro}")

    if lado > 0:
        x = [0, lado, lado, 0, 0]
        y = [0, 0, lado, lado, 0]

        plt.figure()
        plt.plot(x, y)
        plt.fill(x, y, alpha=0.3)
        plt.axis("equal")
        st.pyplot(plt)

elif figura == "Círculo":
    radio = st.number_input("Radio del círculo", min_value=0.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio

    st.write(f"**Área:** {area}")
    st.write(f"**Perímetro:** {perimetro}")

    if radio > 0:
        circle = plt.Circle((0, 0), radio, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(circle)
        ax.set_aspect("equal")
        ax.set_xlim(-radio*1.2, radio*1.2)
        ax.set_ylim(-radio*1.2, radio*1.2)
        st.pyplot(fig)

st.divider()

