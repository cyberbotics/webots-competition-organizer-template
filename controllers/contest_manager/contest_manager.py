#!/usr/bin/env python3
#
# Copyright 1996-2021 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from controller import Supervisor


referee = Supervisor()
timestep = int(referee.getBasicTimeStep())

robot0_node = referee.getFromDef('R0')
robot1_node = referee.getFromDef('R1')
emitter = referee.getDevice('emitter')

winner = None
points0 = None
points1 = None

while referee.step(timestep) != -1:
    altitude0 = robot0_node.getPosition()[1]
    altitude1 = robot1_node.getPosition()[1]

    if altitude0 < 0.04:
        winner = 1
        points0 = -referee.getTime()
        points1 = 0
        break

    if altitude1 < 0.04:
        winner = 0
        points0 = 0
        points1 = -referee.getTime()
        break

# Store the results
with open('/tmp/results.txt', 'w') as f:
    f.write(f'winner: {winner}\n')
    f.write(f'points: {points0}, {points1}\n')

# We want to see the fall :)
referee.step(20 * timestep)

# Notify the end of the game
emitter.send('done'.encode('utf-8'))
referee.step(timestep)
