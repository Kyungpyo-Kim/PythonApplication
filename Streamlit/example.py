# ⛔️ BAD EXAMPLE: PRE-REFACTOR
import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv")  # no function → no cache, requires pandas import: 👎,👎
sample = data.head(100)  # not input into streamlit object: 👎
described_sample = sample.describe()  # input into streamlit object: ✅
st.write(described_sample)


# ✅ GOOD EXAMPLE
## app.py
import streamlit as st
from helpers import load_data, describe_sample

data = load_data()  # data import: ✅
described_sample = describe_sample(data, 100)  # input into streamlit object: ✅
st.write(described_sample)

## helpers.py
import streamlit as st
import pandas as pd


@st.cache
def load_data():
    return pd.read_csv("data.csv")


@st.cache
def describe_sample(dataset, nrows):
    sample = dataset.head(nrows)
    return sample.describe()