
import os
from string import split

op = open("CountTransfers.txt","w")

eventInterval = ['288,288','200,200','168,168','86,86','56,56','43,43','28,29']
#eventInterval = ['576,576','400,400','336,336','168,168','112,112','86,86','56,58]
endTime = [86400,172800]
nrofCopies = [8]
rngSeed = [1,2,3,4,5,6]

count = 0

for mp in eventInterval:
  for e in endTime:
		for n in nrofCopies:
		        smal = 0
		        smsg = 0
		        sct = 0
		        stau = 0
		        for r in rngSeed:
		                count+=1
		                i = str(e)+ "_" + str(n)+ "_"  + str(r)
		                if not os.path.exists(i):
		                        os.makedirs(i)
		                ip = open("SnFOverhead"+ str(count) +".txt")
		                malcnt = 0
		                msgcnt = 0
		                contactcnt = 0
		                taucnt = 0
		                malnode = open(i+"/MalnodeInfoOverhead"+ i +".txt","w")
		                message = open(i+"/MessageInfoOverhead"+ i +".txt","w")
		                contact = open(i+"/ContactInfoOverhead"+ i +".txt","w")
		                tau = open(i+"/TauInfoOverhead"+ i +".txt","w")

		                old = 0

		                for eachline in ip:
		                        l1 = split(eachline)
		                        try:
		                                inc = int(l1[1]) - old
		                                if "MalNode Info Transfer between" in eachline:
		                                        malnode.write(eachline)
		                                        malcnt+=inc                                
		                                elif "Message Info Transfer between" in eachline:
		                                        message.write(eachline)
		                                        msgcnt+=1
		                                elif "Contact Info Transfer between" in eachline:
		                                        contact.write(eachline)
		                                        contactcnt+=inc
		                                elif "Tau Info Transfer" in eachline:
		                                        tau.write(eachline)
		                                        taucnt+=inc
		                                old = int(l1[1])
		                        except:
		                                pass
		                                
		                op.write("------------------------------------------------------------\n")
		                op.write("Transfer Details for Simulation with E:"+ str(e)+ "Load:" + str(mp) + " C:" + str(n) + " R:" + str(r) + "\n")
		                op.write("------------------------------------------------------------\n")
		                op.write("Malicious node info transfer = "+str(malcnt)+" bytes\n")
		                op.write("Message info transfer = "+str(msgcnt*6)+" bytes\n")
		                op.write("Contact info transfer = "+str(contactcnt)+" bytes\n")
		                op.write("Tau info transfer = "+str(taucnt)+" bytes\n")
		                op.write("Total info transfer = "+str(malcnt + (msgcnt*6) + contactcnt + taucnt)+" bytes\n")
		                op.write("------------------------------------------------------------\n\n")

		                smal+=malcnt
		                smsg+=msgcnt
		                sct+=contactcnt
		                stau+=taucnt
		        op.write("############################################################\n")
		        op.write("------------------------------------------------------------\n")
		        op.write("Average Transfer Details for Simulation with E:"+ str(e)+  "Load:" + str(mp) + " C:" + str(n) + "\n")
		        op.write("------------------------------------------------------------\n")
		        op.write("Malicious node info transfer = "+str(smal/6)+" bytes\n")
		        op.write("Message info transfer = "+str((smsg/6)*6)+" bytes\n")
		        op.write("Contact info transfer = "+str(sct/6)+" bytes\n")
		        op.write("Tau info transfer = "+str(stau/6)+" bytes\n")
		        op.write("Total info transfer = "+str((smal + (smsg*6) + sct + stau)/6)+" bytes\n")
		        op.write("------------------------------------------------------------\n")
		        op.write("############################################################\n")
