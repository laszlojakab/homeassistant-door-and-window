""" The module of event handling. """


from typing import Callable


class Event:
    """ Represents an event. """

    def __init__(self):
        """ Initialize a new instance of `Event` class."""
        self.__eventhandlers = []

    def add_listener(self, listener: Callable):
        """
        Adds an event listener to the event.
        The event listener will be called whenever the event invoked.
        """
        self.__eventhandlers.append(listener)
        return self

    def remove_listener(self, handler: Callable):
        """
        Removes an event listener from the event.
        """
        self.__eventhandlers.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        """
        Invokes the event and calls all the added event listeners.
        """
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **kwargs)

    def clear_event_listeners(self):
        """
        Removes all event listeneres.
        """
        self.__eventhandlers.clear()
