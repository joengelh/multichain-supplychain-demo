#!/bin/bash

python3 api-bank/src/main.py &
python3 api-iot/src/main.py &
python3 api-stakeHolder/src/main.py oem 5003 &
python3 api-stakeHolder/src/main.py customer 5007 &
python3 api-stakeHolder/src/main.py serviceProvider 5009 &
python3 frontend-bank/main.py #&
#python3 frontend-stakeHolder/main.py

