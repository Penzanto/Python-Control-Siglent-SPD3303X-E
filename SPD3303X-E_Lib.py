#-----------------------------------------------------------------Description-----------------------------------------------------------------
# This python file is a library that can be used to control via Ethernet only the power supply SPD 3303X-E.
#-----------------------------------------------------------------lib used-----------------------------------------------------------------
import pyvisa   #lib used to send SCPI command to the equipment throught the VISA library

#-----------------------------------------------------------------Main-----------------------------------------------------------------
def PSU_SPD_Reset(StrVisaName):
    """function that reset the PSU (set all of the output to OFF and voltage/current of each channel to 0)

    Args:
        StrVisaName (string): visa name of the PSU
    """
    #Turn off all of the output of the PSU
    PSU_SPD_channelOnOff(StrVisaName, 1, 0)
    PSU_SPD_channelOnOff(StrVisaName, 2, 0)
    PSU_SPD_channelOnOff(StrVisaName, 3, 0)
    #set both channel to be indepedant
    PSU_SPD_SeriesParallelIndependant(StrVisaName, 0)
    #Set the voltage of each channel to 0
    PSU_SPD_SetVoltage(StrVisaName, 1, 0)
    PSU_SPD_SetVoltage(StrVisaName, 2, 0)
    #Set the current of each channel to 0
    PSU_SPD_SetCurrent(StrVisaName, 1, 0)
    PSU_SPD_SetCurrent(StrVisaName, 2, 0)

def PSU_SPD_channelOnOff(StrVisaName, Numchannel, NumOnOff):
    """Function that turn On and Off a channel output

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2 or 3)
        NumOnOff (number): 0 to turn off the output, 1 to turn it on
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    if (NumOnOff==1):
        visaHandle.write("OUTPut CH" + str(Numchannel) +",ON")
    else:
        visaHandle.write("OUTPut CH" + str(Numchannel) +",OFF")
    visaHandle.query("*IDN?")
    visaHandle.close()

def PSU_SPD_SetVoltage(StrVisaName, Numchannel, NumVoltage):
    """Function that change the voltage of one of the channel of the PSU

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2)
        NumVoltage (number): set voltage of the channel (0 up to 32)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    visaHandle.write("CH" + str(Numchannel) + ":VOLTage " +str(NumVoltage))
    visaHandle.query("*IDN?")
    visaHandle.close()

def PSU_SPD_SetCurrent(StrVisaName, Numchannel, NumCurent):
    """Function that change the current of one of the channel of the PSU

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2)
        NumCurrent (number): set current of the channel (0 up to 3.2)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    visaHandle.write("CH" + str(Numchannel) + ":CURRent " +str(NumCurent))
    visaHandle.query("*IDN?")
    visaHandle.close()

def PSU_SPD_ReadCurrent(StrVisaName, Numchannel):
    """function that return the current of a channel of the PSU

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2)

    return
        (number): return the current of a channel of the PSU
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    return(visaHandle.query("MEASure:CURRent? CH" +str(Numchannel)))

def PSU_SPD_ReadVoltage(StrVisaName, Numchannel):
    """function that return the voltage of a channel of the PSU

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2)

    return
        (number): return the voltage of a channel of the PSU
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    return(visaHandle.query("MEASure:VOLTage? CH" +str(Numchannel)))

def PSU_SPD_ReadPower(StrVisaName, Numchannel):
    """function that return the power of a channel of the PSU

    Args:
        StrVisaName (string): visa name of the PSU
        Numchannel (number): channel number of the PSU (1, 2)

    return
        (number): return the power of a channel of the PSU
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    return(visaHandle.query("MEASure:POWEr? CH" +str(Numchannel)))

def PSU_SPD_SeriesParallelIndependant(StrVisaName, numMode):
    """function that set the PSU output to be in series, parallel or independant

    Args:
        StrVisaName (string): visa name of the PSU
        numMode (number): 0 = CH1 and CH2 are independant, 1 = CH1 and CH2 in series, 2 = CH1 and CH2 in parallel
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write_termination = '\n'
    visaHandle.read_termination = '\n'
    visaHandle.write("OUTPut:TRACK " + str(numMode))
    visaHandle.query("*IDN?")
    visaHandle.close()

#-----------------------------------------------------------------__name__ guard-----------------------------------------------------------------
if __name__ == "__main__":
    None

    # #Exemple use of this library
    # StrVisaName = "TCPIP0::192.168.1.22::inst0::INSTR"
    # #reset the PSU
    # PSU_SPD_Reset(StrVisaName)
    # #set the voltage of the PSU
    # PSU_SPD_SetVoltage(StrVisaName, 1, 10)
    # PSU_SPD_SetVoltage(StrVisaName, 2, 20)
    # #set the current of the PSU
    # PSU_SPD_SetCurrent(StrVisaName, 1, 1)
    # PSU_SPD_SetCurrent(StrVisaName, 2, 2)
    # #set the channel output
    # PSU_SPD_channelOnOff(StrVisaName, 1, 1)
    # PSU_SPD_channelOnOff(StrVisaName, 2, 1)
    # PSU_SPD_channelOnOff(StrVisaName, 3, 1)
    # #measure the voltage output of the PSU
    # print("CH1 voltage value: " + str(PSU_SPD_ReadVoltage(StrVisaName, 1)) + "V")
    # print("CH2 voltage value: " + str(PSU_SPD_ReadVoltage(StrVisaName, 2)) + "V")
    # #measure the current output of the PSU
    # print("CH1 current value: " + str(PSU_SPD_ReadCurrent(StrVisaName, 1)) + "A")
    # print("CH2 current value: " + str(PSU_SPD_ReadCurrent(StrVisaName, 2)) + "A")
    # #measure the power output of the PSU
    # print("CH1 power value: " + str(PSU_SPD_ReadPower(StrVisaName, 1)) + "W")
    # print("CH2 power value: " + str(PSU_SPD_ReadPower(StrVisaName, 2)) + "W")
    # #reset the PSU
    # PSU_SPD_Reset(StrVisaName)