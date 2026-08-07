def my_mean(column):
    return sum(column)/len(column)
my_mean_amount=my_mean(df["Amount"])
pandas_mean_amount=df["Amount"].mean()
dif=my_mean_amount-pandas_mean_amount
print("Difference=",dif)
