import streamlit as st
from PIL import Image, ImageOps, ImageDraw

st.set_page_config(layout="wide")

st.title("👨‍💻 Our Team")

col1, col2 = st.columns(2, gap="large")

def linkedin_style_image(image_path, size=(300, 300), centering=(0.5, 0.4)):
    img = Image.open(image_path).convert("RGB")

  
    img = ImageOps.fit(
        img,
        size,
        method=Image.LANCZOS,
        centering=centering  
    )

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    img = img.convert("RGBA")
    img.putalpha(mask)

    return img

card_style = """
<style>
.card {
    background-color: transparent;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}

.name {
    font-size: 24px;
    font-weight: 600;
    margin-top: 15px;
}

.role {
    color: gray;
    margin-top: -5px;
    margin-bottom: 10px;
}

.icons img {
    margin: 8px;
    transition: 0.25s;
}

.icons img:hover {
    transform: scale(1.15);
}
</style>
"""

st.markdown(card_style, unsafe_allow_html=True)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image(linkedin_style_image("Photos/Zyad.jpg"), width=200)

    st.markdown('<div class="name">Zyad Ahmed</div>', unsafe_allow_html=True)
    st.markdown('<div class="role"> Data Analytics Engineer</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/zyad-sakoury/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="32">
            </a>
            <a href="https://github.com/Sakoury1" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image(linkedin_style_image("Photos/Alaa.jpeg", centering=(0.5, 0.35)), width=200)

    st.markdown('<div class="name">Alaa Ahmed</div>', unsafe_allow_html=True)
    st.markdown('<div class="role">Data Engineer</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/alaa-ahmed-635111203" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="32">
            </a>
            <a href="https://github.com/3laaA7med" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
