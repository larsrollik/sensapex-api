import logging

import numpy as np
from sensapex import UMP


def get_device_list(library_path: str = None):
    """"""
    UMP.set_library_path(library_path)
    ump = UMP.get_ump()
    return ump.list_devices()


def get_device_by_id(device_id=None, library_path: str = None):
    """"""
    UMP.set_library_path(library_path)
    ump = UMP.get_ump()
    return ump.get_device(device_id)


class SensapexManipulator:
    """Meta wrapper for Sensapex manipulator API

    device methods for manipulators:
        dev_id
        get_pos
        goto_pos
        is_busy
        n_axes

        stop

    methods on device.ump object

        broadcast_address
        calibrate_zero_position

        manipulator.ump.get_firmware_version

    """

    id = None
    device = None
    library_path = None

    default_move_speed = None

    _position = None
    _relative_zero = None

    def __init__(
        self,
        device_id: int = None,
        library_path: str = "/usr/lib",
        default_move_speed: int = 5,
    ):
        """

        :param device_id:
        :param library_path:
        :param default_move_speed:
        """
        super(SensapexManipulator, self).__init__()
        logging.debug(
            f"Initialising SensapexManipulator object for device={device_id}. "
            f"Library: '{library_path}'. default_move_speed={default_move_speed}"
        )
        self.id = device_id
        self.library_path = library_path
        self.device = get_device_by_id(
            device_id=self.id, library_path=self.library_path
        )

        assert 1 <= default_move_speed < np.inf
        self.default_move_speed = default_move_speed

    @property
    def is_busy(self):
        """Returns if manipulator is busy"""
        is_busy = self.device.is_busy()
        logging.debug(
            f"Manipulator reports to be: {'busy' if is_busy else 'ready'} ({is_busy})"
        )
        return is_busy

    @property
    def position(self):
        """Get position of all axes"""
        current_position = self.device.get_pos()
        logging.debug(f"Current position reading: {current_position}")
        return np.asarray(current_position)

    @property
    def relative_zero(self):
        """Get relative position of all axes"""
        if self._relative_zero is None:
            logging.debug("No relative zero set")
            return None

        relative_zero = self.position - self._relative_zero
        logging.debug(f"Relative zero: {relative_zero.tolist()}")
        return relative_zero

    @relative_zero.setter
    def relative_zero(self, pos):
        """Get current position relative to relative origin"""
        pos = np.asarray(pos)
        curr_zero = (
            self._relative_zero.tolist()
            if self._relative_zero is not None
            else self._relative_zero
        )
        logging.debug(
            f"Setting relative zero from->to: {curr_zero} -> {pos.tolist()}"
        )
        self._relative_zero = pos

    def set_relative_zero_all(self):
        """Set current position to new relative zero position on ALL axes"""
        logging.debug("Requested relative zero for all axes")
        self.relative_zero = self.position

    def set_relative_zero_axis(self, axis: int = None):
        """Set current position to new relative zero position on SPECICIEF axis"""
        logging.debug(f"Requested relative zero for axis: {axis}")
        if self.relative_zero is None:
            self.relative_zero = self.position
        self._relative_zero[axis] = self.position[axis]

    def get_device_state(self):
        """Get device metadata as dictionary"""
        if self.device is None:
            return {}

        state = {
            "device_id": self.device.dev_id,
            "is_busy": self.device.is_busy(),
            "n_axes": self.device.n_axes(),
            "position": self.position.tolist(),
            "relative_position": self.relative_zero.tolist(),
            "broadcast_address": self.device.ump.broadcast_address,
            "firmware_version": self.device.ump.get_firmware_version(self.id),
        }
        logging.debug(state)
        return state

    def set_position(
        self,
        position=None,
        speed: int = None,
        simultaneous=False,
        linear=False,
        max_acceleration=0,
    ):
        """Set absolute position of all axes

        :param position: [x, y, z, w] target position list, in um
        :param speed: speed, in um/s
        :param simultaneous: move all axes simultaneously
        :param linear: if simultaneous movement, then setting same speed value on all axes, otherwise distance-dependent
        :param max_acceleration: in um/(s**2), default=0 will be evaluated to default in ump object
        :return:
        """
        if position is None:
            return

        if speed is None:
            speed = self.default_move_speed

        # https://github.com/sensapex/sensapex-py/blob/bc715130ca1c64dfcaa6a93ce0d5c31bdadd732a/sensapex/sensapex.py#L166
        assert len(position) == self.device.n_axes()

        # https://github.com/sensapex/sensapex-py/blob/bc715130ca1c64dfcaa6a93ce0d5c31bdadd732a/sensapex/sensapex.py#L165
        assert speed >= 1

        self.device.goto_pos(
            position,
            speed,
            simultaneous=simultaneous,
            linear=linear,
            max_acceleration=max_acceleration,
        )

    def get_axis_position(self, axis: int = None):
        """Get position of specified axis

        :param axis: int
        :return: list of position floats
        """
        current_axis_position = self.position[axis]
        logging.debug(f"Axis {axis} position: {current_axis_position}")
        return current_axis_position

    def set_axis_position(
        self,
        axis: int = None,
        position: float = None,
        speed: int = None,
        **kwargs,
    ):
        """Set position of specified axis"""
        new_position = self.position
        new_position[axis] = position
        self.set_position(new_position, speed=speed, **kwargs)

    def set_axis_position_relative(
        self,
        axis: int = None,
        distance: float = None,
        speed: int = None,
        **kwargs,
    ):
        """Move axis by specified relative distance from current position"""
        current_axis_position = self.get_axis_position(axis=axis)
        new_axis_position = current_axis_position + distance

        logging.debug(
            f"Requested move on axis={axis} by {distance}µm at {speed}µm/s. kwargs: {kwargs}"
        )

        self.set_axis_position(
            axis=axis, position=new_axis_position, speed=speed, **kwargs
        )
