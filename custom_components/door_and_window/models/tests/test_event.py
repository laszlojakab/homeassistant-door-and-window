""" Test module for Event class. """
from ..event import Event


def test_event_class():
    """
    Test of the `Event` class.
    """
    event = Event()

    event_fired_counter = 0

    def increase_event_count():
        nonlocal event_fired_counter
        event_fired_counter += 1

    event.add_listener(increase_event_count)
    assert event_fired_counter == 0, "event shouldn't be fired after adding listener"

    event()
    assert event_fired_counter == 1, "event be registered 1st in event listener"

    event()
    assert event_fired_counter == 2, "event be registered 2nd time in event listener"

    event.remove_listener(increase_event_count)

    event()
    assert event_fired_counter == 2, \
        "event must not be registered in event listener if event listener was removed"

def test_event_clear_event_listeners():
    """
    Test of the `Event.clear_event_listeners` method.
    """
    event = Event()

    event_fired_counter = 0

    def increase_event_count():
        nonlocal event_fired_counter
        event_fired_counter += 1

    event.add_listener(increase_event_count)
    assert event_fired_counter == 0, "event shouldn't be fired after adding listener"

    event()
    assert event_fired_counter == 1, "event be registered 1st in event listener"

    event()
    assert event_fired_counter == 2, "event be registered 2nd time in event listener"

    event.clear_event_listeners()

    event()
    assert event_fired_counter == 2, \
        "event must not be registered in event listener if event listeners were cleared"
