""" Test module for `EventHandler` class. """
from ...models.event_handler import EventHandler


def test_event_handler_class():
    """ Test for `EventHandler` class """
    event_handler = EventHandler()

    counter = 0
    event_args = 1

    def callback(args):
        nonlocal counter
        counter += 1
        assert args == event_args

    stop_listen = event_handler.listen(callback)

    assert counter == 0, 'callback should not be called until event fired'

    event_handler.fire(event_args)

    assert counter == 1, 'callback should be called when event fired'

    event_args = 2
    event_handler.fire(event_args)

    assert counter == 2, 'callback should be again called when event fired'

    stop_listen()

    assert counter == 2, 'callback should not be called when calling stop_listen'

    event_args = 3
    event_handler.fire(event_args)

    assert counter == 2, 'callback should not be called after not listening anymore'
