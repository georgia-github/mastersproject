import numpy as np
from pathlib import Path




totalsnrsforalldata = []

for i in range(623):
    file_name = Path('totalsnrsuncut{}.pkl.npy'.format(i))
    if file_name.exists():
        totalsnrsforalldata = np.concatenate((totalsnrsforalldata, np.load('totalsnrsuncut{}.pkl.npy'.format(i))),axis=0)


    

np.save("totalsnrsuncutforalldata.pkl", totalsnrsforalldata, allow_pickle=True)








# condor_rm -all   removes all in queue
#condor_q -analyze <job_id> when held it means error
   