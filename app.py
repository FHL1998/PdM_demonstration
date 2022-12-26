import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Predictive Maintenance Pro',
                   layout='wide',
                   page_icon='✅')

# top row

st.markdown("## Predictive Maintenance Pro")

first_kpi, second_kpi, third_kpi, forth_kpi = st.columns(4)

with first_kpi:
    st.markdown("💵**Cost Saving**")
    number1 = '18%-25%'
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("🚩**Equipment Availability**")
    number2 = '5%-15%'
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("🚀**Remaining Useful Life**")
    number3 = '20%'
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with forth_kpi:
    st.markdown("💹**Compound Annual Growth Rate**")
    number3 = '30.6%'
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Size of the PdM market worldwide in 2020 and 2021, "
            "with a forecast for 2022 to 2030")

first_chart, second_chart = st.columns(2)

with first_chart:
    market_data = pd.read_csv('market_data.csv')
    print('market_data', market_data)
    # chart_data = pd.DataFrame(np.array([2.4, 4.2, 5.1, 6.2]).reshape(4, 2), columns=['a', 'b', 'c'])
    market_data_graph = px.bar(market_data, x='Year', y='Market Size', labels={'Market Size': 'Global Market Size('
                                                                                              'billion U.S. Dollars)'})
    st.plotly_chart(market_data_graph)

with second_chart:
    CAGR_data = pd.read_csv('CAGR_data.csv')
    print('CAGR_data', CAGR_data)
    chart_data = px.pie(CAGR_data, names="Country", values='CAGR',hole=0.4)
    chart_data.update_layout(
        title={  # 设置整个标题的名称和位置
            "text": "Compound Annual Growth Rate",
            "y": 0.96,  # y轴数值
            "x": 0.5,  # x轴数值
            "xanchor": "center",  # x、y轴相对位置
            "yanchor": "top"
        }
    )
    chart_data.update_traces(textposition='inside',
                      textinfo='percent+label')
    st.plotly_chart(chart_data)

st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("## Key Companies Profiled")
