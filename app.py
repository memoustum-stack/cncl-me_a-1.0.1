import streamlit as st

# Sayfa başlığı ve simgesi
st.set_page_config(page_title="Cnclime AI", page_icon="🤖")

# Ana başlık ve Ekip isimleri
st.title("🤖 Cnclime Süper Yapay Zeka")
st.subheader("Geliştiriciler: Mehmet Emin, Emre Can, Ömer Eymen, Yunus Emre")

# Kullanıcıdan soru alma kısmı
soru = st.text_input("Cnclime'a bir soru sor veya bir mesaj yaz:")

if soru:
    if "merhaba" in soru.lower():
        st.write("🤖 Cnclime: Merhaba ekip! Bugün ne yapıyoruz?")
    elif "kim yaptı" in soru.lower():
        st.success("Beni harika bir ekip olan Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre yaptı! 🚀")
    else:
        st.write(f"🤖 Cnclime: '{soru}' dediğin şeyi çok iyi anladım, üzerinde çalışıyorum!")
