import os
import platform


print("pid is:", os.getpid())

platfrom_name = platform.platform()
platfrom_name =platfrom_name.lower()
load_one_min, load_five_min,load_15_min = os.getloadavg()

if platfrom_name.find("linux")!=-1:
   print("----------------Load average------------")
   print("load average over the last 1 min:",load_one_min)
   print("load average over the last 5 min:", load_five_min)
   print("load average over the 15 min:", load_15_min)
   print("---------------------------------")

cpu_count = os.cpu_count()
print("Number of cpus in the system is:", cpu_count)
print("load average over the last 5 min:",load_five_min)

if(cpu_count-load_five_min<0):
    print("exit the script")

