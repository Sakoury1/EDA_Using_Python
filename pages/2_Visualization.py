import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Dashboard"
                   ,page_icon="👋"
                   ,layout="wide"
                   ,initial_sidebar_state="expanded")


Cleaned=pd.read_csv("Data/Cleaned_data.csv")

total_amount=Cleaned["total_amount"].sum()

Net_Profit=Cleaned[Cleaned['Quantity']>0]["total_amount"].sum().round(1)-Cleaned[Cleaned['status'].isin(["Returned","Canceled"])]["total_amount"].sum()

Return=Cleaned[Cleaned['status'].isin(["Returned","Canceled"])]["total_amount"].sum().round(1)

Price=Cleaned["Price"].mean().round(1)
Count_Order=Cleaned["TransactionID"].count()


tab1,tab2,tab3=st.tabs(["Sales","Product_Analysis","Customer_Analysis"])

with tab1:
    st.markdown("""
    <style>

    [data-testid="stMetric"] {
        background-color: #0f172a;  
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    }

    [data-testid="stMetricLabel"] {
        color: #cbd5f5;
        font-size: 14px;
    }

    [data-testid="stMetricValue"] {
        color: #22c55e;  
        font-size: 32px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    st.header("Sales_Dashboard")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total_amount",f"{total_amount/1_000_000:.2f}M")

    with col2:
        st.metric("Net_Profit",f"{Net_Profit/1_000_000:.2f}M")

    with col3:
        st.metric("Returns",f"{Return/1_000:.2f}K")

    with col4:
        st.metric("#Order",Count_Order)

    c1,c2=st.columns(2)
    with c1:
        
        avg_totalAmount_Per_Region=Cleaned.groupby("Region",as_index=False)["total_amount"].sum().sort_values(by="total_amount",ascending=True)
        fig=px.bar(avg_totalAmount_Per_Region,x="Region",y="total_amount",title="Total_amount_by_Region",color="total_amount",color_continuous_scale=["#0FF05E","#0E4924","#07652a", "#105529","#043716"])
        fig.update_traces(texttemplate='%{y:.2s}',textposition='outside')
        fig.update_coloraxes(showscale=False) 
        st.plotly_chart(fig)
    with c2:
        total_amount_per_Category=Cleaned.groupby("Category",as_index=False)["total_amount"].sum().sort_values(by="total_amount",ascending=False)
        fig2=px.pie(data_frame=total_amount_per_Category,names="Category",values="total_amount",title="total_amount_by_Category",color_discrete_sequence=["#62a067","#5be662","#43a047","#1b5e20"])
        st.plotly_chart(fig2)

    sales_by_Day = Cleaned.groupby("Day_Name",as_index=False)["total_amount"].sum()
    fig = px.line(sales_by_Day,x="Day_Name",y="total_amount",markers=True,title="Total_amount_by_Day", color_discrete_sequence=["#22c55e"] )
    st.plotly_chart(fig, use_container_width=True)



with tab2:
    st.header("Proudct_Analysis")
    Prouduct=Cleaned["ProductID"].nunique()
    Avg_Price=Cleaned["Price"].mean().round(1)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total_amount",f"{total_amount/1_000_000:.2f}M")

    with col2:
        st.metric("Net_Profit",f"{Net_Profit/1_000_000:.2f}M")

    with col3:
        st.metric("Avg_Price",Avg_Price)

    with col4:
        st.metric("#Prouduct",Prouduct)
    
    c1,c2=st.columns(2)
    with c1:
        count_Transaction_ProductID = Cleaned.groupby("ProductID",as_index=False)["total_amount"].sum().sort_values(by= "total_amount",ascending=True).tail(5)
        fig=px.bar(data_frame=count_Transaction_ProductID,x="total_amount",y="ProductID",orientation='h',title="Total_amount_By_Product",color="total_amount",color_continuous_scale=["#62a067","#5be662","#43a047","#1b5e20"])
        fig.update_traces(text=count_Transaction_ProductID["total_amount"], textposition="outside", texttemplate='%{text:,.0f}')
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig)
    with c2:
        count_Transaction = Cleaned.groupby("Month_Name",as_index=False)["TransactionID"].count().sort_values(by= "TransactionID",ascending=False).head(5)
        fig=px.pie(data_frame=count_Transaction,names="Month_Name",values="TransactionID",title="Orders_BY_Month",color_discrete_sequence=["#5be662","#1b5e20"])

        st.plotly_chart(fig)
    

with tab3:
    st.header("Customer_Analysis")
    Customer=Cleaned["CustomerID"].nunique()
    Avg_Price=Cleaned["Price"].mean().round(1)
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        st.metric("Total_amount",f"{total_amount/1_000_000:.2f}M")

    with col2:
        st.metric("Net_Profit",f"{Net_Profit/1_000_000:.2f}M")

    with col3:
        st.metric("Avg_Price",Avg_Price)
    
    with col4:
        st.metric("#Customer",Customer)
        
    c1,c2=st.columns(2)
    with c1:

        custmoerby_region=Cleaned.groupby("Region")["CustomerID"].nunique().reset_index().sort_values("CustomerID",ascending=True)
        fig=px.bar(custmoerby_region,x="CustomerID",y="Region",color="CustomerID",title="Customer_by_Region",color_continuous_scale=["#62a067","#5be662","#43a047","#1b5e20"],orientation='h')
        fig.update_traces(texttemplate='%{x:.2s}',textposition='outside')
        fig.update_coloraxes(showscale=False) 
        st.plotly_chart(fig)

        Orders_Per_category = Cleaned.groupby("Category",as_index=False)["TransactionID"].count().sort_values(by= "TransactionID",ascending=True)
        fig = px.bar( Orders_Per_category,x="TransactionID",y="Category",color="TransactionID",title="Orders_byCateogry",color_continuous_scale=["#62a067","#5be662","#43a047","#1b5e20"],orientation='h')
        fig.update_coloraxes(showscale=False)
        fig.update_traces(texttemplate='%{x:.2s}',textposition='outside')
        st.plotly_chart(fig)

    with c2 :
       totalAmount_Per_Customer=Cleaned.groupby("CustomerID",as_index=False)["total_amount"].sum().sort_values(by="total_amount",ascending=True).tail(5)
       fig = px.bar( totalAmount_Per_Customer,x="total_amount",y="CustomerID",color="total_amount",title="Top5_Customerby_Total_amount",color_continuous_scale=["#62a067","#5be662","#43a047","#1b5e20"],orientation='h')
       fig.update_coloraxes(showscale=False)
       fig.update_traces(texttemplate='%{x:.2s}',textposition='outside')
       st.plotly_chart(fig)

       totalAmount_Per_Customer=Cleaned.groupby("status",as_index=False)["CustomerID"].count().sort_values(by="CustomerID",ascending=True).tail(5)
       fig = px.bar( totalAmount_Per_Customer,x="CustomerID",y="status",color="CustomerID",title="Customerby_returns",color_continuous_scale=["#62a067","#43a047","#1b5e20"],orientation='h')
       fig.update_coloraxes(showscale=False)
       fig.update_traces(texttemplate='%{x:.2s}',textposition='outside')
       st.plotly_chart(fig)

    
    



    


