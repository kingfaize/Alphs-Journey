#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Alphs Journey.

#A pograme detailing the generational upgraades of my first computer.

#Global variables
computerName = "My name is Alpha"
myExistence = "I am the first computer Lord Faisal ever assembled. I was his first love, you know:>"
invitationType = "I have evolved over the years and I wish to share my story. Enter the historical year below to learn more"



#li=[["john","doe"]]
#lists of parts ever in Alpha
cpu = ["Intel Pentium 1 166mhz","Intel Pentium 2 400mhz","Intel Pentium 3 933mhz","AMD Sempron 1.8 ghz","Intel Pentium 4 2.66ghz","Intel Pentium 4 3.0ghz", "Intel Pentium D 3.2ghz 2c4t","Intel core2quad q9300 2.5ghz 4c4t","Intel corei3 2400 2ndGen 3.1ghz 4c4t","Intel corei5 4570 4thGen 3.2ghz 4c4t","Intel corei5 10400F 10thGen 3.9ghz 6c12t"]
case = ["Dell Optiplex GXL","Dell Optiplex GX1 500L","Dell Dimension 4100","Unbranded Full Tower Case","Dell Optiplex 330","Aigo Gaming Case","Deepcool Matrrexx 55","Phanteks P400"]
cdrom = ["Tohiba 8X cdrom drive","LG 52x cdrom drive","LG External CDRW drive 52x","Samsung DVDRW drive"]
ram = ["32mb (8mb x2) sdram","128mb sdram","PC133 dimm 256mb"," DDR1 266 memory 512MB","DDR1 PC3200 400mhz 512mb x2","Hynix 2GB DDR2 RAM Memory 6400","Kingston PC3-10600U 1333Mhz DDR3 8GB 2x4GB","G.SKILL Ripjaws 16GB 4x8GB 2400MHz PC4 19200 DDR4"]
gpu = ["Onbaord S3 2mb","Onbaord Matrox 8mb ","ATI radeon 9200 128mb","ATI Radeon HD 4850 1gb","ATI Radeon HD 5850 1gb","MSI R9 390X GAMING 8G","GIGABYTE R9 390 G1 Gaming"]
hddpri = ["Maxtor 84320D4 4GB pata 3.5hdd (5400rpm)","Seagate 20 GB pata 3.5hdd (7200rpm)","SEAGATE ST39175LW 9GB 7.2K Ultra2 68-pin SCSI hard drive x 2","Samsung 40GB pata 3.5hdd (7200rpm)","Samsung 80GB pata 3.5hdd(7200rpm)","Seagate 160GB Sata 3.5hdd (7200rpm)","Seagate 500GB Sata 3.5hdd (7200rpm)","Samsung 120GB ssd","Kingston 256GB SSD"]
mobo = ["Dell Optiplex GXL Mobo","Dell OptiPlex GX1 Desktop Mobo 7803C","Dell dimention 4100 socket370 31REP","K8M800-M7A Micro ATX PGA754 AMD Mobo","Gigabyte PGA 478 GA-8I845G","ASUS P5E LGA775 Intel X38 DDR2-1200 ATX Mobo replaced with Gigabyte GA-EP31-DS3L P31-ES3G P31 LGA775 ATX mobo","Dell Optiplex 330 Mobo Intel LGA1155 CN-0KP561-70821-82c","MSI Intel H81M-E33 LGA1150 Mobo","ASRock Intel B460 PRO4 LGA1200 Mobo"]
psu = ["Dell 200w","Dell 260W","Dell 300W","Generic 400W","Corsair CX600W","EVGA 750W"]
hddsec = ["Seagate 20 GB pata 3.5hdd (7200rpm)","Seagate 160GB Sata 3.5hdd (7200rpm)","Seagate 500GB Sata 3.5hdd (7200rpm)","Hitachi 750GB sata 6GBs 7200rpm","WD 1TB sata 6GBs 7200rpm","WD 2TB sata 6GBs 7200rpm"]
cpucooler = ["Dell GXL stock cooler","Dell GX1 stock cooler","Dell dimension 4100 Stock cooler","Sempron stock cooler","Intel P4 478 stock cooler","Deepcool 775 tower air cooler","Intel 2nd gen 1155 stock cooler","Intel 4th gen 1150 stock cooler","Noctua NH-U12S air cooler"]
vdu = ["15 inch compaq crt","19 inch dell crt","19 inch Asus lcd","22 inch AOC lcd","27 inch HP lcd"]


print (myExistence)

print (computerName)

print (invitationType)

#print (li[0])



#prompt to enter age of PC
Year = 6

#function to determine changed parts
if Year==1:
    Year = "Its 2001; I am 1 year old and these are my specs"
    print(Year)
    print(cpu[0])
    print(cdrom[0])
    print(ram[0])
    print(gpu[0])
    print(hddpri[0])
    print(mobo[0])
    print(psu[0])
    print(hddsec[0])
    print(cpucooler[0])
    print(vdu[0])
    


if Year==2:
    Year = "Its 2002; I am 2 years old and these are my specs; Lord Faisal takes me along to sophomore year (3rd yr) in college"
    print(Year)
    print(cpu[1])
    print(cdrom[1])
    print(ram[1])
    print(gpu[1])
    print(hddpri[0])
    print(mobo[1])
    print(psu[1])
    print(cpucooler[1])
    print(vdu[0])
    
    
if Year==3:
    Year = "Its 2003; I am 3 years old and these are my specs; Lord Faisal is using me to pirate songs for friends for cash"
    print(Year)
    print(cpu[1])
    print(cdrom[1])
    print(ram[1])
    print(gpu[1])
    print(hddpri[0])
    print(mobo[1])
    print(psu[1])
    print(cpucooler[1])
    print(vdu[0])
    
if Year==4:
    Year = "Its 2004; I am 4 years old and these are my specs; Load Faisal is in final year and we are still pirating songs for cash"
    print(Year)
    print(cpu[1])
    print(cdrom[1])
    print(ram[1])
    print(gpu[1])
    print(hddpri[0])
    print(mobo[1])
    print(psu[1])
    print(cpucooler[1])
    print(vdu[0])
    
if Year==5:
    Year = "Its 2005; I am 5 years old and these are my specs; we have graduated from college but still pirating songs for cash"
    print(Year)
    print(cpu[2])
    print(cdrom[1])
    print(ram[2])
    print(gpu[2])
    print(hddpri[1])
    print(mobo[2])
    print(psu[2])
    print(cpucooler[2])
    print(vdu[1])
    
if Year==6:
    Year = "Its 2006; I am 6 years old and these are my specs; Lord Faisal Just started work as a PC technician"
    print(Year)
    print(cpu[2])
    print(cdrom[1])
    print(ram[2])
    print(gpu[2])
    print(hddpri[2])
    print(hddsec[0])
    print(mobo[2])
    print(psu[2])
    print(cpucooler[2])
    print(vdu[1])


