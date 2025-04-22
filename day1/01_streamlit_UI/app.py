import streamlit as st
import pandas as pd
import numpy as np
import time

# ページ設定
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4a90e2;
        }
        .section-title {
            font-size: 1.5em;
            margin-top: 30px;
            color: #5F5;
            border-bottom: 2px solid #4a90e2;
            padding-bottom: 5px;
        }
        .footer {
            color: gray;
            font-size: 0.9em;
        }
        .stButton>button {
            background-color: #4a90e2;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# タイトルと説明
st.markdown('<div class="main-title">Streamlit 初心者向けデモ</div>', unsafe_allow_html=True)
st.info("このデモでは、さまざまなUI要素使用しています！")

# サイドバー
# st.sidebar.header("デモのガイド")
# st.sidebar.markdown("以下のセクションに沿って進めてください：")
# st.sidebar.markdown("- 基本UI\n- レイアウト\n- データ表示\n- グラフ\n- インタラクション")

# 基本的なUI要素
st.markdown('<div class="section-title">基本的なUI要素</div>', unsafe_allow_html=True)
name = st.text_input("あなたの名前", "ゲスト")
st.write(f"こんにちは、{name}さん！")

if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")

if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
    st.info("これは隠れたコンテンツです！")

age = st.slider("年齢を選んでください", 0, 100, 25)
st.write(f"あなたの年齢: {age}")

option = st.selectbox("好きなプログラミング言語は？", 
                      ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "other", "none"])
st.write(f"あなたは **{option}** を選びました。")

# レイアウト
st.markdown('<div class="section-title">レイアウト</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write("🔹 これは左カラムです")
    st.number_input("数値を入力", value=10)
with col2:
    st.write("🔸 これは右カラムです")
    st.metric("メトリクス", "42", "2%")

# データ表示
st.markdown('<div class="section-title">データの表示</div>', unsafe_allow_html=True)
df = pd.DataFrame({
    '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
    '年齢': [25, 30, 22, 28, 33],
    '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
})
st.dataframe(df, use_container_width=True)

# グラフ表示（Pythonのpandasの機能を使用）
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(chart_data)

bar_data = pd.DataFrame({'カテゴリ': ['A', 'B', 'C', 'D'], '値': [10, 25, 15, 30]}).set_index('カテゴリ')
st.bar_chart(bar_data)

st.markdown('<div class="footer">© コピーライトもどき</div>', unsafe_allow_html=True)
