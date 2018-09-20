file= open(“testfile.txt”, “w”)#creates as an empty file
file.write('')
file = open(“testfile.txt”, “a”) 
for h in g_hps: #Uses the relationship above to estimate the number of cars in the frame.
    ncar = (h - b)/m;
    ncar = math.ceil(ncar);
    file.write('%d',ncar)
file.close()
