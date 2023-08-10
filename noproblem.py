import os

import cityflow
import json
import numpy as np

config = {
    "interval": 1.0,
    "seed": 0,
    "dir": "./",
    "roadnetFile": "roadnet_manhattan.json",
    "flowFile": "manhattan_7846.json",
    "laneChange": False,
    "rlTrafficLight": True,
    "saveReplay": True,
    "roadnetLogFile": "frontend/web/roadnetLogFile.json",
    "replayLogFile": "frontend/web/replayLogFile.txt"
}


with open('config.json', 'w') as fp:
    json.dump(config, fp)

config_path = 'config.json'
eng = cityflow.Engine(config_path, thread_num=1)


file = os.path.join(config["dir"], config["roadnetFile"])
for i in range(10000000):

    with open('{0}'.format(file)) as json_data:

        net = json.load(json_data)
        for inter in net['intersections']:
            if not inter['virtual']:
                eng.set_tl_phase(inter['id'], np.random.randint(0,100) % len(inter['trafficLight']['lightphases']))

        for p in range(10):
            eng.next_step()




