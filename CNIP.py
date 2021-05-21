#CN IP, download for PeerGuardian2 Format
#https://www.ip2location.com/free/visitor-blocker
import pandas as pd
data = pd.read_table('xx.txt',header=None)
raw_ip = data.iloc[6:,:].reset_index(drop = True)
ip_list = ''

for _, row in raw_ip.iterrows():
    ip = row[0].split(':')[1]
    ip_list += ip + ';' + '\n'

with open("xx.txt","w") as f:
    f.write(ip_list)