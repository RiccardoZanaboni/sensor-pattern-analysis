# analysing the delta between every sample of MS sensors
import pandas as pd
import datetime
import matplotlib.pyplot as plt

'''global fig, axs
fig, axs = plt.subplots(2, 3, sharey=True, tight_layout=True)
global N_BINS
N_BINS = 20
global index
index = 0'''

def get_stat(path, name, f):
    file_name = path+name
    df = pd.read_csv(file_name, ",")

    drop_list = check_couple(df)        # identify unmatched measures
    print(len(drop_list))
    df = clean_df(df, drop_list)        # clean df from unmatched measures

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])       # select the most accurate period after the summit
    df = df[df['Timestamp'] >= datetime.datetime.strptime("2019-03-28 09:53:40", "%Y-%m-%d %H:%M:%S")]
    df["Delta"] = df["Timestamp"].diff()                    # compute delta
    df["Diff_Value"] = df["Value"].diff()                   # compute diff between values in order to select corret couple
    df1 = df[df['Diff_Value'] == -1]                         # -1 = [isMoving -> notMoving ]
    df2 = df[df['Diff_Value'] == 1]   # 1 = [notMoving -> isMoving ]

    def write_stat(df,header):
        nonlocal name
        df = df.dropna()  # Clean dataset
        df = df["Delta"].apply(lambda x: x.total_seconds())  # Apply totalseconds(Datetime to totalseconds)
        print(df.shape)
        df = df[df < 210]

        plt.hist(df, bins=20)
        plt.ylabel(name)
        plt.show()
        '''global index
        global fig, axs
        axs[1,1].hist(df, bins=N_BINS)
        index += 1'''

        df_statistics = df.describe(percentiles=[0.10, 0.20, 0.40, 0.50, 0.60, 0.80, 0.95])
        f.write(name+"\n"+header+"\n")
        df_statistics.to_csv(f)


    write_stat(df1,'[isMoving -> notMoving ]')
    #write_stat(df2,'[notMoving -> isMoving ]')


def clean_df(df, drop_list):
    return df.drop(drop_list)


def check_couple(df):
    df_check = df['Value']
    i_max = len(df_check)-1
    drop_list = []
    for j in range(0,i_max):
        if df_check.loc[j] == df_check.loc[j+1]:
            if df_check.loc[j] == 1:
                drop_list.append(j)
            else:
                drop_list.append(j+1)
    return drop_list


if __name__ == "__main__":
    path = "/home/orso_matteo/Documents/Tesi/sensor-pattern-analysis/data2/MovementState/"
    file_name = ["livingroom.csv", "bedroom.csv", "kitchen.csv", "toilet.csv", "atrium.csv"]

    f = open(path+"MS_time_samples_stat.csv","w")
    f.close()
    f = open(path+"MS_time_samples_stat.csv", "a")
    for name in file_name:
        get_stat(path, name, f)
    f.close()

