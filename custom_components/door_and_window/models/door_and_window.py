""" The module contains the DoorAndWindow class. """
class DoorAndWindow():
    """ Represents a door and window object. """

    def __init__(
        self,
        # pylint: disable=redefined-builtin
        type: str,
        name: str,
        manufacturer: str,
        model: str,
    ):
        """
        Initialize a new instance of DoorAndWindow class

        Args:
            type:
                The type of door and window. Possible values: "door", "window"
            name: str
                The name of the door and window.
            manufacturer: str
                The manufacturer of the door and window.
            model: str
                The model of the door and window.
        """
        self._type = type
        self._name = name
        self._manufacturer = manufacturer
        self._model = model

    @property
    def type(self) -> str:
        """ Gets or sets the type of the door and window. """
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value

    @property
    def name(self) -> str:
        """ Gets or sets the name of the door and window. """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def manufacturer(self) -> str:
        """ Gets or sets the manufacturer of the door and window. """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        self._manufacturer = value

    @property
    def model(self) -> str:
        """ Gets or sets the model of the door and window. """
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value
