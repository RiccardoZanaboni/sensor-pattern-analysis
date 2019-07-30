import pandas as pd


def read_sequence_MS(file_name):
    df = pd.read_csv(file_name, ",")
    df = df[(df['Value'] != 0) | (df['Class'] == 'Atrium')]
    df.to_csv("out.csv", index=False)
    return df


def compute_transictions(df):
    atrium = "Atrium"
    global atrium_state
    global transictions

    def check_if_atrium_out(index):
        room = df.iloc[index, 0]
        state =df.iloc[index, 1]

        global atrium_state
        if room == atrium and state == 0:
            atrium_state = state
            return True

        return False

    def check_if_atrium(index):
        room = df.iloc[index, 0]
        state = df.iloc[index, 1]
        global atrium_state

        if room == atrium and state == 1:
            atrium_state = state
            return True
        return False
    i = 0
    last_index = df.shape[0]-1


    while i < last_index:
        room = df.iloc[i, 0]

        if check_if_atrium_out(i) == False:     #non è un atrio di uscita
            if check_if_atrium(i):                  # è atrio di ingresso
                next_room = df.iloc[i+1, 0]
                if next_room != atrium:
                    key = room[0]+next_room[0]
                    transictions[key] += 1
                    i += 1
                else:                          # successiva è atrio
                    atrium_state = 0        # perche' non esisitono coppie spurie nel dataset
                    j = i+2
                    while j < last_index:
                        if df.iloc[j, 0] != atrium:
                            key = 'A' + df.iloc[j,0][0]
                            transictions[key] += 1
                            i = j
                            break
                        elif j == last_index-1:
                            i = last_index
                            atrium_state = df.iloc[j,1]
                            j += 1
                        else:
                            atrium_state = df.iloc[j, 1]
                            j += 1
            elif df.iloc[i+1, 0] != atrium:         #la sucessiva non è un atrio

                if atrium_state == 1:
                    key = df.iloc[i,0][0] + 'A'
                    transictions[key] += 1
                    key = 'A' + df.iloc[i+1, 0][0]
                    transictions[key] += 1
                    i += 1

                else:
                    key = df.iloc[i,0][0] + df.iloc[i+1,0][0]
                    transictions[key] += 1
                    i += 1
            else:                                   #la sucessiva è un atrio
                if df.iloc[i+1, 1] == 1:
                    key = room[0] + df.iloc[i+1,0][0]
                    transictions[key] += 1
                    atrium_state = 1
                    i += 1
                else:
                    key = room[0] + df.iloc[i + 2, 0][0]
                    transictions[key] += 1
                    atrium_state = 0
                    i += 2
        else:
            atrium_state = 0
            i += 1


def statistics(transictions):
    output = {"KA": 0, "KL": 0, "KT": 0, "KB": 0, "AK": 0, "AL": 0, "AT": 0, "AB": 0, "LA": 0, "LT": 0, "LB": 0,
              "LK": 0, "BA": 0,"BL": 0, "BK": 0, "BT": 0, "TA": 0, "TL": 0, "TB": 0, "TK": 0, "AA": 0, "LL": 0,
              "BB": 0, "TT": 0,"KK": 0}
    total_sum = {"K" : 0, "A"  : 0, "L"  : 0, "B"  : 0, "T"  : 0}
    for k in total_sum:
        for key in transictions:
            if key[0] == k:
                total_sum[k] = total_sum[k] + transictions[key]

    for i in output:
        output[i] = (transictions[i]/total_sum[i[0]])*100
    return output


if __name__ == "__main__":
    path = "/home/orso_matteo/Documents/Tesi/sensor-pattern-analysis/data2/MovementState/"
    file_name = "sequenceofMS.csv"
    file_test = "test.csv"
    transictions = {"KA":0, "KL":0, "KT":0, "KB":0, "AK":0, "AL":0, "AT":0,"AB":0,"LA":0,"LT":0,"LB":0,"LK":0,"BA":0,
                    "BL":0,"BK":0,"BT":0,"TA":0,"TL":0,"TB":0,"TK":0, "AA":0, "LL":0, "BB":0, "TT":0, "KK":0 }
    df = read_sequence_MS(path+file_name)
    #df = read_sequence_MS(file_test)       #test mode
    atrium_state = 0
    compute_transictions(df)
    print(transictions)
    statistics_transictions = statistics(transictions)
    print(statistics_transictions)
    #f = open("out.txt", "w")
    #for i in transictions:
