import streamlit as st
import streamlit.components.v1 as components
st.header("Movies Links")
st.write("Bharateeyudu 2 -[Bharateeyudu 2](https://www.5movierulz.best/bharateeyudu-2-2024-telugu/movie-watch-online-free-2966.html)")
st.write("PUSHPA 2 - [PUSHPA](https://day.ibomma.observer/ca-tex4c/pushpa-the-rule-part-2-2024-r2tdf-telugu-movie-watch-online.html)")
st.write("I bomma Link - [ibomma](https://osk.ibomma.wf/telugu-movies/)")
st.write(" Lucky Baskhar - [Lucky Baskhar](https://www.5movierulz.io/lucky-baskhar-2024-telugu/movie-watch-online-free-3649.html)")
st.write(" Movierulz - (https://www.5movierulz.rip/)")

video_file = open("myvideo.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
#components.iframe("https://www.youtube.com", width=800, height=600) 
#components.iframe("https://www.5movierulz.rip/daaku-maharaaj-2025-telugu/movie-watch-online-free-4064.html", width=800, height=600) 
