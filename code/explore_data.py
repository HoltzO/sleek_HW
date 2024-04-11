

import numpy as np
import pandas as pd
import os


path = os.getcwd()
Friday_DDOS = pd.read_csv(path+"\\data\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv", sep=",", encoding='utf-8')
Friday_PCAP = pd.read_csv(path+"\\data\\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv", sep=",", encoding='utf-8')
Friday_Morning = pd.read_csv(path+"\\data\\Friday-WorkingHours-Morning.pcap_ISCX.csv", sep=",", encoding='utf-8')
Monday_PCAP = pd.read_csv(path+"\\data\\Monday-WorkingHours.pcap_ISCX.csv", sep=",", encoding='utf-8')
Thu_PCAP_Afternoon = pd.read_csv(path+"\\data\\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv", sep=",", encoding='utf-8')
Thu_PCAP_Morning = pd.read_csv(path+"\\data\\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", sep=",", encoding='utf-8')
TUE_PCAP = pd.read_csv(path+"\\data\\Tuesday-WorkingHours.pcap_ISCX.csv", sep=",", encoding='utf-8')
WED_PCAP = pd.read_csv(path+"\\data\\Wednesday-workingHours.pcap_ISCX.csv", sep=",", encoding='utf-8')


