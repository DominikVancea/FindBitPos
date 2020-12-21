import json
from random import randint
import asyncio
import websockets
import os

async def Socket(websocket, path):

    i = 0
    ReadData = []
    SendData = {"Error": "", "BitPos": 0, "BytePos": 0}

    RecvData = await websocket.recv()

    #Get random 5 digit number for filename
    FileName = ("temp/" + str(randint(10000, 99999)) + ".bin")

    #Create directory "temp" when not avaible
    try:
        File = open(FileName, "w")
    except FileNotFoundError:
        os.system("mkdir temp")
        File = open(FileName, "w")

    File.write(RecvData)
    File.close()

    LineOutput = os.popen("./FindBitPos " + FileName).read()

    #Process Output from c Programm
    if LineOutput == "":
        SendData["Error"] = "No set Bit found"
    else:

        #Seperate bit position and byte position
        for i in range(0, len(LineOutput)):

            if LineOutput[i] == ":":
                ReadData.insert(0, LineOutput[i - 1:i])

                ReadData.insert(1, LineOutput[(1 - (len(LineOutput) - 1)):])

                BitPos = ReadData[0]
                BytePos = ReadData[1]

                SendData["BitPos"] = BitPos
                SendData["BytePos"] = BytePos

    os.remove(FileName)

    #Convert positions to JSON and send to the client
    SendData = json.dumps(SendData)

    await websocket.send(str(SendData))

start_server = websockets.serve(Socket, "", 5001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
