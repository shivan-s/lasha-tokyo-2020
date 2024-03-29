#!usr/bin/python3
# main.py

import altair as alt
import pandas as pd
import streamlit as st

st.image("lasha.jpeg", caption="Lasha Lifting in Tokyo 2020. Image source from Infobae")

"""
# How Good Is Lasha?

The graph below shows all the z-scores of the lifters in the Tokyo 2020 Olympics.

The z-score is calculated using the difference between the individual's total and the mean total of all lifters in the individual's weight class divided by the standard deviation of these totals.

Calculating z-score:
"""
st.latex(
    r"""
        z = \frac{x - \mu}{\sigma}
        """
)

"""
The colour represents the lifter's ranking within the weight category.

The y-axis is the lifter's ranking in their weight category.
"""
df = pd.read_pickle("results_all.pkl")

# list for male and female
cat_lst = list(df["Category"].unique())
categories = st.container()
select_all = st.checkbox("Select All", value=True)
if select_all:
    selected_categories = categories.multiselect("Select", cat_lst, cat_lst)
else:
    selected_categories = categories.multiselect("Select", cat_lst)

df = df[df["Category"].isin(selected_categories)]

c = (
    alt.Chart(df, title="Z-scores of totals for Tokyo 2020 Olympic Lifters")
    .mark_circle()
    .encode(
        y=alt.Y("Rank:Q", title="Ranking", scale=alt.Scale(reverse=True)),
        x=alt.X("Normalised:Q", title="Z-score"),
        color=alt.Color("Rank:Q", legend=None, scale=alt.Scale(scheme="lightmulti")),
        tooltip=[
            "Name:N",
            "Date of Birth:N",
            "Rank:Q",
            "Category:N",
            "Country:N",
            "Final Total:Q",
        ],
    )
    .configure_facet(spacing=0)
    .configure_view(stroke=None)
)
st.altair_chart(c, use_container_width=True)


"""

## Feedback

This was made by [Shivan Sivakumaran](https://shivan.xyz).

[Here is the code](https://github.com/shivan-s/lasha-tokyo-2020)

I'm happy for any feedback. Hope you enjoy this and cheers!

"""
