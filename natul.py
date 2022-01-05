import streamlit as st

st.title('Memory 2021')
st.caption('jadi karena ndada waktuku mengedit vidio, kita buat web aja kali ya tiap pertemuan kita (walaupun adaji drive kusimpan) tapi anggaplah ini web buat simpan best foto')
st.header('Pertemuan 1 : Nonton Spiderman')
col1, col2 = st.columns(2)
with col1:
    st.image("1_1.jpg")

with col2:
    st.image("1_2.jpg")

with st.expander("Caption"):
     st.write("lihat ges foto pertama kita berdua xixixi.... makasih kepada indah yang sudah mau jadi nyamuk pertama dalam hubungan ini")

st.header('Pertemuan 2 : ngedate berdua')
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('mirror selfie')
    st.image("2_1.jpeg")
    st.caption('ini waktu di toko baju cuman numpang foto')

with col2:
    st.subheader('Foto kaki ala2')
    st.image("2_2.jpeg")
    st.caption('ini gatau anda foto kapan si')

with col3:
    st.subheader('kenyang bodo2')
    st.image("2_3.jpeg")
    st.caption('ini waktu kita makan di tsm terus lanjut ke cafe ombak. sayangnya gaada foto d cafe ombak wkwkwk')


st.header('Pertemuan 3 : Ramang-ramang with p3k21')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Foto candid')
    st.image("3_1.jpg")

with col2:
    st.subheader('Foto tegang')
    st.image("3_2.jpg")

with st.expander("Caption"):
     st.write("Ini foto pas dengan anak2 pmr ke ramang-ramang, penuh dengan cie2an dari anak2 wkwkw")

st.header('Pertemuan 4 : Main Badminton')
st.subheader('Gaada foto berdua :(')
st.image("4_1.jpeg")
with st.expander("Caption"):
     st.write("Ini pas main badminton di laniang bersama sepupu2 yuyun. walaupun nda sempat ki main berdua krn fauzul misscom wkwkw")

st.header('Pertemuan 5 : ngedate bersama 2 nyamuk')
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('Kenyang bodo2 part 2')
    st.image("5_1.jpeg")
    st.caption('ini lagi makan ayce sampai kenyang bodo2')

with col2:
    st.subheader('Foto melihat pantai')
    st.image("5_2.jpeg")
    st.caption('ini di pantai bosowa yang airnya pake busa')

with col3:
    st.subheader('Foto duduk2 melihat pantai')
    st.image("5_3.jpeg")
    st.caption('ini juga di bosowa melihat awan colonimbus hitam')

col1, col2 = st.columns(2)
with col1:
    st.subheader('Miss universe')
    st.image("5_4.jpeg")
    st.caption('ini natul over gulanya jadi terlalu manis (cantik banget woi)')

with col2:
    st.subheader('Foto bedua')
    st.image("5_5.jpeg")
    st.caption('ini natul bersama kopi pahit biar dia ga terlalu manis xixixi (jokes bapak2)')

st.subheader('Penutup')
with st.expander("Open this"):
    st.caption("""
        Hai natul, sepertinya ketika anda melihat web ini berarti 
        anda sudah menerima hadiah ku. 
        Jadi jam itu untuk hadiah ultahmu hehe (maap telat)
        Nda tau ka nulis yg bagus2 dan indah2 jadi mau ja bilang makasih 
        makasih karena telah mau jadi salahh satu bagian penting dalam hidupku (anjay)
        makasih menyempatkan waktunya bertemu di makassar 
        dahhh itu aja natul, intinya ya makasih wkwkwk
        sampai jumpa lagi di makassar kalau libur kuliah ma xixixixi 
        nanti kita bikin web baru lagi untuk memori 2022 wkwkwk
        if u wanna masuk drive bisa lewat link : https://bit.ly/Natul18
        natul, kalau nanti ada masalah sama hubungan ta tanya ka nah 
        jgn mi curhat ke org lain :(

        lop u, nat  """)

