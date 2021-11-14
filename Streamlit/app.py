import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt


# cache: the data will be downloaded only once and cached for future use
@st.cache
def get_data():
    return pd.read_csv(
        "http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2021-09-07/visualisations/listings.csv"
    )


df = get_data()

st.title("Streamlit 101: An in-depth introduction")
st.markdown("Welcome to this in-depth introduction to [...].")
st.header("Customary quote")
st.markdown("> I just love to go home, no matter where I am [...]")
st.dataframe(df.head())

st.code(
    """
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/[...]"
    return pd.read_csv(url)
""",
    language="python",
)

cols = ["name", "host_name", "neighbourhood", "room_type", "price"]
st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)

st.table(
    df.groupby("room_type")
    .price.mean()
    .reset_index()
    .round(2)
    .sort_values("price", ascending=False)
    .assign(avg_price=lambda x: x.pop("price").apply(lambda y: "%.2f" % y))
)

values = st.sidebar.slider("Price range", float(df.price.min()), 1000.0, (50.0, 300.0))
f = px.histogram(
    df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution"
)
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)

st.write("Using a radio button restricts selection to only one option at a time.")
neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
show_exp = st.checkbox("Include expensive listings")

# df.query("availability_365>0").groupby(
#     "neighbourhood_group"
# ).availability_365.mean().plot.bar(rot=0).set(
#     title="Average availability by neighborhood group",
#     xlabel="Neighborhood group",
#     ylabel="Avg. availability (in no. of days)",
# )
# st.pyplot()

minimum = st.sidebar.number_input("Minimum", min_value=0)
maximum = st.sidebar.number_input("Maximum", min_value=0, value=5)
if minimum > maximum:
    st.error("Please enter a valid range")
else:
    df.query("@minimum<=number_of_reviews<=@maximum")

pics = {
    "Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
    "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
    "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg",
}
pic = st.selectbox("Picture choices", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True, caption=pics[pic])

st.markdown("## Party time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
