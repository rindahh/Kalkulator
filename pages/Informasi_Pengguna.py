import streamlit as st

st.title('Informasi Pengguna')

st.subheader("Banyak Data (n)")
st.write("Pada bagian input 'banyak data (n)', pengguna diminta untuk memasukkan jumlah data yang akan digunakan dalam analisis regresi dan korelasi. Nilai minimum yang diperbolehkan adalah 2.")

st.subheader("Data untuk Mencari Regresi dan Korelasi")
st.write("Setelah pengguna mengirimkan jumlah data, akan ditampilkan tabel kosong dengan dua kolom, yaitu 'Variabel Prediktor (X)' dan 'Variabel Respon (Y)'. Pengguna dapat mengisi nilai-nilai data pada tabel tersebut. Setelah selesai mengisi, pengguna dapat menekan tombol 'OK' untuk melanjutkan dan untuk memunculkan hasil regresi, hasil korelasi, model regresi, dan grafik.")

st.subheader("Hasil Regresi")
st.write("Hasil regresi akan menampilkan nilai koefisien determinasi (R-squared). Koefisien determinasi mengukur sejauh mana variabilitas data respon dapat dijelaskan oleh variabel prediktor dalam model regresi linier. Nilai R-squared berkisar antara 0 hingga 1, dimana semakin mendekati 1 menunjukkan hubungan yang lebih kuat antara variabel prediktor dan variabel respon.")

st.subheader("Hasil Korelasi")
st.write("Hasil korelasi akan menampilkan korelasi antara variabel prediktor (X) dan variabel respon (Y). Nilai korelasi berkisar antara -1 hingga 1, dimana nilai positif menunjukkan korelasi positif antara variabel dan nilai negatif menunjukkan korelasi negatif. Nilai korelasi yang mendekati 1 atau -1 menunjukkan hubungan yang lebih kuat antara variabel prediktor dan variabel respon.")

st.subheader("Model Regresi")
st.write("Model regresi dalam bentuk persamaan matematika 'y = a + bx', di mana 'a' merupakan intercept (nilai konstanta) dan 'b' merupakan koefisien dari variabel prediktor (X). Persamaan ini menjelaskan hubungan antara variabel prediktor dan variabel respon dalam model regresi linier.")

st.subheader("Grafik Regresi dan Korelasi")
st.write("Hasil regresi akan ditampilkan dalam bentuk grafik scatter plot, di mana titik-titik biru mewakili data yang diinputkan, dan garis merah mewakili model regresi. Grafik ini membantu untuk memvisualisasikan hubungan antara variabel prediktor dan variabel respon dalam regresi linier.")