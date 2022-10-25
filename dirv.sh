#!/bin/bash

python met-cap.py $1 ./walk.json
python sankey-graph.py
