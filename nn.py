import csv                                           
                                                     
                                                     
with open('flight_rasp_data.csv', newline='') as csvf
    reader = csv.DictReader(csvfile)                 
    flights = []                                     
    x =[]                                            
    for row in reader:                               
        flights.append(row['departure_terminal'])    
    def fl():                                        
        global flights                               
        flb = []                                     
        flc =[]                                      
        for i in flights:                            
            if i == 'B':                             
                flb.append(i)                        
            else:                                    
                flc.append(i)                        
        return len(flb), len(flc)                    
                                                     
