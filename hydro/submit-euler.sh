#!/bin/bash

bsub -n 1121 -W 24:00 -J spux-hydro -oo report.dat < script-euler.sh
