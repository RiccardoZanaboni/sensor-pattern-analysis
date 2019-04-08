import pandas as pd
import matplotlib.pyplot as plt



str_nameas = ["hlt_4.csv", "hlt_7.csv", "hlt_9.csv", "hlt_11.csv", "hlt_19.csv"]


def delta_timestamp(df, f):
    global i
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])                   #Timestamp to Datetime

    df["Delta"] = df["Timestamp"].diff()                                # Caluclate delta between two consecutive timestamps
    df = df.dropna()                                                    # Clean dataset
    df["Delta"] = df["Delta"].apply(lambda x: x.total_seconds())        # Apply totalseconds(Datetima to totalseconds)


    df_statistics = df.describe(percentiles = [0.25, 0.50, 0.75, 0.85, 0.90, 0.98])

    #print(df_statistics)

    #Cleaning the data from outlayers inorder to calculate a better mean using only delta value< 3*mean

    outlayers_line = 3*df_statistics.loc['mean']['Delta']

    df = df[df['Delta'] < outlayers_line]
    df_statistics = df.describe(percentiles = [0.25, 0.50, 0.75, 0.85, 0.90, 0.98])
    df_statistics = df_statistics['Delta']
    #print(df_statistics)
    f.write(str_nameas[i] +"\n")
    i += 1
    df_statistics.to_csv(f)


if __name__=='__main__':
    i = 0
    df = (pd.read_csv(str_nameas[0]), pd.read_csv(str_nameas[1]), pd.read_csv(str_nameas[2]), pd.read_csv(str_nameas[3]),
          pd.read_csv(str_nameas[4]))

    f = open("hlt_statistics.csv", "w")
    f.close()
    f = open("hlt_statistics.csv", "a")

    for j in df:
        delta_timestamp(j, f)

    f.close()
