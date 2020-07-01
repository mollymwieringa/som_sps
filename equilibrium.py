def find_equilibrium(volume):
        annualmean = volume.reshape(12,volume.size//12,order='F').mean(axis=0)
        annualmax = volume.reshape(12,volume.size//12,order='F').max(axis=0)
        
        eq = (annualmean[1:]/annualmean[0:-1]-1)*100
        percent = (annualmean[1:]-annualmean[0:-1])/annualmax[1:]*100

        temp = []
        for i in range(2, len(percent)-2):
             if (abs(percent[i])+abs(percent[i+1])+abs(percent[i+2])+abs(percent[i-1])+abs(percent[i-2]))/5 < 0.01:
                    temp.append(i)
        ind = temp[0]
        
        return eq, percent, ind