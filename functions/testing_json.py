#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import ujson
ev3 = EV3Brick()

with open('action.json') as f:
  parsed = ujson.load(f)
  print(parsed["actions"],file=stderr)