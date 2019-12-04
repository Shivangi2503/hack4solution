# Python3 Program to 
# compute GST from original 
# and net prices. 
  
def Calculate_GST(org_cost, N_price): 
  
    # return value after calculate GST% 
    return (((N_price - org_cost) * 100) / org_cost); 
  
# Driver program to test above functions 
org_cost = 100
N_price = 120
print("GST = ",end='') 
  
print(round(Calculate_GST(org_cost, N_price)),end='') 
  
print("%") 
  
