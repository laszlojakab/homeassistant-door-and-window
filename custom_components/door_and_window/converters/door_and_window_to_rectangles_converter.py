""" Module for door and window to rectangles converter. """
from ..models.door_and_window import DoorAndWindow
from ..models.door_and_window_rectangles import DoorAndWindowRectangles
from ..models.quadrilateral import Quadrilateral
from ..transformers.coordinate_transformations import CoordinateTransformations

# pylint: disable=too-few-public-methods


class DoorAndWindowToRectanglesConverter():
    """
    Responsible for converting `DoorAndWindow` instance to
    `DoorAndWindowRectangles` instance.
    """

    def __init__(self):
        self._transformations = CoordinateTransformations()

    def convert(self, door_and_window: DoorAndWindow) -> DoorAndWindowRectangles:
        """
        Converts the specified DoorAndWindow instance to rectangles
        which represent the DoorAndWindow instance in the 3D space.

        The origin is:
            - the outer surface of the glazing on Z axis
            - the center of the glazing on X axis
            - the ground level on Y axis

        The Y axis is positive to up.
        The X axis is positive to right as seen from outside.
        The Z axis is positive to inside.

        Args:
            door_and_window
                The DoorAndWindow instance to convert.

        Returns:
            Rectangles represents the door and window in the 3D space.
        """
        transformation_matrix = self._transformations.get_rotation_matrix_y(door_and_window.azimuth)
        transformation_matrix = transformation_matrix.dot(
            self._transformations.get_rotation_matrix_x(90 - door_and_window.tilt)
        )

        return DoorAndWindowRectangles(
            glazing=Quadrilateral(
                [
                    door_and_window.frame_face_thickness - door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.frame_face_thickness,
                    0.0
                ],
                [
                    door_and_window.width / 2 - door_and_window.frame_face_thickness,
                    door_and_window.parapet_wall_height + door_and_window.frame_face_thickness,
                    0.0
                ],
                [
                    door_and_window.width / 2 - door_and_window.frame_face_thickness,
                    door_and_window.parapet_wall_height + door_and_window.height -
                    door_and_window.frame_face_thickness,
                    0.0
                ],
                [
                    door_and_window.frame_face_thickness - door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height -
                    door_and_window.frame_face_thickness,
                    0.0
                ]
            ).apply_matrix(transformation_matrix),

            outside_left_jamb_wall=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    0.0
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    -door_and_window.outside_depth
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    -door_and_window.outside_depth
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    0.0
                ],
            ).apply_matrix(transformation_matrix),

            outside_right_jamb_wall=Quadrilateral(
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    0.0
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    -door_and_window.outside_depth],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height +
                    door_and_window.height,
                    -door_and_window.outside_depth
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    0
                ],
            ).apply_matrix(transformation_matrix),

            outside_head_jamb_wall=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    0.0
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    -door_and_window.outside_depth
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    -door_and_window.outside_depth
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    0.0
                ],
            ).apply_matrix(transformation_matrix),

            outside_stool=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    0.0
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    -door_and_window.outside_depth
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    -door_and_window.outside_depth],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    0.0
                ]
            ).apply_matrix(transformation_matrix),

            inside_left_jamb_wall=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.frame_thickness
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.frame_thickness
                ],
            ).apply_matrix(transformation_matrix),

            inside_right_jamb_wall=Quadrilateral(
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.frame_thickness
                ],
            ).apply_matrix(transformation_matrix),

            inside_head_jamb_wall=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.frame_thickness
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height +
                    door_and_window.height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height + door_and_window.height,
                    door_and_window.frame_thickness
                ],
            ).apply_matrix(transformation_matrix),

            inside_stool=Quadrilateral(
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.frame_thickness
                ],
                [
                    -door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.inside_depth + door_and_window.frame_thickness
                ],
                [
                    door_and_window.width / 2,
                    door_and_window.parapet_wall_height,
                    door_and_window.frame_thickness
                ]
            ).apply_matrix(transformation_matrix)
        )
