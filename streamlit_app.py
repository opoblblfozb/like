import streamlit as st

from matplotlib import pyplot as plt
import japanize_matplotlib

st.title("ゆきちゃん大好き！ピヨピヨ")
st.markdown(
    """
    hogehoge
    """
)

def exp(x):
    return [10 ** t for t in x]

x = [i /30 for i in range(50)]
fig, ax = plt.subplots()
ax.plot(x, exp(x))
ax.set_title("ゆきちゃんへの溺愛度")
ax.set_xlabel("時間")
ax.set_ylabel("溺愛度")
st.pyplot(fig)