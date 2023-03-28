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
    print(s)
    s.set_relative_zero_all()
    print(s)

    print(s)
    s.set_axis_position_relative(-1, -2000, 500)
    time.sleep(5)
    print(s)

    # while True:
    #     try:
    #         print(s)
    #         time.sleep(1)
    #     except KeyboardInterrupt:
    #         break
