#!/usr/bin/python3

import json
import sys

filename="global_conf.json"

# print(sys.argv)

if len(sys.argv) > 1:
        filename=sys.argv[1]

# Open and read the JSON file
with open(filename, 'r') as file:
    data = json.load(file)

# Print the data


sx_conf="SX1301_conf"

if sx_conf not in data:
        sx_conf="SX130x_conf"

if sx_conf not in data:
        print("SX130x object not found in JSON")
        exit()

for i in range(0,8):
        channel_n="chan_multiSF_" + str(i)
        radio_n= "radio_" + str(data[sx_conf][channel_n]["radio"])
        print("CH" + str(i) + ":", data[sx_conf][channel_n]["if"] + data[sx_conf][radio_n]["freq"], radio_n,"EN:", str(data[sx_conf][channel_n]["enable"]))

channel_n="chan_Lora_std"
# LORA SINGLE CHANNEL
radio_n= "radio_" + str(data[sx_conf][channel_n]["radio"])
print("STD" + ":", data[sx_conf][channel_n]["if"] + data[sx_conf][radio_n]["freq"], radio_n, "EN:", str(data[sx_conf][channel_n]["enable"]))

channel_n="chan_FSK"
# FSK CHANNEL
radio_n= "radio_" + str(data[sx_conf][channel_n]["radio"])
print("FSK" + ":", data[sx_conf][channel_n]["if"] + data[sx_conf][radio_n]["freq"], radio_n, "EN:", str(data[sx_conf][channel_n]["enable"]))

print("RD0:", data[sx_conf]["radio_0"]["freq"])
print("RD1:", data[sx_conf]["radio_1"]["freq"])
