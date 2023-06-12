import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.title('Kalkulator Regresi dan Korelasi')

with st.form('data'):
    data = st.number_input('banyak data (n)', min_value=2)
    submit_button = st.form_submit_button('kirim')

    st.write('data untuk mencari regresi dan korelasi')
    df = pd.DataFrame(columns=["Variabel Prediktor (X)", "Variabel Respon (Y)"], index=range(1, data+1), dtype=float)
    df_input = st.data_editor(df, use_container_width=True)
    submit_button_2 = st.form_submit_button('OK')

if submit_button_2:
    X = df_input["Variabel Prediktor (X)"].to_numpy().reshape(-1, 1)
    Y = df_input["Variabel Respon (Y)"].to_numpy().reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, Y)
    a = model.intercept_
    b = model.coef_[0]
    Y_pred = model.predict(X)

    r2 = r2_score(Y, Y_pred)

    st.subheader("Hasil Regresi")
    st.write("Koefisien Determinasi (R-squared):", r2)

    correlation_matrix = np.corrcoef(X.T, Y.T)
    correlation = correlation_matrix[0, 1]

    st.subheader("Hasil Korelasi")
    st.write("Korelasi antara Variabel Prediktor (X) dan Variabel Respon (Y):", correlation)

    st.subheader("Model Regresi : y = {:.2f} + {:.2f}x".format(a[0], b[0]))

    st.subheader("Grafik Regresi dan Korelasi")

    fig, ax = plt.subplots()
    ax.scatter(X, Y, color='blue', label='Data')
    ax.plot(X, Y_pred, color='red', label='Regresi')
    ax.set_xlabel('Variabel Prediktor (X)')
    ax.set_ylabel('Variabel Respon (Y)')
    ax.legend()

    st.pyplot(fig)