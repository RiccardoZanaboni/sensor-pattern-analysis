import pandas as pd
import hlt_state

def create_df_fsm_differentation(fsm_states):
    def state_conversion(element):
        switch = {hlt_state.HltState.WORKING :[1,0,0,0], hlt_state.HltState.WARNING_NOT_SAMPLE : [0,1,0,0],
                  hlt_state.HltState.WARNING_EQUAL_MEASURES : [0,0,1,0], hlt_state.HltState.NOT_WORKING : [0,0,0,1]}
        return switch[element.iat[0,1]]

    fsm_different_states = pd.DataFrame(columns=['Timestamp', 'WORKING', 'WARNING_NOT_SAMPLE', 'WARNING_EQUAL_MEASURES',
                                              'NOT_WORKING'])
    for i in range(0,fsm_states.shape[0]):
        tmp = state_conversion(fsm_states.iloc[[i]])
        fsm_different_states = fsm_different_states.append({'Timestamp': fsm_states.iloc[[i]].iat[0, 0] ,'WORKING' : tmp[0],
                                     'WARNING_NOT_SAMPLE' : tmp[1], 'WARNING_EQUAL_MEASURES' : tmp[2],
                                     'NOT_WORKING' : tmp[3]}, ignore_index=True)
    return fsm_different_states

def read_samples():
    return pd.read_csv("fsm_hlt_7_beta.csv", ",")

if __name__ == '__main__':

    df = read_samples()
    fsm_different_states = create_df_fsm_differentation(df)
    fsm_different_states.to_csv("fsm_hlt_7_separate.csv", index=False)