from sense_hat import SenseHat
import os

sense = SenseHat()


temp = sense.get_temperature()
print(temp)

def get_corrected_temp():

    cpu_temp = float(open("/sys/class/thermal/thermal_zone0/temp").read()) / 1000
    print(cpu_temp)
    temp = sense.get_temperature()
    adjustment = (cpu_temp - temp) / 1.5
    corrected_temp = temp - adjustment 
    return [str(corrected_temp), ' '+str(temp-7)+'\n'] # assume tmp-7 isabout the correct tmp

with open("meas.txt", "a" ) as file: 
    file.writelines(get_corrected_temp())




