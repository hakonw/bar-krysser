import streamlit as st
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import streamlit.components.v1 as components

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("regning.html")

st.title("Barsystem")

gjeng = st.selectbox("Gjeng", ["VK", "REGI"])
dato = st.date_input("Dato", pd.Timestamp.now())
csv_data = st.text_area("Kryssing (CSV format)", "person,44\nanother_person,55")

# TODO kanskje endre det litt
try:
    rows = []
    total = 0
    for line in csv_data.splitlines():
        if line.strip():
            name, amount = line.split(",")
            amount = int(amount)
            rows.append((name, amount))
            total += amount

    rendered_html = template.render(
        gjeng=gjeng,
        rows=rows,
        total=total,
        date=dato.strftime("%Y-%m-%d")
    )

    components.html(rendered_html, height=600, scrolling=True)

except Exception as e:
    st.error(f"Error: {e}")