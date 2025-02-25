import serial
import serial.tools.list_ports
from enum import IntEnum


class SCPIValue():

    OFF      = "OFF"
    ON       = "ON"
    EXTERNAL = "EXTERNAL"
    INTERNAL = "INTERNAL"

class SCPICommandType(IntEnum):

    EMPTY_COMMAND = 0
    SET_COMMAND   = 1
    QUERY_COMMAND = 2


class SCPICommand():

    def __init__(self, cmd_str : str, cmd_type : SCPICommandType):

        self.cmd_str = cmd_str
        self.cmd_type = cmd_type

    def send_str(self):

        send_str = self.cmd_str + "\r\n"

        return send_str.encode()

    def query_cmd(self):

        get_cmd_str = self.cmd_str.split()[0]
        get_cmd_str += "?"

        return SCPICommand(get_cmd_str, SCPICommandType.QUERY_COMMAND)

class SCPICommonComands():

    CLEAR_STATUS        = SCPICommand("*CLS", SCPICommandType.EMPTY_COMMAND)
    EVENT_STATUS_EN     = SCPICommand("*ESE", SCPICommandType.SET_COMMAND)
    EVENT_STATUS_QUERY  = SCPICommand("*ESE?", SCPICommandType.QUERY_COMMAND)
    EVENT_STATUS_ENREG  = SCPICommand("*ESR", SCPICommandType.EMPTY_COMMAND)
    IDENTIFY            = SCPICommand("*IDN?", SCPICommandType.QUERY_COMMAND)
    OP_COMPLETE         = SCPICommand("*OPC", SCPICommandType.EMPTY_COMMAND)
    OP_COMPLETE_QUERY   = SCPICommand("*CLS", SCPICommandType.QUERY_COMMAND)
    IDENTIFY_OPTIONS    = SCPICommand("*OPT?", SCPICommandType.QUERY_COMMAND)
    RESET               = SCPICommand("*RST", SCPICommandType.EMPTY_COMMAND)
    SERV_REQ_EN         = SCPICommand("*SRE", SCPICommandType.SET_COMMAND)
    SERV_REQ_EN_QUERY   = SCPICommand("*SRE?", SCPICommandType.QUERY_COMMAND)
    STATUS_BYTE_QUERY   = SCPICommand("*STB?", SCPICommandType.QUERY_COMMAND)
    TRIGGER             = SCPICommand("*TRG", SCPICommandType.EMPTY_COMMAND)
    SELF_TEST_QUERY     = SCPICommand("*TST?", SCPICommandType.QUERY_COMMAND)
    WAIT                = SCPICommand("*WAI", SCPICommandType.EMPTY_COMMAND)


class SCPI():

    def __init__(self, port : str = None, baud_rate : int = 9600, timeout : float = 1.0, debug_mode : bool = False, comm_id : str = None):

        if(port is None and comm_id is None):

            comm_id = "ACM"
            print(f"WARNING: Defaulting on finding comm with {comm_id}")

        if(port is None):

            ports_avail = serial.tools.list_ports.comports()

            for avail_port in ports_avail:

                if(avail_port.product is None): continue

                if(comm_id in avail_port.product):

                    port = avail_port.device
                    break

            if(port is None):

                print("ERROR: Unable to Find Port. Please Specify Manually")

        self.timeout = timeout
        self.comm_port = serial.Serial(port, baud_rate, timeout=self.timeout)

        self.timeout = timeout
        self.debug   = debug_mode

    def send_cmd(self, cmd: SCPICommand, value=None):

        ret_value = None
        cmd_copy = cmd

        if(cmd.cmd_type is SCPICommandType.EMPTY_COMMAND):

            self._send_cmd(cmd_copy)

        elif(cmd.cmd_type is SCPICommandType.QUERY_COMMAND):

            if(cmd_copy.cmd_str[-1] != "?"):

                print(f"WARNING: {cmd_copy.cmd_str} Did Not Contain ?")

            ret_value = self._send_cmd(cmd)

        elif(cmd_copy.cmd_type is SCPICommandType.SET_COMMAND):

            if(value is None):

                print(f"WARNING: {cmd_copy.cmd_str} Had No Set Value Given")

            else:

                cmd_copy.cmd_str += " " + str(value)

            resp = self._send_cmd(cmd_copy)

            if(str(value) != str(resp)):

                print(f"ERROR: {cmd_copy.cmd_str} Set Value to {resp} Instead of {value}")

            ret_value = resp

        else:

            print(f"ERROR: Reached End Of If Statement In SCPI.py send_cmd")

        return ret_value

    def _send_cmd(self, cmd: SCPICommand):

        ret_value = None

        if(self.debug):

            print(f"DEBUG: Send String Is {cmd.send_str()}")

        self.comm_port.write(cmd.send_str())

        if(cmd.cmd_type is SCPICommandType.QUERY_COMMAND):

            try:

                ret_value = self.comm_port.read_until(b"\r\n")
                ret_value = ret_value.decode()
                ret_value = ret_value.strip("\r\n")

            except:

                print(f"ERROR: Get Command {cmd.cmd_str} Failed To Rx Data In {self.timeout} Duration")

        elif(cmd.cmd_type is SCPICommandType.SET_COMMAND):

            ret_value = self._send_cmd(cmd.query_cmd())


        return ret_value