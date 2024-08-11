import streamlit as st
import plotly.graph_objects as go

st.title("Animated Plot with Plotly")

fig = go.Figure(
    data=[go.Scatter(x=[0], y=[0], mode="lines+markers")],
    layout=go.Layout(
        xaxis=dict(range=[0, 10], autorange=False),
        yaxis=dict(range=[0, 10], autorange=False),
        title="Animating Line Plot"
    )
)

for i in range(1, 11):
    fig.add_trace(go.Scatter(x=[i], y=[i], mode="lines+markers"))

fig.update_layout(updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])])

st.plotly_chart(fig)
