import pandas as pd
obj=pd.Series([80,75,90,92],index=["Chemistry","Physics","ICT","Math"])
print(obj["Physics":"Math"])