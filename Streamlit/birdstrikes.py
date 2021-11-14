import streamlit as st
from vega_datasets import data
from time import time
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np

@st.cache
def load_data():
    return pd.concat((data.airports() for _ in range(100)))


@st.cache
def select_rows(dataset, nrows):
    return dataset.head(nrows)


@st.cache
def describe(dataset):
    return dataset.describe()


rows = st.slider("Rows", min_value=100, max_value=3300 * 100, step=10000)

start_uncached = time()
dataset_uncached = pd.concat((data.airports() for _ in range(100)))
load_uncached = time()
dataset_sample_uncached = dataset_uncached.head(rows)
select_uncached = time()
describe_uncached_dataset = dataset_sample_uncached.describe()
finish_uncached = time()
benchmark_uncached = (
    f"Cached. Total: {finish_uncached - start_uncached:.2f}s"
    f" Load: {load_uncached - start_uncached:.2f}"
    f" Select: {select_uncached - load_uncached:.2f}"
    f" Describe: {finish_uncached - select_uncached:.2f}"
)

st.text(benchmark_uncached)
st.write(describe_uncached_dataset)

start_cached = time()
dataset_cached = load_data()
load_cached = time()
dataset_sample_cached = select_rows(dataset_cached, rows)
select_cached = time()
describe_cached_dataset = describe(dataset_sample_cached)
finish_cached = time()

benchmark_cached = (
    f"Cached. Total: {finish_cached - start_cached:.2f}s"
    f" Load: {load_cached - start_cached:.2f}"
    f" Select: {select_cached - load_cached:.2f}"
    f" Describe: {finish_cached - select_cached:.2f}"
)
st.text(benchmark_cached)
st.write(describe_cached_dataset)


cars = data.cars()

quantitative_variables = [
    "Miles_per_Gallon",
    "Cylinders",
    "Displacement",
    "Horsepower",
    "Weight_in_lbs",
    "Acceleration",
]


@st.cache
def get_y_vars(dataset, x, variables):
    corrs = dataset.corr()[x]
    remaining_variables = [v for v in variables if v != x]
    sorted_remaining_variables = sorted(
        remaining_variables, key=lambda v: corrs[v], reverse=True
    )
    format_dict = {v: f"{v} ({corrs[v]:.2f})" for v in sorted_remaining_variables}
    return sorted_remaining_variables, format_dict


st.header("Cars Dataset - Correlation Dynamic Dropdown")
x = st.selectbox("x", quantitative_variables)
y_options, y_formats = get_y_vars(cars, x, quantitative_variables)
y = st.selectbox(
    f"y (sorted by correlation with {x})", y_options, format_func=y_formats.get
)

plot = alt.Chart(cars).mark_circle().encode(x=x, y=y)

st.altair_chart(plot)



def mpl_scatter(dataset, x, y):
    fig, ax = plt.subplots()
    dataset.plot.scatter(x=x, y=y, alpha=0.8, ax=ax)
    return fig


def altair_scatter(dataset, x, y):
    plot = (
        alt.Chart(dataset, height=400, width=400)
        .mark_point(filled=True, opacity=0.8)
        .encode(x=x, y=y)
    )
    return plot


size = st.slider("Size", min_value=1000, max_value=100_000, step=10_000)
dataset = pd.DataFrame(
    {"x": np.random.normal(size=size), "y": np.random.normal(size=size)}
)

mpl_start = time()
mpl_plot = mpl_scatter(dataset, "x", "y")
mpl_finish = time()

st.pyplot(mpl_plot)
mpl_render = time()
st.subheader("Matplotlib")
st.write(f"Create: {mpl_finish - mpl_start:.3f}s")
st.write(f"Render: {mpl_render - mpl_finish:.3f}s")
st.write(f"Total: {mpl_render - mpl_start:.3f}s")

alt_start = time()
alt_plot = altair_scatter(dataset, "x", "y")
alt_finish = time()

st.altair_chart(alt_plot)
alt_render = time()
st.subheader("Altair")
st.write(f"Create: {alt_finish - alt_start:.3f}s")
st.write(f"Render: {alt_render - alt_finish:.3f}s")
st.write(f"Total: {alt_render - alt_start:.3f}s")

speedup = (mpl_render - mpl_start) / (alt_render - alt_start)
st.write(f"MPL / Altair Ratio: {speedup:.1f}x")