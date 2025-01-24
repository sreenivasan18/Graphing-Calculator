import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
    }
    .icon {
        margin-left: 15px;
    }
    </style>
    <div class="header-container">
        <a href="https://github.com/sreenivasan18/" target="_blank" class="icon">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" alt="GitHub">
        </a>
        <a href="https://www.linkedin.com/in/v-sreenivasan-187933282/" target="_blank" class="icon">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" alt="LinkedIn">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Graphing Calculator")
st.write("Visualize mathematical functions dynamically.")

st.header("Enter Function Details")
function_input = st.text_input("Enter a mathematical function (use 'x' as the variable, e.g., 'sin(x)', 'x**2 - 4'):", value="sin(x)")
x_min = st.number_input("X-axis Minimum", value=-10.0)
x_max = st.number_input("X-axis Maximum", value=10.0)
num_points = st.slider("Number of Points for Plotting", min_value=100, max_value=5000, value=500)

if st.button("Plot Function"):
    try:
        x = np.linspace(x_min, x_max, num_points)
        y = eval(function_input, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp, "log": np.log, "sqrt": np.sqrt})

        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"y = {function_input}", color="blue")
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
        ax.grid(color="gray", linestyle="--", linewidth=0.5)
        ax.legend()

        ax.set_title("Graph of the Function")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
