lines = open("summer.csv","r").readlines()
header = lines.pop(0)
demand = []
hours  = []
for cnt, line in enumerate(lines):
    
  if line.strip().split(",")[0].strip() == "23":
    # first line
    start_counter = cnt
  elif line.strip().split(",")[0].strip() == "00":
    # last line
    demand.append([float(lin.strip().split(",")[1]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
    hours.append ([int(lin.strip().split(",")[0]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )

for hist_cnt in range(len(demand)):
  f_obj = open("summer_"+str(hist_cnt)+".csv","w")
  f_obj.write(header.rstrip().strip()+"\n")
  for ts in reversed(range(len(hours[hist_cnt]))):
    f_obj.write(str(hours[hist_cnt][ts])+","+str(demand[hist_cnt][ts])+"\n")
  f_obj.close()







