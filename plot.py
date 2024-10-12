import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

cache_size_new = "4B,8B,16B,32B,64B,128B,256B,512B,1K,2K,4K,8K,16K,32K,64K,128K,256K,512K,1M,2M,4M,8M,16M,32M,64M,128M".split(",")
data_new =  {
'4K': [2.3, 2.8, 2.8, 2.8, 2.4, 2.0, 1.1, 0.8, 0.3, 0.3],
'8K': [2.7, 2.8, 2.8, 2.8, 2.9, 2.4, 2.1, 1.0, 0.8, 0.3, 0.3],
'16K': [2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.4, 2.0, 1.0, 0.8, 0.3, 0.3],
'32K': [2.8, 2.8, 2.8, 2.9, 3.0, 2.9, 2.9, 2.5, 2.1, 1.0, 0.8, 0.3, 0.3],
'64K': [2.7, 2.8, 2.8, 2.8, 5.0, 5.0, 5.0, 5.1, 4.4, 4.3, 2.3, 0.8, 0.3, 0.3],
'128K': [2.8, 2.8, 2.8, 2.8, 5.0, 5.4, 5.6, 5.6, 5.8, 5.7, 4.7, 2.3, 0.8, 0.3, 0.3],
'256K': [2.8, 2.8, 2.9, 2.9, 5.4, 5.9, 7.4, 7.5, 8.0,12.7,10.5, 4.5, 2.3, 0.8, 0.3, 0.3],
'512K': [2.8, 2.9, 2.8, 2.9, 5.5, 6.7,11.8,13.1,15.0,18.8,20.6,12.6, 6.0, 4.4, 1.7, 0.3, 0.3],
'1M': [2.8, 2.8, 2.9, 2.9, 5.7, 6.9,12.1,13.2,15.6,18.6,20.6,19.7,13.6, 6.0, 4.3, 1.7, 0.3, 0.3],
'2M': [2.8, 2.8, 2.8, 3.0, 5.7,10.6,15.6,16.1,18.4,22.1,24.2,20.6,19.3,12.9, 6.3, 4.6, 1.6, 0.3, 0.3],
'4M': [2.8, 2.8, 2.9, 4.2, 6.5,18.5,31.4,30.2,33.6,41.1,58.9,24.3,20.6,19.8,12.6, 9.6, 4.3, 1.7, 0.3, 0.3],
'8M': [2.8, 2.8, 3.0, 4.4, 6.8,20.4,41.1,41.1,49.7,61.1,76.9,55.4,24.8,24.3,19.5,13.2, 7.1, 4.2, 1.6, 0.3, 0.3],
'16M': [2.8, 2.8, 3.0, 4.3, 7.0,21.3,44.2,42.6,49.7,66.2,79.5,74.5,54.2,25.9,20.2,19.5,13.4, 6.2, 4.4, 1.7, 0.3, 0.3],
'32M': [2.8, 2.8, 3.1, 4.4, 6.9,22.1,42.6,39.7,49.7,66.2,74.5,74.5,66.2,54.2,37.3,24.8,18.6,12.7, 6.7, 4.3, 1.7, 0.3, 0.3],
'64M': [2.8, 2.8, 3.0, 4.3, 6.8,19.9,42.6,42.6,49.7,47.7,74.5,74.5,74.5,74.5,59.6,33.1,19.9,18.6,14.2, 6.6, 4.3, 1.7, 0.3, 0.3],
'128M': [2.7, 2.8, 3.0, 3.2, 7.0,14.9,29.8,29.8,49.7,69.5,74.5,59.6,74.5,59.6,74.5,39.7,29.8,21.3,18.6,12.4, 7.0, 4.3, 1.7, 0.3, 0.3],
'256M': [2.8, 2.8, 3.0, 3.2, 6.6,14.9,44.7,29.8,37.3,67.1,74.5,59.6,74.5,74.5,59.6,89.4,44.7,24.8,14.9,18.6, 9.9, 6.6, 4.6, 1.6, 0.3, 0.3]}


# values = [label(2**i) for i in range(len(data['256M']))]


fig = plt.figure(figsize=(15,10))
x_bound = np.arange(len(data_new['256M']))
legend = [key for key, val in data_new.items()]

for i, (key, val) in enumerate(data_new.items()):
    x = np.arange(len(val))
    plt.plot(x, val, label = legend[i], marker='o')


plt.yticks(np.arange(0, 100, 10))
plt.legend(loc="upper right")
plt.xlabel('Stride')
plt.ylabel('Access Time(ns)')
plt.xticks(x_bound, cache_size_new, rotation=40)
plt.title('Access Time vs Strides for different cache sizes')
plt.show()
fig.savefig('cache_new.png')


fig_log = plt.figure(figsize=(15,10))

for i, (key, val) in enumerate(data_new.items()):
    x = np.arange(len(val))
    plt.plot(x, np.log(val), label = legend[i], marker='o')


plt.yticks(np.arange(0, 10, 1))
plt.legend(loc="upper right")
plt.xlabel('Stride')
plt.ylabel('Access Time(ns)')
plt.title('Log(Access Time) vs Strides for different cache sizes')
plt.xticks(x_bound, cache_size_new, rotation=40)   
plt.show()
fig_log.savefig('cache_new_log.png')