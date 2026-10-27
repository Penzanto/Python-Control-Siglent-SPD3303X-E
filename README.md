# Python-Control-Siglent-SPD3303X-E
A python lib file that can be used to control a Siglent SPD3303X-E via ethernet only using VISA command (it doesn’t work with a USB connection).

This python file can be called to use the following function on the Siglent SPD3303X-E power supply:
  -	Reset the power supply (disable all channel. Set the channel 1 and 2 to be independent with a voltage and current output of 0V and 0A)
  -	Tun On/Off a channel
  -	Set the voltage of a channel
  -	Set the current of a channel
  -	Measure the voltage output of a specific channel
  -	Measure the current output of a specific channel
  -	Measure the power output of a specific channel
  -	Set the channel 1 and 2 to be in series, parallel or independent from each other

At the end of the python file, you will see an example of how to use each of the function of this lib.

This python file uses the Pyvisa library. So, to use it you would need to install the Pyvisa lib and a visa library (Like the ni-visa library from National Instrument).

