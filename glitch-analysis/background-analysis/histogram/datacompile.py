import numpy as np
from pathlib import Path



name5 = 'totalfreqscut' + inputarg + ".pkl"
np.save(name5,cut_total_frequencies,allow_pickle=True)
name6 = 'totalsnrscut' + inputarg + ".pkl"
np.save(name6,cut_total_snrs,allow_pickle=True)


totalsnrsforalldata = []

for i in range():
    file_name = Path('totalsnrscut{}.pkl.npy'.format(i))
    if file_name.exists():
        totalsnrsforalldata = np.concatenate((totalsnrsforalldata, np.load('totalsnrscut{}.pkl.npy'.format(i))),axis=0)


    

np.save("totalsnrsforalldata.pkl", totalsnrsforalldata, allow_pickle=True)








# condor_rm -all   removes all in queue
#condor_q -analyze <job_id> when held it means error
   