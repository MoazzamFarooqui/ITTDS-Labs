import pandas as pd

data={
    "Product_ID":[1,2,3,4,5],
    "Product_Name":["Shampoo","Hair Brush","Soap","Charger","Tooth Brush"],
    "Price":[120000,2500,4500,6000,35000],
    "Category":["Hygiene","Personal Accesories","Hygiene","Electronics","Hygiene"],
    "Stock_Quantity":[1000,500,10000,1000,1500]
}

df=pd.DataFrame(data)
print(df)

df.info()
df.describe()

avgprice=df["Price"].mean()
print(avgprice)

