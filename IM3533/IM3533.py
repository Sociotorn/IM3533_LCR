from SCPI.SCPI import *

class IM3533_CMD(SCPICommonComands):
    # Average Commands
    SET_AVERAGE_NUM = SCPICommand(":AVER", SCPICommandType.SET_COMMAND)
    GET_AVERAGE_NUM = SCPICommand(":AVER?", SCPICommandType.QUERY_COMMAND)

    # DC Bias Commands
    SET_DC_BIAS       = SCPICommand(":DCBIAS", SCPICommandType.SET_COMMAND)
    GET_DC_BIAS       = SCPICommand(":DCBIAS?", SCPICommandType.QUERY_COMMAND)
    SET_DC_BIAS_LEVEL = SCPICommand(":DCBIAS:LEV", SCPICommandType.SET_COMMAND)
    GET_DC_BIAS_LEVEL = SCPICommand(":DCBIAS:LEV?", SCPICommandType.QUERY_COMMAND)

    # Measurement Frequency Commands
    SET_MEAS_FREQ = SCPICommand(":FREQ", SCPICommandType.SET_COMMAND)
    GET_MEAS_FREQ = SCPICommand(":FREQ?", SCPICommandType.QUERY_COMMAND)

    # Parameter Settings
    SET_PARAM1_MODE = SCPICommand(":PAR1", SCPICommandType.SET_COMMAND)
    GET_PARAM1_MODE = SCPICommand(":PAR1", SCPICommandType.QUERY_COMMAND)
    SET_PARAM2_MODE = SCPICommand(":PAR2", SCPICommandType.SET_COMMAND)
    GET_PARAM2_MODE = SCPICommand(":PAR2", SCPICommandType.QUERY_COMMAND)
    SET_PARAM3_MODE = SCPICommand(":PAR3", SCPICommandType.SET_COMMAND)
    GET_PARAM3_MODE = SCPICommand(":PAR3", SCPICommandType.QUERY_COMMAND)
    SET_PARAM4_MODE = SCPICommand(":PAR4", SCPICommandType.SET_COMMAND)
    GET_PARAM4_MODE = SCPICommand(":PAR4", SCPICommandType.QUERY_COMMAND)

    # Trigger Commands
    SET_TRIG_MODE = SCPICommand(":TRIG", SCPICommandType.SET_COMMAND)
    GET_TRIG_MODE = SCPICommand(":TRIG", SCPICommandType.QUERY_COMMAND)
    SET_TRIG_DELAY = SCPICommand(":TRIG", SCPICommandType.SET_COMMAND)
    GET_TRIG_DELAY = SCPICommand(":TRIG?", SCPICommandType.QUERY_COMMAND)

    #Measurement Speed Commands
    SET_MEAS_SPEED = SCPICommand(":SPEE", SCPICommandType.SET_COMMAND)
    GET_MEAS_SPEED = SCPICommand(":SPEE?", SCPICommandType.QUERY_COMMAND)

    # Voltage Control Commands
    SET_OC_VOLTAGE = SCPICommand(":LEV:VOLT", SCPICommandType.SET_COMMAND)
    GET_OC_VOLTAGE = SCPICommand(":LEV:VOLT?", SCPICommandType.QUERY_COMMAND)
    SET_LIMIT_MODE = SCPICommand(":LIM", SCPICommandType.SET_COMMAND)
    GET_LIMIT_MODE = SCPICommand(":LIM?", SCPICommandType.QUERY_COMMAND)
    SET_VOLT_LIMIT = SCPICommand(":LIM:VOLT", SCPICommandType.SET_COMMAND)
    GET_VOLT_LIMIT = SCPICommand(":LIM:VOLT?", SCPICommandType.QUERY_COMMAND)


class IM3533(SCPI):

    def __init__(self, port : str = None, baud_rate: int = 115200, timeout : float =1.0, debug_mode : bool = False):

        COMM_ID = "IM3533"
        super().__init__(port=port, baud_rate=baud_rate, timeout=timeout, debug_mode=debug_mode, comm_id=COMM_ID)

        self.send_cmd(IM3533_CMD.RESET)

if __name__ == "__main__":

    lcr = IM3533(debug_mode=True)

    print(lcr.send_cmd(IM3533_CMD.IDENTIFY))
    print(lcr.send_cmd(IM3533_CMD.IDENTIFY))

    print(lcr.send_cmd(IM3533_CMD.SET_PARAM1_MODE, "CP"))