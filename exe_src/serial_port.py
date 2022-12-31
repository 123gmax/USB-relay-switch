import serial

START_ID = 0xA0
ON_ID = 0x01
OFF_ID = 0x00


def Get_Cmd_Prototype():
    data = bytearray()
    data.append(START_ID)
    data.append(0x00)  # Switch Number
    data.append(0x00)  # Action ON or OFF
    return data


def Send_Data(port, data):
    try:
        ser = serial.Serial(port)
        ser.write(data)
        ser.close()
        return True
    except:
        return False


def Get_ON_Cmd(SWITCH_NUM):
    data = Get_Cmd_Prototype()
    data[1] = SWITCH_NUM
    data[2] = ON_ID
    data.append(data[0] + data[1] + data[2])
    return data


def Get_OFF_Cmd(SWITCH_NUM):
    data = Get_Cmd_Prototype()
    data[1] = SWITCH_NUM
    data[2] = OFF_ID
    data.append(data[0] + data[1] + data[2])
    return data


def Turn_Relay_ON(port):
    cmd = Get_ON_Cmd(1)
    status = Send_Data(port=port, data=cmd)
    return status


def Turn_Relay_OFF(port):
    cmd = Get_OFF_Cmd(1)
    status = Send_Data(port=port, data=cmd)
    return status


if __name__ == "__main__":
    print()
    #print(Turn_Relay_ON("/dev/ttyUSB0"))
    print(Turn_Relay_OFF("/dev/ttyUSB0"))
