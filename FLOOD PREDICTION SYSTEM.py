import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

#ports = serial.tools.list_ports.comports()
#for port, desc, hwid in sorted(ports):
    #print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
print(ser.readline())
#print(htr1)
#print(a)
res = 1
i = 0

time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
    #cc = str(1234)
    #print(cc)
    #val = cc
    firebase1 = firebase.FirebaseApplication('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        temp = a[0]
        temp = temp[5:]
        data0 = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': temp,
                'time': datetime.now().strftime("%H:%M:%S")
                }
        result0 = firebase1.patch('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/' + '/TEMPERATURE_data/' + str(i), data0)
        print(result0)
    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        humidity = a[1]
        humidity = humidity[4:]
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': humidity,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result1 = firebase1.patch('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/' + '/HUMIDITY_data/' + str(i), data1)
        print(result1)
    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        rain = a[2]
        rain = rain[3:]
        data2 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': rain,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result2 = firebase1.patch('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/' + '/RAIN_data/' + str(i), data2)
        print(result2)
    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        flow_rate = a[3]
        flow_rate = flow_rate[4:]
        data3 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': flow_rate,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result3 = firebase1.patch('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/' + '/WATER_FLOW_data/' + str(i), data3)
        print(result3)
    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        Distance_inches = a[4]
        Distance_inches = Distance_inches[4:][:-5]
        data4 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': Distance_inches,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result4 = firebase1.patch('https://flood-prediction-system-dd224-default-rtdb.firebaseio.com/' + '/WATER_LEVEL_data/' + str(i), data4)
        print(result4)

