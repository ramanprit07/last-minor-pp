import streamlit as st
css_animation = """
<style>
  .typewriter h1 {
    overflow: hidden;
    white-space: nowrap;
    margin: 0 auto;
    letter-spacing: .15em;
    animation: 
      typing 3.5s steps(40, end),
      blink-caret .75s step-end 15,
      color-change 3.5s infinite;
  }

  @keyframes typing {
    from { width: 0 }
    to { width: 100% }
  }

  @keyframes blink-caret {
    from, to { opacity: 1 }
    50% { opacity: 0 }
  }

  @keyframes color-change {
    0% { color: #f00; }
    20% { color: #0f0; }
    40% { color: #00f; }
    60% { color: #ff0; }
    80% { color: #0ff; }
    100% { color: #f0f; }
  }

  .blinking-effect {
    animation: blink 1s step-end infinite;
  }

  @keyframes blink {
    0%, 49% { opacity: 1; }
    50%, 100% { opacity: 0; }
  }
</style>
"""

# HTML for the text
html_content = """
<div class="typewriter">
  <h1 class="blinking-effect">Cyber Threat Detection</h1>
</div>
"""

# Display in Streamlit
st.markdown(css_animation + html_content, unsafe_allow_html=True)
html_content = """
<style>
 .subheadline {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    color: #FFFFFF; /* white */
    background: linear-gradient(to right, #FF69B4, #33CC33, #0066FF, #FFC107); /* rainbow colors */
    background-size: 400px 100%; /* wave effect */
    animation: wave 3s infinite;
    padding: 10px;
    border-radius: 10px;
  }

  @keyframes wave {
    0% {
      background-position: 0% 50%;
    }
    100% {
      background-position: 100% 50%;
    }
  }
</style>

<h3 class="subheadline">
  Explore our features to know more about your food habits and nutrition intake.
"""

st.markdown(html_content, unsafe_allow_html=True)

