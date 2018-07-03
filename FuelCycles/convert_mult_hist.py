def multipleHistories(filename, season):
    lines = open(filename,"r").readlines()
    header = lines.pop(0)
    demand = []
    hours  = []
    for cnt, line in enumerate(lines):

        if line.strip().split(",")[0].strip() == "0":
            # first line
            start_counter = cnt
        elif line.strip().split(",")[0].strip() == "23":
            # last line
            demand.append([float(lin.strip().split(",")[1]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
            hours.append([int(lin.strip().split(",")[0]) for lin in lines[start_counter:cnt+1] if len(lin.strip()) > 0] )
            print("here")

    for hist_cnt in range(len(demand)):
      f_obj = open(season+"/"+season+str(hist_cnt)+".csv","w")
      f_obj.write(header.rstrip().strip()+"\n")
      for ts in reversed(range(len(hours[hist_cnt]))):
        f_obj.write(str(hours[hist_cnt][ts])+","+str(demand[hist_cnt][ts])+"\n")
      f_obj.close()

    InputFile=open(season+"/raw_data_"+season+".csv","w")
    InputFile.write("scaling,filename"+"\n")
    for hist_cnt in range(len(demand)):
        InputFile.write("1"+","+season+"_"+str(hist_cnt)+".csv"+"\n")
    InputFile.close()



Spring=multipleHistories("spring/SpringDemand.csv", "spring")
Summer=multipleHistories("summer/SummerDemand.csv", "summer")
Fall=multipleHistories("fall/FallDemand.csv", "fall")
Winter=multipleHistories("winter/Winterdemand.csv", "winter")
