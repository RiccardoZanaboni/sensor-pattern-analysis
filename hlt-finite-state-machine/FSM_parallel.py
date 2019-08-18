import pandas as pd
import hlt_state
import Read_configurations


def create_df_fsm_differentation(fsm_states):
    """Create a DataFrame so that tsl can show parallel plots"""

    def state_conversion(element):
        """Create a dictionary: key the state value, value the matching sequence output for the state"""
        switch = {hlt_state.HltState.WORKING: [1, 0, 0, 0], hlt_state.HltState.WARNING_NOT_SAMPLE: [0, 1, 0, 0],
                  hlt_state.HltState.WARNING_EQUAL_MEASURES: [0, 0, 1, 0], hlt_state.HltState.NOT_WORKING: [0, 0, 0, 1]}
        return switch[element.iat[0, 1]]

    state = Read_configurations.open_json()["state"]
    col = ["Timestamp"] + state
    fsm_different_states = pd.DataFrame(columns=col)
    for i in range(0, fsm_states.shape[0]):
        tmp = state_conversion(fsm_states.iloc[[i]])
        fsm_different_states = fsm_different_states.append({'Timestamp': fsm_states.iloc[[i]].iat[0, 0],
                                                            state[0]: tmp[0], state[1]: tmp[1], state[2]: tmp[2],
                                                            state[3]: tmp[3]},
                                                           ignore_index=True)
    return fsm_different_states


def read_samples():
    return pd.read_csv(Read_configurations.open_json()["info"]["path_directory_input_parallel"] +
                       ["info"]["file_input_parallel"], ",")


if __name__ == '__main__':
    df = read_samples()
    fsm_different_states = create_df_fsm_differentation(df)
    fsm_different_states.to_csv(Read_configurations.open_json()["info"]["path_directory_output_parallel"] +
                                ["info"]["file_output_parallel"], index=False)
