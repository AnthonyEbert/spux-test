#!/bin/bash

bsub -n 145 -W 24:00 -J spux-rwalk -oo report.dat < script-euler.sh
