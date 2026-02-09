
import streamlit as st 
import pandas as pd
import plotly.express as px
from PIL import Image, ImageOps, ImageDraw

tab1,tab2=st.tabs(["Data_Cleaning","Data_Modeding"])

with tab1 :
        st.title("Data_Cleaning")
        st.write("**1_Drop_duplicates**")
        st.code('customers.drop_duplicates(subset="CustomerID",keep="first",inplace=True)')

        st.write("**2_Change Type to Date**")
        st.code('customers["Signup_Date"]=pd.to_datetime(customers["Signup_Date"])')

        st.write("**3_Mapping Values**")
        st.code("""region_map ={"east":"East","west":"West",
            "north":"North","south":"South","midwest":"Midwest"}
        customers["Region"]=customers["Region"].replace(region_map)
        """)


        st.write("**4_Made Year 2033 to 2023**")
        st.code("""sales['Date'] = pd.to_datetime(sales['Date'], errors='coerce')
        sales.loc[sales['Date'].dt.year == 2033, 'Date'] -= pd.DateOffset(years=10)""")

        st.write("**5_Status of Order(Approved , Canceled , Returned)**")
        st.code("""sales["status"] = np.where(
        sales["Quantity"] > 0, "Approved",
        np.where(sales["Quantity"] == 0, "Canceled", "Returned")  
        )""")

        st.write("**6_Handel Null in Date**")
        st.code("""mask = sales['Date'].isna()
        sales.loc[mask, 'Date'] = (
        sales['Date'].shift(1)
        .loc[mask]
        + pd.Timedelta(hours=1)
        )""")

        st.write("**7_Handel Worng Data**")
        st.code("""sales["Quantity"] = sales["Quantity"].replace({1000:10})
        sales["CustomerID"] = sales["CustomerID"].replace({"CUST-999":"CUST-099"})""")

        st.write("**8_Remove Spacees**")
        st.code("""products['ProductID'] = products['ProductID'].str.strip()
        customers['CustomerID'] = customers['CustomerID'].str.strip()
        sales['ProductID'] = sales['ProductID'].str.strip()
        sales['CustomerID'] = sales['CustomerID'].str.strip()""")

        st.write("**9_Handel Error in Total_amount**")
        st.code("""sales.drop(columns=["Total_Amount"],inplace=True)
        df=sales.merge(products,on="ProductID",how="left")
        df=df.merge(customers,on="CustomerID",how="left")
        df["total_amount"]=df["Price"]*df["Quantity"]
        df["total_amount"]= df["total_amount"]-(df["total_amount"]*df["Discount"])
        df["total_amount"]=df["total_amount"].round(2)
        df""")

        st.write('**10_Handel Quantity < 0**')
        st.code('df["Quantity"]=np.where(df["Quantity"]<=0  ,df["Quantity"]*-1,df["Quantity"])')

        
        st.write("**11_Create_Date_dim**")
        st.code("""df=pd.date_range(Cleaned.Date.min(),Cleaned.Date.max())
date=pd.DataFrame(df,index=range(len(df)))
date.columns=["Date"]
date["Month"]=date["Date"].dt.month_name()
date["Day"]=date["Date"].dt.day_name()
date""")
        
        st.write("**11_Data_Aanalysis**")
        st.code("""avgsales_byRegion=df.groupby("Region")["total_amount"].mean().sort_values(by="total_amount",ascending=False)
Orders_byRegion = df.groupby("Region")["TransactionID"].count().sort_values(by= "TransactionID",ascending=False)
monthly_sales = df.groupby("Month_Name")["total_amount"].sum()
                
total_amount_byCategory=df.groupby("Category")["total_amount"].sum().sort_values(by="total_amount",ascending=False)
total_amount_byregion =  df.groupby("Region")["total_amount"].sum().sort_values(by="total_amount", ascending=False)""")


with tab2 :
        
        
        st.write("**Data_Before_Cleaning**")
        st.code("""Before_Cleaned=pd.read_csv("Data/Before_Cleaned.csv")""")
        Before_Cleaned=pd.read_csv("Data/Before_Cleaned.csv")
        Before_Cleaned.drop("Unnamed: 0",axis=1,inplace=True)
        Cleaned=pd.read_csv("Data/Cleaned_data.csv")
        Cleaned.drop("Unnamed: 0",axis=1,inplace=True)
        with st.sidebar:
                col=st.multiselect("Before_Cleaned",Before_Cleaned.columns,default=Before_Cleaned.columns)
                col2=st.multiselect("After_Cleaned",Cleaned.columns,default=Cleaned.columns)
        st.write(Before_Cleaned.loc[:,col])
        st.write("**Data_After_Cleaning**")
        st.code("""After_Cleaned=pd.read_csv("Data/customers.csv")""")
        st.write(Cleaned.loc[:,col2])
    

