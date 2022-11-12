import time
import wiotp.sdk.application

myConfig={

"identity":{
    "orgID" : "cb7mz1",
    "typeID" : "jayashree123",
    "deviceID" : "jayashreeid",
    },
    "auth" : {
        "token":"+?PWUcJLsI@Om4(bKy"
        }
}

        

client= wiotp.sdk.device.DeviceClient (config= myConfig, logitandlers = None)

client.connect()

while True:
    name = "Child"
    latitude = 11.020503
    longitude = 76.935123

    myData ={'name' : name, 'lat': latitude, 'lon': longitude}
    client.publishEvent (eventId = "status", msgFormat = "json", data= myData, qos=0, onPublish = none)
    print("Data published to IBM IoT Platform:", myData)
    time.sleep (5)

client.disconnect()
