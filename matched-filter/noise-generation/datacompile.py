import numpy as np
from pathlib import Path
#totalnoisedata.append(np.load('maximumnoisesnr{}.pkl.npy'.format(i),allow_pickle=True))


totalnoisedata = []

for i in range(1,1000):
    file_name = Path('maximumnoisesnr{}.pkl.npy'.format(i))
    if file_name.exists():
        totalnoisedata = np.concatenate((totalnoisedata,np.load('maximumnoisesnr{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)


totalnoisesorted = np.sort(totalnoisedata)
print(np.array(totalnoisedata))
print(len(totalnoisedata))



np.save("compliednoisedatasnr.pkl", totalnoisesorted, allow_pickle=True)


# condor_rm -all   removes all in queue
#condor_q -analyze <job_id> when held it means error
#chmod a+x matchedfiltersignals.py
#chmod a+x matchedfilternoise.py


   