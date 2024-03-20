import numpy as np
import matplotlib.pyplot as plt

def line_to_numpy_array(line):
    # Split the line by comma and strip spaces, then filter out any non-numeric entries
    numbers = [int(x.strip()) for x in line.split(',') if x.strip().isdigit()]
    return np.array(numbers)

# Function to read the file and convert it into a numpy array of arrays
def file_to_numpy_array_of_arrays(file_path):
    data_arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            # Check if line contains any digits, to skip empty or non-data lines
            if any(char.isdigit() for char in line):
                numpy_array = line_to_numpy_array(line)
                data_arrays.append(numpy_array)
    return np.array(data_arrays)

NAMES              = np.array([  "barnes",      "fmm",     "ocean",     "radiosity", "water-nsquared", "water-spatial", "cholensky",   "fft", "lu-contiguous", "lu-noncontiguous",    "radix"])
OP                 = np.array([2256183036, 2617387016,  1914731924,       1467839265,       649443669,       509394345,    42784491, 35575606,      456666762,         1041412811,  525383136])
OP_1core           = np.array([4245448866, 4922027934,  3261296443,       2761885217,      1239770455,      1010924777,    72829595, 68657862,      905268966,         1909958961, 1013300452])
name_perf_counter_culsans = np.array(["#cycles", "#instrs", "#l1icachemiss", "#l1ddcachemiss", "#loads"    , "#stores" , "#ifempty"   ,"#stall" ,
                                      "#in_read_once", "#in_read_shared", "#in_read_clean"      , "#in_read_no_shared" , "#in_read_unique"   , "#in_clean_shared"  , "#in_clean_invalid" ,   "#in_clean_unique"  , "#in_make_invalid"   ,
                                      "#out_read_once", "#out_read_shared", "#out_read_unique"      , "#out_read_no_snoop" , "#out_clean_unique"   , "#out_wr_unique"  , "#out_wr_nosnoop" ,   "#out_writeback"    ])

# Specify the path to your text file
file_path = 'culsans.rpt'

# Convert the file to a numpy array of arrays
data = file_to_numpy_array_of_arrays(file_path)
perf_counters = np.reshape(data, (len(NAMES),len(name_perf_counter_culsans)))

single_core = 0

if(single_core):
    OP = OP_1core

culsans = perf_counters[:,1] / perf_counters[:,0]
OP = perf_counters[:,1] / OP
delta = (culsans - OP) *100/OP
indices = np.argsort(delta)
instructions = perf_counters[:,1]

sorted_names = NAMES[indices]
sorted_instructions = instructions[indices]
sorted_OP           = OP[indices]
sorted_culsans      = culsans[indices]
sorted_deltas       = delta[indices]
tmp = perf_counters.astype(float)
tmp1 = tmp
tmp2 = tmp1[indices]
sorted_perf_counters = perf_counters[indices]
percyc_perf_counters = tmp[indices]

for i in range(len(name_perf_counter_culsans)):
    percyc_perf_counters[:,i] = percyc_perf_counters[:,i]/tmp2[:,1]

barWidth = 0.25
b1 = np.arange(len(NAMES))
b2 = [x+ barWidth for x in b1]

fig = plt.figure()
ax0 = plt.subplot(3,1,1)
ax1 = plt.subplot(3,1,2)
ax2 = plt.subplot(3,1,3)

bar1 = ax0.bar(b1, sorted_OP, color = 'red', width = barWidth, ec="k", label='OpenPiton 16kB L1 Icache, 8kB L1WT Dcache, 8kB L1.5, 2x64kB L2, 4-ways')
bar2 = ax0.bar(b2, sorted_culsans, color = 'yellow', width = barWidth, ec="k", label='Culsans, 16kB L1 Icache, 16kB L1 WB Dcache, 128kB LLC, 4-ways')

i = 0
for rect in bar1:
    height = max(sorted_culsans[i],sorted_OP[i])
    x1 = sorted_deltas[i]
    ax0.text(rect.get_x() + rect.get_width() * 1.5 , height, '$\Delta$ =%.2f%%'%(x1), ha='center', va='bottom', fontsize=12,rotation=0)
    i = i+1

ax0.set_xticks([r + barWidth for r in range(len(NAMES))],sorted_names,fontsize=15,rotation= 0)
ax0.set_ylabel('Instructions per clock cycle\n (higher is better)', fontsize=15)
ax0.set_yticks(np.linspace(0,0.7,8))
ax0.tick_params(axis='y',which='major',labelsize=10)
ax0.legend(fontsize=12, loc='upper left')

barWidth = 0.2
b1 = np.arange(len(NAMES))
b2 = [x+ barWidth for x in b1]
b3 = [x+ barWidth for x in b2]
b4 = [x+ barWidth for x in b3]
b5 = [x+ barWidth for x in b4]
b6 = [x+ barWidth for x in b5]
b7 = [x+ barWidth for x in b6]

bar2 = ax1.bar(b1,np.squeeze(percyc_perf_counters[:,2].reshape(1,-1)), color = 'blue', width = barWidth, ec="k", label=name_perf_counter_culsans[2])
bar3 = ax1.bar(b1,np.squeeze(percyc_perf_counters[:,3].reshape(1,-1)), bottom=np.squeeze(percyc_perf_counters[:,2].reshape(1,-1)), color = 'yellow', width = barWidth, ec="k", label=name_perf_counter_culsans[3])
bar3 = ax1.bar(b2,np.squeeze(percyc_perf_counters[:,4].reshape(1,-1)), color = 'pink', width = barWidth, ec="k", label=name_perf_counter_culsans[4])
bar3 = ax1.bar(b2,np.squeeze(percyc_perf_counters[:,5].reshape(1,-1)), bottom=np.squeeze(percyc_perf_counters[:,4].reshape(1,-1)), color = 'grey', width = barWidth, ec="k", label=name_perf_counter_culsans[5])
bar4 = ax1.bar(b3,np.squeeze(percyc_perf_counters[:,6].reshape(1,-1)), color = 'green', width = barWidth, ec="k", label=name_perf_counter_culsans[6])

ax1.set_xticks([r + barWidth for r in range(len(NAMES))],sorted_names,fontsize=15,rotation= 0)
ax1.set_ylabel('Culsans \nEvents per instruction', fontsize=15)
ax1.legend(fontsize=12, loc='upper left',ncols=3)

barWidth = 0.1
b1 = np.arange(len(NAMES))
b2 = [x+ barWidth for x in b1]
b3 = [x+ barWidth for x in b2]
b4 = [x+ barWidth for x in b3]
b5 = [x+ barWidth for x in b4]
b6 = [x+ barWidth for x in b5]
b7 = [x+ barWidth for x in b6]
b8 = [x+ barWidth for x in b7]
b9 = [x+ barWidth for x in b8]
b10= [x+ barWidth for x in b9]

ax2.bar(b1,np.squeeze(percyc_perf_counters[:,8].reshape(1,-1)), color = 'red', width = barWidth, ec="k", label=name_perf_counter_culsans[8])
ax2.bar(b2,np.squeeze(percyc_perf_counters[:,9].reshape(1,-1)), color = 'blue', width = barWidth, ec="k", label=name_perf_counter_culsans[9])
ax2.bar(b3,np.squeeze(percyc_perf_counters[:,12].reshape(1,-1)), color = 'yellow', width = barWidth, ec="k", label=name_perf_counter_culsans[12])
ax2.bar(b4,np.squeeze(percyc_perf_counters[:,19].reshape(1,-1)), color = 'orange', width = barWidth, ec="k", hatch='//', label=name_perf_counter_culsans[19])
ax2.bar(b5,np.squeeze(percyc_perf_counters[:,24].reshape(1,-1)), color = 'brown', width = barWidth, ec="k", hatch='//', label=name_perf_counter_culsans[24])
ax2.bar(b6,np.squeeze(percyc_perf_counters[:,18].reshape(1,-1)), color = 'pink', width = barWidth, ec="k", hatch='//', label=name_perf_counter_culsans[18])
ax2.bar(b7,np.squeeze(percyc_perf_counters[:,3].reshape(1,-1)), color = 'grey', width = barWidth, ec="k", hatch='*', label=name_perf_counter_culsans[3])
ax2.bar(b8,np.squeeze(percyc_perf_counters[:,2].reshape(1,-1)), color = 'lightblue', width = barWidth, ec="k", hatch='*', label=name_perf_counter_culsans[2])

if(single_core):
    ax2.text(b1[1]-0.09, 0.1, 'in_read_clean, in_read_no_shared\nin_clean_shared, in_clean_invalid,\nin_clean_unique, out_write_nosnoop,\nout_write_unique, out_read_no_snoop\nout_clean_unique all = 0', ha='left', va='top', fontsize=12,rotation=0)
else:
    ax2.text(b1[5]-0.09, 0.1, 'in_read_clean, in_read_no_shared\nin_clean_shared, in_clean_invalid,\nin_clean_unique, out_write_nosnoop,\nout_write_unique, out_read_no_snoop\nout_clean_unique all = 0', ha='left', va='top', fontsize=12,rotation=0)

ax2.set_xticks([r + barWidth for r in range(len(NAMES))],sorted_names,fontsize=15,rotation= 0)
ax2.set_ylabel('Culsans \n ACE snoop trx \n per instruction', fontsize=15)
ax2.legend(fontsize=15, loc='upper right',ncols=2)

plt.subplots_adjust(top=0.917,
bottom=0.046,
left=0.076,
right=0.992,
hspace=0.176,
wspace=0.2)

plt.suptitle("Splash-3 results, %d threads \n Genesys 2 40MHz with DDR3 at 250MHz \n L1 cache line 8B, L2/LLC cache line 64B" %(single_core), fontsize=15)
plt.show()
