import ctypes
import datetime
import math
import os
import random
import time

from DataStructures import *

# def getIntersectionNode(headA, headB):
#     temp = headA
#     node_list = []
#     flag = False
#
#     while temp:
#         node_list.append(id(temp))
#         temp = temp.next
#
#     temp = headB
#
#     while temp:
#         if id(temp) in node_list:
#             return ctypes.cast(id(temp), ctypes.py_object).value
#
#         temp = temp.next
#
#     return None
#
#
# join = ListNode(99)
# nodeA = ListNode(1, ListNode(2, ListNode(3, join)))
# nodeB = ListNode(-1, ListNode(-2, ListNode(-3, join)))
#
# print(f"Intersected at: {getIntersectionNode(nodeA, nodeB).val}")

sh = """AARTIIND
ABB
ABCAPITAL
ABFRL
ADANIENT
ADANIPORTS
ALKEM
AMARAJABAT
AMBUJACEM
APLLTD
APOLLOHOSP
APOLLOTYRE
ASHOKLEY
ASTRAL
ATUL
AUBANK
AUROPHARMA
BAJAJFINSV
BAJFINANCE
BALKRISIND
BALRAMCHIN
BANDHANBNK
BANKBARODA
BATAINDIA
BEL
BHARATFORG
BIOCON
BRATANNIA
BSOFT
CANBK
CANFINHOME
CHAMBLFERT
CHOLAFIN
CIPLA
COFORGE
CONCOR
COROMANDEL
CROMPTON
CUMMINSIND
DABUR
DALBHARAT
DEEPAKNTR
DELTACORP
DIVISLAB
DIXON
DLF
DRREDDY
ESCORTS
EXIDEIND
GLENMARK
GLS
GNFC
GODREJCP
GODREJPROP
GRANULES
GRASIM
GUJGASLTD
HAL
HAVELLS
HCLTECH
HDFCAMC
HDFCLIFE
HINDALCO
HINDCOPPER
ICICIGI
ICICIPRULI
IEX
IGL
INDHOTEL
INDIACEM
INDIAMART
INDIGO
INDUSINDBK
INDUSTOWER
INTELLECT
IPCALAB
JINDALSTEL
JKCEMENT
JSWSTEEL
JUBLFOOD
KOTAKBANK
LALPATHLAB
LAURUSLABS
LICHSGFIN
LTIM
LTTS
LUPIN
M&MFIN
MANAPPURAM
MARICO
MCDOWELL-N
MCX
METROPOLIS
MFSL
MGL
MPHASIS
MUTHOOTFIN
NAM-INDIA
NAUKRI
NAVINFLUOR
NMDC
NTPC
OBEROIRLTY
PEL
PERSISTENT
PETRONET
PIDILITIND
POLYCAB
POWERGRID
RAIN
RAMCOCEM
RBLBANK
RECLTD
SBICARD
SBILIFE
SIEMENS
SRF
STAR
SUNPHARMA
SYNGENE
TATACOMM
TECHM
TORNTPHARM
TORNTPOWER
TRENT
TVSMOTOR
UBL
ULTRACEMCO
UPL
VEDL
VOLTAS
ZEEL
ZYDUSLIFE"""

# L = sh.split("\n")
# print(L)
# j = 1
# for i in L:
#     print(i, end=" ")
#     if j % 3 == 0:
#         print()
#     # time.sleep(1)
#     j += 1
# print(len(L))

# for i in range(0, 11):
#     print(i**7)
#
# for i in range(0, 11):
#     print(i**109)


#
#
#
# y = round_up(12.16)
# print(y)
#
# x = Decimal("3.456")
# (x * 2).quantize(Decimal('.05'), rounding=ROUND_UP) / 2
#
# r = """AARTIIND
# ABB
# ABCAPITAL
# ABFRL
# ADANIENT
# ADANIPORTS
# ALKEM
# AMBUJACEM
# APOLLOHOSP
# APOLLOTYRE
# ASHOKLEY
# ASTRAL
# ATUL
# AUBANK
# AUROPHARMA
# BAJAJFINSV
# BAJFINANCE
# BALKRISIND
# BALRAMCHIN
# BANDHANBNK
# BANKBARODA
# BATAINDIA
# BEL
# BHARATFORG
# BIOCON
# BRITANNIA
# BSOFT
# CANBK
# CANFINHOME
# CHAMBLFERT
# CHOLAFIN
# CIPLA
# COFORGE
# CONCOR
# COROMANDEL
# CROMPTON
# CUMMINSIND
# DABUR
# DALBHARAT
# DEEPAKFERT
# DEEPAKNTR
# DELTACORP
# DIVISLAB
# DIXON
# DLF
# DRREDDY
# ESCORTS
# EXIDEIND
# GLENMARK
# GLS
# GNFC
# GODREJCP
# GODREJPROP
# GRANULES
# GRASIM
# GUJGASLTD
# HAL
# HAVELLS
# HCLTECH
# HDFCAMC
# HDFCLIFE
# HINDALCO
# HINDCOPPER
# ICICIGI
# ICICIPRULI
# IEX
# IGL
# INDHOTEL
# INDIACEM
# INDIAMART
# INDIGO
# INDUSINDBK
# INDUSTOWER
# INTELLECT
# IPCALAB
# JINDALSTEL
# JKCEMENT
# JSWSTEEL
# JUBLFOOD
# KOTAKBANK
# LALPATHLAB
# LAURUSLABS
# LICHSGFIN
# LTIM
# LTTS
# LUPIN
# M&MFIN
# MANAPPURAM
# MARICO
# MCDOWELL-N
# MCX
# METROPOLIS
# MFSL
# MGL
# MPHASIS
# MUTHOOTFIN
# NAM-INDIA
# NAUKRI
# NAVINFLUOR
# NMDC
# NTPC
# OBEROIRLTY
# PEL
# PERSISTENT
# PETRONET
# PIDILITIND
# POLYCAB
# POWERGRID
# RAIN
# RAMCOCEM
# RBLBANK
# RECLTD
# SBICARD
# SBILIFE
# SIEMENS
# SRF
# STAR
# SUNPHARMA
# SYNGENE
# TATACOMM
# TATAMOTORS
# TECHM
# TORNTPHARM
# TORNTPOWER
# TRENT
# TVSMOTOR
# UBL
# ULTRACEMCO
# UPL
# VEDL
# VOLTAS
# ZEEL
# ZYDUSLIFE"""
# ALGO_1_min_shares = r.split("\n")
#
# print(ALGO_1_min_shares)
# print(len(ALGO_1_min_shares))


# cash_share_names = ['ADANIENT', 'APOLLOTYRE', 'BAJAJFINSERV', 'BAJAJFINANCE', 'BANDHANBANK', 'BANKBARODA', 'COAL INDIA',
#                     'DLF CHL', 'EICHERMOTOR', 'FEDRAL BANK', 'HCLTECH', 'HDFC', 'ICICIBANK', 'INDUSINDBANK', 'INFY',
#                     'JINDALS chl', 'LICHSGFIN', 'M&M', 'M&MFINANCE', '03 RELIANCE CHL', '04 SBIN CHL', 'SUNTV',
#                     'TATACHEM', '07 TATAMOTOR CHL', 'TATAPOWER', '05 TATASTEEL chl', 'ULTRACHEM']
#
# cash_share_rows = [1579, 2946, 1579, 1579, 1579, 1579, 3232, 4058, 2715, 1579, 1579, 3936, 1579, 1579, 2765, 5195, 1579,
#                    1579, 1579, 4793, 4860, 1579, 1579, 4434, 1579, 4570, 2696]
# fo_share_names = ['ADANI PORT', 'AUROPHARMA', '02 BANKNIFTY F', 'CANBK', 'DLF', 'HINDALCO', 'ICICIBANK', 'JINDS',
#                   '01 NIFTY F', '03 RELIANCE', 'SBIN', 'TATACONSUM', '05 TATAMOTOR', '04 TATASTEEL', 'TCS', 'TITAN']
#
# fo_share_rows = [2279, 2789, 3309, 2016, 2831, 3989, 1093, 2274, 2795, 2792, 2793, 2276, 2791, 2793, 4826, 1762]
#
# d = {}
# i = 0
# for s in fo_share_names:
#     d[s] = fo_share_rows[i]
#     i+= 1
#
# print(d)


# for s in d:
#     print(s)
#
# count = 0
# insert_rows = [40, 52, 69, 71, 75, 77, 90, 106, 200, 231, 241, 260, 282, 314, 326, 330, 338, 343, 359, 408, 429, 445,
#                470, 485,
#                495, 543, 569, 580, 599, 600, 612, 682, 686, 698, 723, 738, 747, 804, 832, 849, 852, 855, 860, 871, 914,
#                947, 972,
#                981, 997]
#
# wb = xl.load_workbook(rf'C:\Users\admin\Downloads\current\{share}.xlsx')
# sheet = wb['D']
#
# for row in insert_rows:
#     sheet.insert_rows(row)
#
# wb.save(rf'C:\Users\admin\Downloads\current\{share}.xlsx')

r = """01-01-2020
02-01-2020
03-01-2020
06-01-2020
07-01-2020
08-01-2020
09-01-2020
10-01-2020
13-01-2020
14-01-2020
15-01-2020
16-01-2020
17-01-2020
20-01-2020
21-01-2020
22-01-2020
23-01-2020
24-01-2020
27-01-2020
28-01-2020
29-01-2020
30-01-2020
31-01-2020
01-02-2020
03-02-2020
04-02-2020
05-02-2020
06-02-2020
07-02-2020
10-02-2020
11-02-2020
12-02-2020
13-02-2020
14-02-2020
17-02-2020
18-02-2020
19-02-2020
20-02-2020
21-02-2020
24-02-2020
25-02-2020
26-02-2020
27-02-2020
28-02-2020
02-03-2020
03-03-2020
04-03-2020
05-03-2020
06-03-2020
09-03-2020
10-03-2020
11-03-2020
12-03-2020
13-03-2020
16-03-2020
17-03-2020
18-03-2020
19-03-2020
20-03-2020
23-03-2020
24-03-2020
25-03-2020
26-03-2020
27-03-2020
30-03-2020
31-03-2020
01-04-2020
02-04-2020
03-04-2020
06-04-2020
07-04-2020
08-04-2020
09-04-2020
10-04-2020
13-04-2020
14-04-2020
15-04-2020
16-04-2020
17-04-2020
20-04-2020
21-04-2020
22-04-2020
23-04-2020
24-04-2020
27-04-2020
28-04-2020
29-04-2020
30-04-2020
01-05-2020
04-05-2020
05-05-2020
06-05-2020
07-05-2020
08-05-2020
11-05-2020
12-05-2020
13-05-2020
14-05-2020
15-05-2020
18-05-2020
19-05-2020
20-05-2020
21-05-2020
22-05-2020
25-05-2020
26-05-2020
27-05-2020
28-05-2020
29-05-2020
01-06-2020
02-06-2020
03-06-2020
04-06-2020
05-06-2020
08-06-2020
09-06-2020
10-06-2020
11-06-2020
12-06-2020
15-06-2020
16-06-2020
17-06-2020
18-06-2020
19-06-2020
22-06-2020
23-06-2020
24-06-2020
25-06-2020
26-06-2020
29-06-2020
30-06-2020
01-07-2020
02-07-2020
03-07-2020
06-07-2020
07-07-2020
08-07-2020
09-07-2020
10-07-2020
13-07-2020
14-07-2020
15-07-2020
16-07-2020
17-07-2020
20-07-2020
21-07-2020
22-07-2020
23-07-2020
24-07-2020
27-07-2020
28-07-2020
29-07-2020
30-07-2020
31-07-2020
03-08-2020
04-08-2020
05-08-2020
06-08-2020
07-08-2020
10-08-2020
11-08-2020
12-08-2020
13-08-2020
14-08-2020
17-08-2020
18-08-2020
19-08-2020
20-08-2020
21-08-2020
24-08-2020
25-08-2020
26-08-2020
27-08-2020
28-08-2020
31-08-2020
01-09-2020
02-09-2020
03-09-2020
04-09-2020
07-09-2020
08-09-2020
09-09-2020
10-09-2020
11-09-2020
14-09-2020
15-09-2020
16-09-2020
17-09-2020
18-09-2020
21-09-2020
22-09-2020
23-09-2020
24-09-2020
25-09-2020
28-09-2020
29-09-2020
30-09-2020
01-10-2020
02-10-2020
05-10-2020
06-10-2020
07-10-2020
08-10-2020
09-10-2020
12-10-2020
13-10-2020
14-10-2020
15-10-2020
16-10-2020
19-10-2020
20-10-2020
21-10-2020
22-10-2020
23-10-2020
26-10-2020
27-10-2020
28-10-2020
29-10-2020
30-10-2020
02-11-2020
03-11-2020
04-11-2020
05-11-2020
06-11-2020
09-11-2020
10-11-2020
11-11-2020
12-11-2020
13-11-2020
16-11-2020
17-11-2020
18-11-2020
19-11-2020
20-11-2020
23-11-2020
24-11-2020
25-11-2020
26-11-2020
27-11-2020
30-11-2020
01-12-2020
02-12-2020
03-12-2020
04-12-2020
07-12-2020
08-12-2020
09-12-2020
10-12-2020
11-12-2020
14-12-2020
15-12-2020
16-12-2020
17-12-2020
18-12-2020
21-12-2020
22-12-2020
23-12-2020
24-12-2020
25-12-2020
28-12-2020
29-12-2020
30-12-2020
31-12-2020
01-01-2021
04-01-2021
05-01-2021
06-01-2021
07-01-2021
08-01-2021
11-01-2021
12-01-2021
13-01-2021
14-01-2021
15-01-2021
18-01-2021
19-01-2021
20-01-2021
21-01-2021
22-01-2021
25-01-2021
26-01-2021
27-01-2021
28-01-2021
29-01-2021
01-02-2021
02-02-2021
03-02-2021
04-02-2021
05-02-2021
08-02-2021
09-02-2021
10-02-2021
11-02-2021
12-02-2021
15-02-2021
16-02-2021
17-02-2021
18-02-2021
19-02-2021
22-02-2021
23-02-2021
24-02-2021
25-02-2021
26-02-2021
01-03-2021
02-03-2021
03-03-2021
04-03-2021
05-03-2021
08-03-2021
09-03-2021
10-03-2021
11-03-2021
12-03-2021
15-03-2021
16-03-2021
17-03-2021
18-03-2021
19-03-2021
22-03-2021
23-03-2021
24-03-2021
25-03-2021
26-03-2021
29-03-2021
30-03-2021
31-03-2021
01-04-2021
02-04-2021
05-04-2021
06-04-2021
07-04-2021
08-04-2021
09-04-2021
12-04-2021
13-04-2021
14-04-2021
15-04-2021
16-04-2021
19-04-2021
20-04-2021
21-04-2021
22-04-2021
23-04-2021
26-04-2021
27-04-2021
28-04-2021
29-04-2021
30-04-2021
03-05-2021
04-05-2021
05-05-2021
06-05-2021
07-05-2021
10-05-2021
11-05-2021
12-05-2021
13-05-2021
14-05-2021
17-05-2021
18-05-2021
19-05-2021
20-05-2021
21-05-2021
24-05-2021
25-05-2021
26-05-2021
27-05-2021
28-05-2021
31-05-2021
01-06-2021
02-06-2021
03-06-2021
04-06-2021
07-06-2021
08-06-2021
09-06-2021
10-06-2021
11-06-2021
14-06-2021
15-06-2021
16-06-2021
17-06-2021
18-06-2021
21-06-2021
22-06-2021
23-06-2021
24-06-2021
25-06-2021
28-06-2021
29-06-2021
30-06-2021
01-07-2021
02-07-2021
05-07-2021
06-07-2021
07-07-2021
08-07-2021
09-07-2021
12-07-2021
13-07-2021
14-07-2021
15-07-2021
16-07-2021
19-07-2021
20-07-2021
21-07-2021
22-07-2021
23-07-2021
26-07-2021
27-07-2021
28-07-2021
29-07-2021
30-07-2021
02-08-2021
03-08-2021
04-08-2021
05-08-2021
06-08-2021
09-08-2021
10-08-2021
11-08-2021
12-08-2021
13-08-2021
16-08-2021
17-08-2021
18-08-2021
19-08-2021
20-08-2021
23-08-2021
24-08-2021
25-08-2021
26-08-2021
27-08-2021
30-08-2021
31-08-2021
01-09-2021
02-09-2021
03-09-2021
06-09-2021
07-09-2021
08-09-2021
09-09-2021
10-09-2021
13-09-2021
14-09-2021
15-09-2021
16-09-2021
17-09-2021
20-09-2021
21-09-2021
22-09-2021
23-09-2021
24-09-2021
27-09-2021
28-09-2021
29-09-2021
30-09-2021
01-10-2021
04-10-2021
05-10-2021
06-10-2021
07-10-2021
08-10-2021
11-10-2021
12-10-2021
13-10-2021
14-10-2021
15-10-2021
18-10-2021
19-10-2021
20-10-2021
21-10-2021
22-10-2021
25-10-2021
26-10-2021
27-10-2021
28-10-2021
29-10-2021
01-11-2021
02-11-2021
03-11-2021
04-11-2021
05-11-2021
08-11-2021
09-11-2021
10-11-2021
11-11-2021
12-11-2021
15-11-2021
16-11-2021
17-11-2021
18-11-2021
19-11-2021
22-11-2021
23-11-2021
24-11-2021
25-11-2021
26-11-2021
29-11-2021
30-11-2021
01-12-2021
02-12-2021
03-12-2021
06-12-2021
07-12-2021
08-12-2021
09-12-2021
10-12-2021
13-12-2021
14-12-2021
15-12-2021
16-12-2021
17-12-2021
20-12-2021
21-12-2021
22-12-2021
23-12-2021
24-12-2021
27-12-2021
28-12-2021
29-12-2021
30-12-2021
31-12-2021
03-01-2022
04-01-2022
05-01-2022
06-01-2022
07-01-2022
10-01-2022
11-01-2022
12-01-2022
13-01-2022
14-01-2022
17-01-2022
18-01-2022
19-01-2022
20-01-2022
21-01-2022
24-01-2022
25-01-2022
26-01-2022
27-01-2022
28-01-2022
31-01-2022
01-02-2022
02-02-2022
03-02-2022
04-02-2022
07-02-2022
08-02-2022
09-02-2022
10-02-2022
11-02-2022
14-02-2022
15-02-2022
16-02-2022
17-02-2022
18-02-2022
21-02-2022
22-02-2022
23-02-2022
24-02-2022
25-02-2022
28-02-2022
01-03-2022
02-03-2022
03-03-2022
04-03-2022
07-03-2022
08-03-2022
09-03-2022
10-03-2022
11-03-2022
14-03-2022
15-03-2022
16-03-2022
17-03-2022
18-03-2022
21-03-2022
22-03-2022
23-03-2022
24-03-2022
25-03-2022
28-03-2022
29-03-2022
30-03-2022
31-03-2022
01-04-2022
04-04-2022
05-04-2022
06-04-2022
07-04-2022
08-04-2022
11-04-2022
12-04-2022
13-04-2022
14-04-2022
15-04-2022
18-04-2022
19-04-2022
20-04-2022
21-04-2022
22-04-2022
25-04-2022
26-04-2022
27-04-2022
28-04-2022
29-04-2022
02-05-2022
03-05-2022
04-05-2022
05-05-2022
06-05-2022
09-05-2022
10-05-2022
11-05-2022
12-05-2022
13-05-2022
16-05-2022
17-05-2022
18-05-2022
19-05-2022
20-05-2022
23-05-2022
24-05-2022
25-05-2022
26-05-2022
27-05-2022
30-05-2022
31-05-2022
01-06-2022
02-06-2022
03-06-2022
06-06-2022
07-06-2022
08-06-2022
09-06-2022
10-06-2022
13-06-2022
14-06-2022
15-06-2022
16-06-2022
17-06-2022
20-06-2022
21-06-2022
22-06-2022
23-06-2022
24-06-2022
27-06-2022
28-06-2022
29-06-2022
30-06-2022
01-07-2022
04-07-2022
05-07-2022
06-07-2022
07-07-2022
08-07-2022
11-07-2022
12-07-2022
13-07-2022
14-07-2022
15-07-2022
18-07-2022
19-07-2022
20-07-2022
21-07-2022
22-07-2022
25-07-2022
26-07-2022
27-07-2022
28-07-2022
29-07-2022
01-08-2022
02-08-2022
03-08-2022
04-08-2022
05-08-2022
08-08-2022
09-08-2022
10-08-2022
11-08-2022
12-08-2022
15-08-2022
16-08-2022
17-08-2022
18-08-2022
19-08-2022
22-08-2022
23-08-2022
24-08-2022
25-08-2022
26-08-2022
29-08-2022
30-08-2022
31-08-2022
01-09-2022
02-09-2022
05-09-2022
06-09-2022
07-09-2022
08-09-2022
09-09-2022
12-09-2022
13-09-2022
14-09-2022
15-09-2022
16-09-2022
19-09-2022
20-09-2022
21-09-2022
22-09-2022
23-09-2022
26-09-2022
27-09-2022
28-09-2022
29-09-2022
30-09-2022
03-10-2022
04-10-2022
05-10-2022
06-10-2022
07-10-2022
10-10-2022
11-10-2022
12-10-2022
13-10-2022
14-10-2022
17-10-2022
18-10-2022
19-10-2022
20-10-2022
21-10-2022
24-10-2022
25-10-2022
26-10-2022
27-10-2022
28-10-2022
31-10-2022
01-11-2022
02-11-2022
03-11-2022
04-11-2022
07-11-2022
08-11-2022
09-11-2022
10-11-2022
11-11-2022
14-11-2022
15-11-2022
16-11-2022
17-11-2022
18-11-2022
21-11-2022
22-11-2022
23-11-2022
24-11-2022
25-11-2022
28-11-2022
29-11-2022
30-11-2022
01-12-2022
02-12-2022
05-12-2022
06-12-2022
07-12-2022
08-12-2022
09-12-2022
12-12-2022
13-12-2022
14-12-2022
15-12-2022
16-12-2022
19-12-2022
20-12-2022
21-12-2022
22-12-2022
23-12-2022
26-12-2022
27-12-2022
28-12-2022
29-12-2022
30-12-2022
02-01-2023
03-01-2023
04-01-2023
05-01-2023
06-01-2023
09-01-2023
10-01-2023
11-01-2023
12-01-2023
13-01-2023
16-01-2023
17-01-2023
18-01-2023
19-01-2023
20-01-2023
23-01-2023
24-01-2023
25-01-2023
26-01-2023
27-01-2023
30-01-2023
31-01-2023
01-02-2023
02-02-2023
03-02-2023
06-02-2023
07-02-2023
08-02-2023
09-02-2023
10-02-2023
13-02-2023
14-02-2023
15-02-2023
16-02-2023
17-02-2023
20-02-2023
21-02-2023
22-02-2023
23-02-2023
24-02-2023
27-02-2023
28-02-2023
01-03-2023
02-03-2023
03-03-2023
06-03-2023
07-03-2023
08-03-2023
09-03-2023
10-03-2023
13-03-2023
14-03-2023
15-03-2023
16-03-2023
17-03-2023
20-03-2023
21-03-2023
22-03-2023
23-03-2023
24-03-2023
27-03-2023
28-03-2023
29-03-2023
30-03-2023
31-03-2023
03-04-2023
04-04-2023
05-04-2023
06-04-2023
07-04-2023
10-04-2023
11-04-2023
12-04-2023
13-04-2023
14-04-2023
17-04-2023
18-04-2023
19-04-2023
20-04-2023
21-04-2023
24-04-2023
25-04-2023
26-04-2023
27-04-2023
28-04-2023
01-05-2023
02-05-2023
03-05-2023
04-05-2023
05-05-2023
08-05-2023
09-05-2023
10-05-2023
11-05-2023
12-05-2023
15-05-2023
16-05-2023
17-05-2023
18-05-2023
19-05-2023
22-05-2023
23-05-2023
24-05-2023
25-05-2023
26-05-2023
29-05-2023
30-05-2023
31-05-2023
01-06-2023
02-06-2023
05-06-2023
06-06-2023
07-06-2023
08-06-2023
09-06-2023
12-06-2023
13-06-2023
14-06-2023
15-06-2023
16-06-2023
19-06-2023
20-06-2023
21-06-2023
22-06-2023
23-06-2023
26-06-2023
27-06-2023
28-06-2023
29-06-2023
30-06-2023
03-07-2023
04-07-2023
05-07-2023
06-07-2023
07-07-2023
10-07-2023
11-07-2023
12-07-2023
13-07-2023
14-07-2023
17-07-2023
18-07-2023
19-07-2023
20-07-2023
21-07-2023
24-07-2023
25-07-2023
26-07-2023
27-07-2023
28-07-2023
31-07-2023
01-08-2023
02-08-2023
03-08-2023
04-08-2023
07-08-2023
08-08-2023
09-08-2023
10-08-2023
11-08-2023
14-08-2023
15-08-2023
16-08-2023
17-08-2023
18-08-2023
21-08-2023
22-08-2023
23-08-2023
24-08-2023
25-08-2023
28-08-2023
29-08-2023
30-08-2023
31-08-2023
01-09-2023
04-09-2023
05-09-2023
06-09-2023
07-09-2023
08-09-2023
11-09-2023
12-09-2023
13-09-2023
14-09-2023
15-09-2023
18-09-2023
19-09-2023
20-09-2023
21-09-2023
22-09-2023
25-09-2023
26-09-2023
27-09-2023
28-09-2023
29-09-2023
02-10-2023
03-10-2023
04-10-2023
05-10-2023
06-10-2023
09-10-2023
10-10-2023
11-10-2023
12-10-2023
13-10-2023
16-10-2023
17-10-2023
18-10-2023
19-10-2023
20-10-2023
23-10-2023
24-10-2023
25-10-2023
26-10-2023
27-10-2023
30-10-2023
31-10-2023
01-11-2023
02-11-2023
03-11-2023
06-11-2023
07-11-2023
08-11-2023
09-11-2023
10-11-2023
13-11-2023
14-11-2023
15-11-2023
16-11-2023
17-11-2023
20-11-2023
21-11-2023
22-11-2023
23-11-2023
24-11-2023
27-11-2023
28-11-2023
29-11-2023
30-11-2023
01-12-2023
04-12-2023
05-12-2023
06-12-2023
07-12-2023
08-12-2023
11-12-2023
12-12-2023
13-12-2023
14-12-2023
15-12-2023
18-12-2023
19-12-2023
20-12-2023
21-12-2023
22-12-2023
25-12-2023
26-12-2023
27-12-2023
28-12-2023
29-12-2023
01-01-2024
02-01-2024
03-01-2024
04-01-2024
05-01-2024
08-01-2024
09-01-2024
10-01-2024
11-01-2024
12-01-2024
15-01-2024
16-01-2024
17-01-2024
18-01-2024
19-01-2024
22-01-2024
23-01-2024
24-01-2024
25-01-2024
26-01-2024
29-01-2024
30-01-2024
31-01-2024
01-02-2024
02-02-2024
05-02-2024
06-02-2024
07-02-2024
08-02-2024
09-02-2024
12-02-2024
13-02-2024
14-02-2024
15-02-2024
16-02-2024
19-02-2024
20-02-2024
21-02-2024
22-02-2024
23-02-2024
26-02-2024
27-02-2024
28-02-2024
29-02-2024
01-03-2024
04-03-2024
05-03-2024
06-03-2024
07-03-2024
08-03-2024
11-03-2024
12-03-2024
13-03-2024
14-03-2024
15-03-2024
18-03-2024
19-03-2024
20-03-2024
21-03-2024
22-03-2024
25-03-2024
26-03-2024
27-03-2024
28-03-2024
29-03-2024
01-04-2024
02-04-2024
03-04-2024
04-04-2024
05-04-2024
08-04-2024
09-04-2024
10-04-2024
11-04-2024
12-04-2024
15-04-2024
16-04-2024
17-04-2024
18-04-2024
19-04-2024
22-04-2024
23-04-2024
24-04-2024
25-04-2024
26-04-2024
29-04-2024
30-04-2024
01-05-2024
02-05-2024
03-05-2024
06-05-2024
07-05-2024
08-05-2024
09-05-2024
10-05-2024
13-05-2024
14-05-2024
15-05-2024
16-05-2024
17-05-2024
20-05-2024
21-05-2024
22-05-2024
23-05-2024
24-05-2024
27-05-2024
28-05-2024
29-05-2024
30-05-2024
31-05-2024
03-06-2024
04-06-2024
05-06-2024
06-06-2024
07-06-2024
10-06-2024
11-06-2024
12-06-2024
13-06-2024
14-06-2024
17-06-2024
18-06-2024
19-06-2024
20-06-2024
21-06-2024
24-06-2024
25-06-2024
26-06-2024
27-06-2024
28-06-2024
01-07-2024
02-07-2024
03-07-2024
04-07-2024
05-07-2024
08-07-2024
09-07-2024
10-07-2024
11-07-2024
12-07-2024
15-07-2024
16-07-2024
17-07-2024
18-07-2024
19-07-2024
22-07-2024
23-07-2024
24-07-2024
25-07-2024
26-07-2024
29-07-2024
30-07-2024
31-07-2024
01-08-2024
02-08-2024
05-08-2024
06-08-2024
07-08-2024
08-08-2024
09-08-2024
12-08-2024
13-08-2024
14-08-2024
15-08-2024
16-08-2024
19-08-2024
20-08-2024
21-08-2024
22-08-2024
23-08-2024
26-08-2024
27-08-2024
28-08-2024
29-08-2024
30-08-2024
02-09-2024
03-09-2024
04-09-2024
05-09-2024
06-09-2024
09-09-2024
10-09-2024
11-09-2024
12-09-2024
13-09-2024
16-09-2024
17-09-2024
18-09-2024
19-09-2024
20-09-2024
23-09-2024
24-09-2024
25-09-2024
26-09-2024
27-09-2024
30-09-2024
01-10-2024
02-10-2024
03-10-2024
04-10-2024
07-10-2024
08-10-2024
09-10-2024
10-10-2024
11-10-2024
14-10-2024
15-10-2024
16-10-2024
17-10-2024
18-10-2024
21-10-2024
22-10-2024
23-10-2024
24-10-2024
25-10-2024
28-10-2024
29-10-2024
30-10-2024
31-10-2024
01-11-2024
04-11-2024
05-11-2024
06-11-2024
07-11-2024
08-11-2024
11-11-2024
12-11-2024
13-11-2024
14-11-2024
15-11-2024
18-11-2024
19-11-2024
20-11-2024
21-11-2024
22-11-2024
25-11-2024
26-11-2024
27-11-2024
28-11-2024
29-11-2024
02-12-2024
03-12-2024
04-12-2024
05-12-2024
06-12-2024
09-12-2024
10-12-2024
11-12-2024
12-12-2024
13-12-2024
16-12-2024
17-12-2024
18-12-2024
19-12-2024
20-12-2024
23-12-2024
24-12-2024
25-12-2024
26-12-2024
27-12-2024
30-12-2024
31-12-2024
01-01-2025
02-01-2025
03-01-2025
06-01-2025
07-01-2025
08-01-2025
09-01-2025
10-01-2025
13-01-2025
14-01-2025
15-01-2025
16-01-2025
17-01-2025
20-01-2025
21-01-2025
22-01-2025
23-01-2025
24-01-2025
27-01-2025
28-01-2025
29-01-2025
30-01-2025
31-01-2025
03-02-2025
04-02-2025
05-02-2025
06-02-2025
07-02-2025
10-02-2025
11-02-2025
12-02-2025
13-02-2025
14-02-2025
17-02-2025
18-02-2025
19-02-2025
20-02-2025
21-02-2025
24-02-2025
25-02-2025
26-02-2025
27-02-2025
28-02-2025
03-03-2025
04-03-2025
05-03-2025
06-03-2025
07-03-2025
10-03-2025
11-03-2025
12-03-2025
13-03-2025
14-03-2025
17-03-2025
18-03-2025
19-03-2025
20-03-2025
21-03-2025
24-03-2025
25-03-2025
26-03-2025
27-03-2025
28-03-2025
31-03-2025
01-04-2025
02-04-2025
03-04-2025
04-04-2025
07-04-2025
08-04-2025
09-04-2025
10-04-2025
11-04-2025
14-04-2025
15-04-2025
16-04-2025
17-04-2025
18-04-2025
21-04-2025
22-04-2025
23-04-2025
24-04-2025
25-04-2025
28-04-2025
29-04-2025
30-04-2025
01-05-2025
02-05-2025
05-05-2025
06-05-2025
07-05-2025
08-05-2025
09-05-2025
12-05-2025
13-05-2025
14-05-2025
15-05-2025
16-05-2025
19-05-2025
20-05-2025
21-05-2025
22-05-2025
23-05-2025
26-05-2025
27-05-2025
28-05-2025
29-05-2025
30-05-2025
02-06-2025
03-06-2025
04-06-2025
05-06-2025
06-06-2025
09-06-2025
10-06-2025
11-06-2025
12-06-2025
13-06-2025
16-06-2025
17-06-2025
18-06-2025
19-06-2025
20-06-2025
23-06-2025
24-06-2025
25-06-2025
26-06-2025
27-06-2025
30-06-2025
01-07-2025
02-07-2025
03-07-2025
04-07-2025
07-07-2025
08-07-2025
09-07-2025
10-07-2025
11-07-2025
14-07-2025
15-07-2025
16-07-2025
17-07-2025
18-07-2025
21-07-2025
22-07-2025
23-07-2025
24-07-2025
25-07-2025
28-07-2025
29-07-2025
30-07-2025
31-07-2025
01-08-2025
04-08-2025
05-08-2025
06-08-2025
07-08-2025
08-08-2025
11-08-2025
12-08-2025
13-08-2025
14-08-2025
15-08-2025
18-08-2025
19-08-2025
20-08-2025
21-08-2025
22-08-2025
25-08-2025
26-08-2025
27-08-2025
28-08-2025
29-08-2025
01-09-2025
02-09-2025
03-09-2025
04-09-2025
05-09-2025
08-09-2025
09-09-2025
10-09-2025
11-09-2025
12-09-2025
15-09-2025
16-09-2025
17-09-2025
18-09-2025
19-09-2025
22-09-2025
23-09-2025
24-09-2025
25-09-2025
26-09-2025
29-09-2025
30-09-2025
01-10-2025
02-10-2025
03-10-2025
06-10-2025
07-10-2025
08-10-2025
09-10-2025
10-10-2025
13-10-2025
14-10-2025
15-10-2025
16-10-2025
17-10-2025
20-10-2025
21-10-2025
22-10-2025
23-10-2025
24-10-2025
27-10-2025
28-10-2025
29-10-2025
30-10-2025
31-10-2025
03-11-2025
04-11-2025
05-11-2025
06-11-2025
07-11-2025
10-11-2025
11-11-2025
12-11-2025
13-11-2025
14-11-2025
17-11-2025
18-11-2025
19-11-2025
20-11-2025
21-11-2025
24-11-2025
25-11-2025
26-11-2025
27-11-2025
28-11-2025
01-12-2025
02-12-2025
03-12-2025
04-12-2025
05-12-2025
08-12-2025
09-12-2025
10-12-2025
11-12-2025
12-12-2025
15-12-2025
16-12-2025
17-12-2025
18-12-2025
19-12-2025
22-12-2025
23-12-2025
24-12-2025
25-12-2025
26-12-2025
29-12-2025
30-12-2025
31-12-2025
01-01-2026
02-01-2026
05-01-2026
06-01-2026
07-01-2026
08-01-2026
09-01-2026
12-01-2026
13-01-2026
14-01-2026
15-01-2026
16-01-2026
19-01-2026
20-01-2026
21-01-2026
22-01-2026
23-01-2026
26-01-2026
27-01-2026
28-01-2026
29-01-2026
30-01-2026
02-02-2026
03-02-2026
04-02-2026
05-02-2026
06-02-2026
09-02-2026
10-02-2026
11-02-2026
12-02-2026
13-02-2026
16-02-2026
17-02-2026
18-02-2026
19-02-2026
20-02-2026
23-02-2026
24-02-2026
25-02-2026
26-02-2026
27-02-2026
02-03-2026
03-03-2026
04-03-2026
05-03-2026
06-03-2026
09-03-2026
10-03-2026
11-03-2026
12-03-2026
13-03-2026
16-03-2026
17-03-2026
18-03-2026
19-03-2026
20-03-2026
23-03-2026
24-03-2026
25-03-2026
26-03-2026
27-03-2026
30-03-2026
31-03-2026
01-04-2026
02-04-2026
03-04-2026
06-04-2026
07-04-2026
08-04-2026
09-04-2026
10-04-2026
13-04-2026
14-04-2026
15-04-2026
16-04-2026
17-04-2026
20-04-2026
21-04-2026
22-04-2026
23-04-2026
24-04-2026
27-04-2026
28-04-2026
29-04-2026
30-04-2026
01-05-2026
04-05-2026
05-05-2026
06-05-2026
07-05-2026
08-05-2026
11-05-2026
12-05-2026
13-05-2026
14-05-2026
15-05-2026
18-05-2026
19-05-2026
20-05-2026
21-05-2026
22-05-2026
25-05-2026
26-05-2026
27-05-2026
28-05-2026
29-05-2026
01-06-2026
02-06-2026
03-06-2026
04-06-2026
05-06-2026
08-06-2026
09-06-2026
10-06-2026
11-06-2026
12-06-2026
15-06-2026
16-06-2026
17-06-2026
18-06-2026
19-06-2026
22-06-2026
23-06-2026
24-06-2026
25-06-2026
26-06-2026
29-06-2026
30-06-2026
01-07-2026
02-07-2026
03-07-2026
06-07-2026
07-07-2026
08-07-2026
09-07-2026
10-07-2026
13-07-2026
14-07-2026
15-07-2026
16-07-2026
17-07-2026
20-07-2026
21-07-2026
22-07-2026
23-07-2026
24-07-2026
27-07-2026
28-07-2026
29-07-2026
30-07-2026
31-07-2026
03-08-2026
04-08-2026
05-08-2026
06-08-2026
07-08-2026
10-08-2026
11-08-2026
12-08-2026
13-08-2026
14-08-2026
17-08-2026
18-08-2026
19-08-2026
20-08-2026
21-08-2026
24-08-2026
25-08-2026
26-08-2026
27-08-2026
28-08-2026
31-08-2026
01-09-2026
02-09-2026
03-09-2026
04-09-2026
07-09-2026
08-09-2026
09-09-2026
10-09-2026
11-09-2026
14-09-2026
15-09-2026
16-09-2026
17-09-2026
18-09-2026
21-09-2026
22-09-2026
23-09-2026
24-09-2026
25-09-2026
28-09-2026
29-09-2026
30-09-2026
01-10-2026
02-10-2026
05-10-2026
06-10-2026
07-10-2026
08-10-2026
09-10-2026
12-10-2026
13-10-2026
14-10-2026
15-10-2026
16-10-2026
19-10-2026
20-10-2026
21-10-2026
22-10-2026
23-10-2026
26-10-2026
27-10-2026
28-10-2026
29-10-2026
30-10-2026
02-11-2026
03-11-2026
04-11-2026
05-11-2026
06-11-2026
09-11-2026
10-11-2026
11-11-2026
12-11-2026
13-11-2026
16-11-2026
17-11-2026
18-11-2026
19-11-2026
20-11-2026
23-11-2026
24-11-2026
25-11-2026
26-11-2026
27-11-2026
30-11-2026
01-12-2026
02-12-2026
03-12-2026
04-12-2026
07-12-2026
08-12-2026
09-12-2026
10-12-2026
11-12-2026
14-12-2026
15-12-2026
16-12-2026
17-12-2026
18-12-2026
21-12-2026
22-12-2026
23-12-2026
24-12-2026
25-12-2026
28-12-2026
29-12-2026
30-12-2026
31-12-2026
01-01-2027
04-01-2027
05-01-2027
06-01-2027
07-01-2027
08-01-2027
11-01-2027
12-01-2027
13-01-2027
14-01-2027
15-01-2027
18-01-2027
19-01-2027
20-01-2027
21-01-2027
22-01-2027
25-01-2027
26-01-2027
27-01-2027
28-01-2027
29-01-2027
01-02-2027
02-02-2027
03-02-2027
04-02-2027
05-02-2027
08-02-2027
09-02-2027
10-02-2027
11-02-2027
12-02-2027
15-02-2027
16-02-2027
17-02-2027
18-02-2027
19-02-2027
22-02-2027
23-02-2027
24-02-2027
25-02-2027
26-02-2027
01-03-2027
02-03-2027
03-03-2027
04-03-2027
05-03-2027
08-03-2027
09-03-2027
10-03-2027
11-03-2027
12-03-2027
15-03-2027
16-03-2027
17-03-2027
18-03-2027
19-03-2027
22-03-2027
23-03-2027
24-03-2027
25-03-2027
26-03-2027
29-03-2027
30-03-2027
31-03-2027
01-04-2027
02-04-2027
05-04-2027
06-04-2027
07-04-2027
08-04-2027
09-04-2027
12-04-2027
13-04-2027
14-04-2027
15-04-2027
16-04-2027
19-04-2027
20-04-2027
21-04-2027
22-04-2027
23-04-2027
26-04-2027
27-04-2027
28-04-2027
29-04-2027
30-04-2027
03-05-2027
04-05-2027
05-05-2027
06-05-2027
07-05-2027
10-05-2027
11-05-2027
12-05-2027
13-05-2027
14-05-2027
17-05-2027
18-05-2027
19-05-2027
20-05-2027
21-05-2027
24-05-2027
25-05-2027
26-05-2027
27-05-2027
28-05-2027
31-05-2027
01-06-2027
02-06-2027
03-06-2027
04-06-2027
07-06-2027
08-06-2027
09-06-2027
10-06-2027
11-06-2027
14-06-2027
15-06-2027
16-06-2027
17-06-2027
18-06-2027
21-06-2027
22-06-2027
23-06-2027
24-06-2027
25-06-2027
28-06-2027
29-06-2027
30-06-2027
01-07-2027
02-07-2027
05-07-2027
06-07-2027
07-07-2027
08-07-2027
09-07-2027
12-07-2027
13-07-2027
14-07-2027
15-07-2027
16-07-2027
19-07-2027
20-07-2027
21-07-2027
22-07-2027
23-07-2027
26-07-2027
27-07-2027
28-07-2027
29-07-2027
30-07-2027
02-08-2027
03-08-2027
04-08-2027
05-08-2027
06-08-2027
09-08-2027
10-08-2027
11-08-2027
12-08-2027
13-08-2027
16-08-2027
17-08-2027
18-08-2027
19-08-2027
20-08-2027
23-08-2027
24-08-2027
25-08-2027
26-08-2027
27-08-2027
30-08-2027
31-08-2027
01-09-2027
02-09-2027
03-09-2027
06-09-2027
07-09-2027
08-09-2027
09-09-2027
10-09-2027
13-09-2027
14-09-2027
15-09-2027
16-09-2027
17-09-2027
20-09-2027
21-09-2027
22-09-2027
23-09-2027
24-09-2027
27-09-2027
28-09-2027
29-09-2027
30-09-2027
01-10-2027
04-10-2027
05-10-2027
06-10-2027
07-10-2027
08-10-2027
11-10-2027
12-10-2027
13-10-2027
14-10-2027
15-10-2027
18-10-2027
19-10-2027
20-10-2027
21-10-2027
22-10-2027
25-10-2027
26-10-2027
27-10-2027
28-10-2027
29-10-2027
01-11-2027
02-11-2027
03-11-2027
04-11-2027
05-11-2027
08-11-2027
09-11-2027
10-11-2027
11-11-2027
12-11-2027
15-11-2027
16-11-2027
17-11-2027
18-11-2027
19-11-2027
22-11-2027
23-11-2027
24-11-2027
25-11-2027
26-11-2027
29-11-2027
30-11-2027
01-12-2027
02-12-2027
03-12-2027
06-12-2027
07-12-2027
08-12-2027
09-12-2027
10-12-2027
13-12-2027
14-12-2027
15-12-2027
16-12-2027
17-12-2027
20-12-2027
21-12-2027
22-12-2027
23-12-2027
24-12-2027
27-12-2027
28-12-2027
29-12-2027
30-12-2027
31-12-2027
03-01-2028
04-01-2028
05-01-2028
06-01-2028
07-01-2028
10-01-2028
11-01-2028
12-01-2028
13-01-2028
14-01-2028
17-01-2028
18-01-2028
19-01-2028
20-01-2028
21-01-2028
24-01-2028
25-01-2028
26-01-2028
27-01-2028
28-01-2028
31-01-2028
01-02-2028
02-02-2028
03-02-2028
04-02-2028
07-02-2028
08-02-2028
09-02-2028
10-02-2028
11-02-2028
14-02-2028
15-02-2028
16-02-2028
17-02-2028
18-02-2028
21-02-2028
22-02-2028
23-02-2028
24-02-2028
25-02-2028
28-02-2028
29-02-2028
01-03-2028
02-03-2028
03-03-2028
06-03-2028
07-03-2028
08-03-2028
09-03-2028
10-03-2028
13-03-2028
14-03-2028
15-03-2028
16-03-2028
17-03-2028
20-03-2028
21-03-2028
22-03-2028
23-03-2028
24-03-2028
27-03-2028
28-03-2028
29-03-2028
30-03-2028
31-03-2028
03-04-2028
04-04-2028
05-04-2028
06-04-2028
07-04-2028
10-04-2028
11-04-2028
12-04-2028
13-04-2028
14-04-2028
17-04-2028
18-04-2028
19-04-2028
20-04-2028
21-04-2028
24-04-2028
25-04-2028
26-04-2028
27-04-2028
28-04-2028
01-05-2028
02-05-2028
03-05-2028
04-05-2028
05-05-2028
08-05-2028
09-05-2028
10-05-2028
11-05-2028
12-05-2028
15-05-2028
16-05-2028
17-05-2028
18-05-2028
19-05-2028
22-05-2028
23-05-2028
24-05-2028
25-05-2028
26-05-2028
29-05-2028
30-05-2028
31-05-2028
01-06-2028
02-06-2028
05-06-2028
06-06-2028
07-06-2028
08-06-2028
09-06-2028
12-06-2028
13-06-2028
14-06-2028
15-06-2028
16-06-2028
19-06-2028
20-06-2028
21-06-2028
22-06-2028
23-06-2028
26-06-2028
27-06-2028
28-06-2028
29-06-2028
30-06-2028
03-07-2028
04-07-2028
05-07-2028
06-07-2028
07-07-2028
10-07-2028
11-07-2028
12-07-2028
13-07-2028
14-07-2028
17-07-2028
18-07-2028
19-07-2028
20-07-2028
21-07-2028
24-07-2028
25-07-2028
26-07-2028
27-07-2028
28-07-2028
31-07-2028
01-08-2028
02-08-2028
03-08-2028
04-08-2028
07-08-2028
08-08-2028
09-08-2028
10-08-2028
11-08-2028
14-08-2028
15-08-2028
16-08-2028
17-08-2028
18-08-2028
21-08-2028
22-08-2028
23-08-2028
24-08-2028
25-08-2028
28-08-2028
29-08-2028
30-08-2028
31-08-2028
01-09-2028
04-09-2028
05-09-2028
06-09-2028
07-09-2028
08-09-2028
11-09-2028
12-09-2028
13-09-2028
14-09-2028
15-09-2028
18-09-2028
19-09-2028
20-09-2028
21-09-2028
22-09-2028
25-09-2028
26-09-2028
27-09-2028
28-09-2028
29-09-2028
02-10-2028
03-10-2028
04-10-2028
05-10-2028
06-10-2028
09-10-2028
10-10-2028
11-10-2028
12-10-2028
13-10-2028
16-10-2028
17-10-2028
18-10-2028
19-10-2028
20-10-2028
23-10-2028
24-10-2028
25-10-2028
26-10-2028
27-10-2028
30-10-2028
31-10-2028
01-11-2028
02-11-2028
03-11-2028
06-11-2028
07-11-2028
08-11-2028
09-11-2028
10-11-2028
13-11-2028
14-11-2028
15-11-2028
16-11-2028
17-11-2028
20-11-2028
21-11-2028
22-11-2028
23-11-2028
24-11-2028
27-11-2028
28-11-2028
29-11-2028
30-11-2028
01-12-2028
04-12-2028
05-12-2028
06-12-2028
07-12-2028
08-12-2028
11-12-2028
12-12-2028
13-12-2028
14-12-2028
15-12-2028
18-12-2028
19-12-2028
20-12-2028
21-12-2028
22-12-2028
25-12-2028
26-12-2028
27-12-2028
28-12-2028
29-12-2028
01-01-2029
02-01-2029
03-01-2029
04-01-2029
05-01-2029
08-01-2029
09-01-2029
10-01-2029
11-01-2029
12-01-2029
15-01-2029
16-01-2029
17-01-2029
18-01-2029
19-01-2029
22-01-2029
23-01-2029
24-01-2029
25-01-2029
26-01-2029
29-01-2029
30-01-2029
31-01-2029
01-02-2029
02-02-2029
05-02-2029
06-02-2029
07-02-2029
08-02-2029
09-02-2029
12-02-2029
13-02-2029
14-02-2029
15-02-2029
16-02-2029
19-02-2029
20-02-2029
21-02-2029
22-02-2029
23-02-2029
26-02-2029
27-02-2029
28-02-2029
01-03-2029
02-03-2029
05-03-2029
06-03-2029
07-03-2029
08-03-2029
09-03-2029
12-03-2029
13-03-2029
14-03-2029
15-03-2029
16-03-2029
19-03-2029
20-03-2029
21-03-2029
22-03-2029
23-03-2029
26-03-2029
27-03-2029
28-03-2029
29-03-2029
30-03-2029
02-04-2029
03-04-2029
04-04-2029
05-04-2029
06-04-2029
09-04-2029
10-04-2029
11-04-2029
12-04-2029
13-04-2029
16-04-2029
17-04-2029
18-04-2029
19-04-2029
20-04-2029
23-04-2029
24-04-2029
25-04-2029
26-04-2029
27-04-2029
30-04-2029
01-05-2029
02-05-2029
03-05-2029
04-05-2029
07-05-2029
08-05-2029
09-05-2029
10-05-2029
11-05-2029
14-05-2029
15-05-2029
16-05-2029
17-05-2029
18-05-2029
21-05-2029
22-05-2029
23-05-2029
24-05-2029
25-05-2029
28-05-2029
29-05-2029
30-05-2029
31-05-2029
01-06-2029
04-06-2029
05-06-2029
06-06-2029
07-06-2029
08-06-2029
11-06-2029
12-06-2029
13-06-2029
14-06-2029
15-06-2029
18-06-2029
19-06-2029
20-06-2029
21-06-2029
22-06-2029
25-06-2029
26-06-2029
27-06-2029
28-06-2029
29-06-2029
02-07-2029
03-07-2029
04-07-2029
05-07-2029
06-07-2029
09-07-2029
10-07-2029
11-07-2029
12-07-2029
13-07-2029
16-07-2029
17-07-2029
18-07-2029
19-07-2029
20-07-2029
23-07-2029
24-07-2029
25-07-2029
26-07-2029
27-07-2029
30-07-2029
31-07-2029
01-08-2029
02-08-2029
03-08-2029
06-08-2029
07-08-2029
08-08-2029
09-08-2029
10-08-2029
13-08-2029
14-08-2029
15-08-2029
16-08-2029
17-08-2029
20-08-2029
21-08-2029
22-08-2029
23-08-2029
24-08-2029
27-08-2029
28-08-2029
29-08-2029
30-08-2029
31-08-2029
03-09-2029
04-09-2029
05-09-2029
06-09-2029
07-09-2029
10-09-2029
11-09-2029
12-09-2029
13-09-2029
14-09-2029
17-09-2029
18-09-2029
19-09-2029
20-09-2029
21-09-2029
24-09-2029
25-09-2029
26-09-2029
27-09-2029
28-09-2029
01-10-2029
02-10-2029
03-10-2029
04-10-2029
05-10-2029
08-10-2029
09-10-2029
10-10-2029
11-10-2029
12-10-2029
15-10-2029
16-10-2029
17-10-2029
18-10-2029
19-10-2029
22-10-2029
23-10-2029
24-10-2029
25-10-2029
26-10-2029
29-10-2029
30-10-2029
31-10-2029
01-11-2029
02-11-2029
05-11-2029
06-11-2029
07-11-2029
08-11-2029
09-11-2029
12-11-2029
13-11-2029
14-11-2029
15-11-2029
16-11-2029
19-11-2029
20-11-2029
21-11-2029
22-11-2029
23-11-2029
26-11-2029
27-11-2029
28-11-2029
29-11-2029
30-11-2029
03-12-2029
04-12-2029
05-12-2029
06-12-2029
07-12-2029
10-12-2029
11-12-2029
12-12-2029
13-12-2029
14-12-2029
17-12-2029
18-12-2029
19-12-2029
20-12-2029
21-12-2029
24-12-2029
25-12-2029
26-12-2029
27-12-2029
28-12-2029
31-12-2029
01-01-2030
02-01-2030
03-01-2030
04-01-2030
07-01-2030
08-01-2030
09-01-2030
10-01-2030
11-01-2030
14-01-2030
15-01-2030
16-01-2030
17-01-2030
18-01-2030
21-01-2030
22-01-2030
23-01-2030
24-01-2030
25-01-2030
28-01-2030
29-01-2030
30-01-2030
31-01-2030
01-02-2030
04-02-2030
05-02-2030
06-02-2030
07-02-2030
08-02-2030
11-02-2030
12-02-2030
13-02-2030
14-02-2030
15-02-2030
18-02-2030
19-02-2030
20-02-2030
21-02-2030
22-02-2030
25-02-2030
26-02-2030
27-02-2030
28-02-2030
01-03-2030
04-03-2030
05-03-2030
06-03-2030
07-03-2030
08-03-2030
11-03-2030
12-03-2030
13-03-2030
14-03-2030
15-03-2030
18-03-2030
19-03-2030
20-03-2030
21-03-2030
22-03-2030
25-03-2030
26-03-2030
27-03-2030
28-03-2030
29-03-2030
01-04-2030
02-04-2030
03-04-2030
04-04-2030
05-04-2030
08-04-2030
09-04-2030
10-04-2030
11-04-2030
12-04-2030
15-04-2030
16-04-2030
17-04-2030
18-04-2030
19-04-2030
22-04-2030
23-04-2030
24-04-2030
25-04-2030
26-04-2030
29-04-2030
30-04-2030
01-05-2030
02-05-2030
03-05-2030
06-05-2030
07-05-2030
08-05-2030
09-05-2030
10-05-2030
13-05-2030
14-05-2030
15-05-2030
16-05-2030
17-05-2030
20-05-2030
21-05-2030
22-05-2030
23-05-2030
24-05-2030
27-05-2030
28-05-2030
29-05-2030
30-05-2030
31-05-2030
03-06-2030
04-06-2030
05-06-2030
06-06-2030
07-06-2030
10-06-2030
11-06-2030
12-06-2030
13-06-2030
14-06-2030
17-06-2030
18-06-2030
19-06-2030
20-06-2030
21-06-2030
24-06-2030
25-06-2030
26-06-2030
27-06-2030
28-06-2030
01-07-2030
02-07-2030
03-07-2030
04-07-2030
05-07-2030
08-07-2030
09-07-2030
10-07-2030
11-07-2030
12-07-2030
15-07-2030
16-07-2030
17-07-2030
18-07-2030
19-07-2030
22-07-2030
23-07-2030
24-07-2030
25-07-2030
26-07-2030
29-07-2030
30-07-2030
31-07-2030
01-08-2030
02-08-2030
05-08-2030
06-08-2030
07-08-2030
08-08-2030
09-08-2030
12-08-2030"""
# print(r.split("\n"))
# share_add_list = ['CHOLAFIN',
#                      'CIPLA', 'COFORGE', 'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DABUR', 'DALBHARAT',
#                      'DEEPAKFERT', 'DEEPAKNTR', 'DELTACORP', 'DIVISLAB', 'DIXON', 'DLF', 'DRREDDY', 'ESCORTS',
#                      'EXIDEIND', 'GLENMARK', 'GLS', 'GNFC', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GUJGASLTD',
#                      'HAL', 'HAVELLS', 'HCLTECH', 'HDFCAMC', 'HDFCLIFE', 'HINDALCO', 'HINDCOPPER', 'ICICIGI',
#                      'ICICIPRULI', 'IEX', 'IGL', 'INDHOTEL', 'INDIACEM', 'INDIAMART', 'INDIGO', 'INDUSINDBK',
#                      'INDUSTOWER', 'INTELLECT', 'IPCALAB', 'JINDALSTEL', 'JKCEMENT', 'JSWSTEEL', 'JUBLFOOD',
#                      'KOTAKBANK', 'LALPATHLAB', 'LAURUSLABS', 'LICHSGFIN', 'LTIM', 'LTTS', 'LUPIN', 'M&MFIN',
#                      'MANAPPURAM', 'MARICO', 'MCDOWELL-N', 'MCX', 'METROPOLIS', 'MFSL', 'MGL', 'MPHASIS', 'MUTHOOTFIN',
#                      'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NMDC', 'NTPC', 'OBEROIRLTY', 'PEL', 'PERSISTENT', 'PETRONET',
#                      'PIDILITIND', 'POLYCAB', 'POWERGRID', 'RAIN', 'RAMCOCEM', 'RBLBANK', 'RECLTD', 'SBICARD',
#                      'SBILIFE', 'SIEMENS', 'SRF', 'STAR', 'SUNPHARMA', 'SYNGENE', 'TATACOMM', 'TATAMOTORS', 'TECHM',
#                      'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS',
#                      'ZEEL', 'ZYDUSLIFE']
#
# import webbrowser
# import openpyxl as xl
# wb = xl.load_workbook(r'E:\Daily Data work\hourlys 1 minute ALGO\2023\NOV\13.11.23\ABCAPITAL.xlsx')
# ws = wb['ABCAPITAL-Sheet1']
# t = ws.cell(392, 7).value
# print(t < datetime.time(15, 25, 00))
# print(type(t))

# if(10 >= 5 >= 5):
#     print("yes")

# i = 2000
# while (i <2024):
#     print(f'"{i}", ', end="")
#     i += 1
from zipfile import ZipFile
import pandas as pd
from date_variables import date, mnth, yr

# MD file
md_path_zipped = rf"E:\chrome downloads\fo{date[:2]}{mnth}20{date[6:]}bhav.csv.zip"     # .zip file path of downloaded cash bhavcpoy
md_path = rf"E:\chrome downloads"

# extracting .zip file
with ZipFile(md_path_zipped, 'r') as zObject:
    zObject.extractall(path=md_path)

md_file_path = rf"E:\Daily Data work\MD files\{yr}\{mnth}\fo{date[:2]}{mnth}20{date[6:]}bhav.xlsx"

df = pd.read_csv(md_path_zipped[:-4])
# df = df.iloc[:600]
df.to_excel(md_file_path, index=False)