import pandas as pd

def binary_conversion(df):
    for i in range(0, df.shape[0]):
        if df.iat[i, 1] != 0:
            df.iat[i, 1] = 1
    return df


if __name__ == '__main__':
    df = pd.read_csv( "fsm_hlt_9_beta.csv", ",")
    df = binary_conversion(df)
    df.to_csv("fsm_hlt_9_binary_out.csv",index=False)
