Feature: Attempt
  Attempt runs a call once and returns its value as Ok. A named exception becomes Err. Any other exception propagates.

  # Behaviour: PT-B09
  Scenario: attempt returns Ok when the call succeeds
    Given a call that returns 12
    When I attempt the call naming ValueError
    Then the outcome is Ok holding 12

  # Behaviour: PT-B10
  Scenario: attempt catches a named type and propagates any other
    Given a call that raises a ValueError
    When I attempt the call naming ValueError
    Then the outcome is an Err holding that ValueError
    Given a call that raises a KeyError
    When I attempt the call naming ValueError
    Then the call error propagates as a KeyError
