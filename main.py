import streamlit as st
import yfinance as fn

st.title("Stock Market")

st.sidebar.title("Your Selections")

comapany_name = st.sidebar.selectbox("Select Company", ("Select", "Apple", "Tesla", "Microsoft"))
info_check = st.sidebar.checkbox("Do you want to get Information?")
graph_check = st.sidebar.checkbox("Do you want to get Graph Plot?")


def get_ticker(name):
    company = fn.Ticker(name)
    return company


def plot_apple():
    apple = fn.download("AAPL", start="2020-01-01", end="2021-12-31")
    st.write(""" ### Apple """)
    st.write(apple)


def info_apple():
    c1 = get_ticker("AAPL")
    st.write(c1.info['longBusinessSummary'])


def graph_apple():
    c1 = get_ticker("AAPL")
    data1 = c1.history(period="3mo")
    st.line_chart(data1.values)


def plot_tesla():
    tesla = fn.download("TSLA", start="2020-01-01", end="2021-12-31")
    st.write(""" ### Tesla """)
    st.write(tesla)


def info_tesla():
    c2 = get_ticker("TSLA")
    st.write(c2.info['longBusinessSummary'])


def graph_tesla():
    c2 = get_ticker("TSLA")
    data2 = c2.history(period="3mo")
    st.line_chart(data2.values)


def plot_micrsoft():
    microsoft = fn.download("MSFT", start="2020-01-01", end="2021-12-31")
    st.write(""" ### Microsoft """)
    st.write(microsoft)


def info_microsoft():
    c3 = get_ticker("MSFT")
    st.write(c3.info['longBusinessSummary'])


def graph_microsoft():
    c3 = get_ticker("MSFT")
    data3 = c3.history(period="3mo")
    st.line_chart(data3.values)


if __name__ == '__main__':
    if comapany_name == "Apple":
        plot_apple()
    elif comapany_name == "Tesla":
        plot_tesla()
    else:
        plot_micrsoft()

    if info_check is True and comapany_name == "Apple":
        info_apple()
    elif info_check is True and comapany_name == "Tesla":
        info_tesla()
    elif info_check is True and comapany_name == "Microsoft":
        info_microsoft()

    if graph_check is True and comapany_name == "Apple":
        graph_apple()
    elif graph_check is True and comapany_name == "Tesla":
        graph_tesla()
    elif graph_check is True and comapany_name == "Microsoft":
        graph_microsoft()
