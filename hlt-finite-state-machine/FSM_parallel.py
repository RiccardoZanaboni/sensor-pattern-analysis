import pandas as pd
import hlt_state
import Read_configurations
import sys


def create_df_fsm_differentation(fsm_states, configurator):
    """Create a DataFrame so that tsl can show parallel plots"""

    def state_conversion(element):
        """Create a dictionary: key the state value, value the matching sequence output for the state"""
        nonlocal configurator
        hlt = hlt_state.HltState(configurator)
        switch = {hlt.possible_states["WORKING"]: [1, 0, 0, 0],
                  hlt.possible_states["WARNING_NOT_SAMPLE"]: [0, 1, 0, 0],
                  hlt.possible_states["WARNING_EQUAL_MEASURES"]: [0, 0, 1, 0],
                  hlt.possible_states["NOT_WORKING"]: [0, 0, 0, 1]}
        return switch[element.iat[0, 1]]

    state = configurator["FSM_info"]["state"]
    col = ["Timestamp"] + state
    fsm_different_states = pd.DataFrame(columns=col)
    for i in range(0, fsm_states.shape[0]):
        tmp = state_conversion(fsm_states.iloc[[i]])
        fsm_different_states = fsm_different_states.append({'Timestamp': fsm_states.iloc[[i]].iat[0, 0],
                                                            state[0]: tmp[0], state[1]: tmp[1], state[2]: tmp[2],
                                                            state[3]: tmp[3]},
                                                           ignore_index=True)
    return fsm_different_states


def read_samples(configurator):
    return pd.read_csv(configurator["info"]["path_directory_input_parallel"] +
                       configurator["info"]["file_input_parallel"], ",")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = Read_configurations.open_json(sys.argv[1])
    df = read_samples(configurator)
    fsm_different_states = create_df_fsm_differentation(df, configurator)
    fsm_different_states.to_csv(configurator["info"]["path_directory_output_parallel"] +
                                configurator["info"]["file_output_parallel"], index=False)
