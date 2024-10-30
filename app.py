import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt


st.title('Exploratory Analysis & Visualisasi Data untuk E-Commerce Public Dataset')

with st.sidebar:

    st.write(
        """
        # Identitas Diri
        Nama: Dimas Pangestu Aji Purnomo
        """)
    st.write('E-Mail: dimaspurnomo610@yahoo.com')
    st.write('Dicoding ID: gh4nd4')
    st.text(' ')
    st.header('Pertanyaan Bisnis')
    st.text("""Kategori produk apa saja yang
    sedang populer sehingga dapat
    direkomendasikan sebagai top 5
    rekomendari produk di halaman
    utama website agar pembeli tertarik
    membelinya pada 3 bulan terakhir?""")

    st.text("""Bagaimana perilaku pembeli selama
    3 bulan terakhir agar kita bisa mengambil
    tindakan terhadap jenis-jenis perilaku
    tersebut?
    """)

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Tab 1")
    s_date = st.date_input(label='Tanggal mulai', min_value=datetime.date(2000, 1, 1))
    e_date = st.date_input(label='Tanggal akhir', min_value=datetime.date(2000, 1, 1))

    new_df1 = pd.read_csv('/content/test1.csv')
    mask_s = (new_df1['month_order_approved_at'] >= str(s_date)) & (new_df1['month_order_approved_at'] <= str(e_date))
    test_df = new_df1.loc[mask_s]


    x = list(test_df['product_category_name'].value_counts().index[0:5])

    fig, ax = plt.subplots()
    ax.bar(x, test_df['product_category_name'].value_counts()[0:5],
        color = ['orange', 'red', 'purple', 'blue', 'green'])
    st.pyplot(fig)

with tab2:
    st.header("Tab 2")

    final_merge = pd.read_csv('/content/test2.csv')

    fig, ax = plt.subplots()
    ax.pie(final_merge.customer_segment.value_counts(),
        labels=final_merge.customer_segment.value_counts().index,
        autopct='%.0f%%')
    st.pyplot(fig)
