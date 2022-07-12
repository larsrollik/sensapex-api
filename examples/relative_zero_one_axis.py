import logging
import time

from sensapex_api.manipulator import SensapexManipulator

logging.getLogger().setLevel("DEBUG")


def print_positions(s):
    print("origin  ", s._relative_zero)
    print("position", s.position)
    print("relative", s.relative_zero)


if __name__ == "__main__":
    s = SensapexManipulator(device_id=1)
    s.set_relative_zero_axis(-1)

    print_positions(s)
    s.set_axis_position_relative(-1, -2000, 500)
    time.sleep(5)
    print_positions(s)
