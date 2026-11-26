Feature: Result
  An Ok holds a value and an Err holds a fault. Each combinator acts on its own side and passes the other side on.

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_result.py
  @integration-exempt
  # Behaviour: PT-B01
  Scenario: Ok maps its value
    Given an Ok holding 2
    When I map it with a function that adds 1
    Then the outcome is Ok holding 3

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_result.py
  @integration-exempt
  # Behaviour: PT-B02
  Scenario: Err map leaves its error unchanged
    Given an Err holding "boom"
    When I map it with a function that adds 1
    Then the outcome is Err holding "boom"

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_result.py
  @integration-exempt
  # Behaviour: PT-B03
  Scenario: Flat map chains an Ok and keeps an Err
    Given an Ok holding 2
    When I flat map it with a step that doubles the value into an Ok
    Then the outcome is Ok holding 4
    Given an Err holding "boom"
    When I flat map it with a step that doubles the value into an Ok
    Then the outcome is Err holding "boom"

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_result.py
  @integration-exempt
  # Behaviour: PT-B04
  Scenario: Tap and tap err see their own side
    Given an Ok holding 2
    When I tap it with a recording action
    Then the outcome is Ok holding 2
    And the action saw 2
    Given an Err holding "boom"
    When I tap its fault with a recording action
    Then the outcome is Err holding "boom"
    And the action saw "boom"

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_result.py
  @integration-exempt
  # Behaviour: PT-B05
  Scenario: Curried functions transform only their own side
    Given an Ok holding 2
    When I apply result map err with a function that adds an exclamation mark
    Then the outcome is Ok holding 2
    Given an Err holding "boom"
    When I apply result map err with a function that adds an exclamation mark
    Then the outcome is Err holding "boom!"
    Given an Ok holding 2
    When I apply result flat map err with a step that recovers as Ok 0
    Then the outcome is Ok holding 2
    Given an Err holding "boom"
    When I apply result flat map err with a step that recovers as Ok 0
    Then the outcome is Ok holding 0
    Given an Ok holding 2
    When I apply result tap err with a recording action
    Then the outcome is Ok holding 2
    And the action saw nothing
    Given an Err holding "boom"
    When I apply result tap err with a recording action
    Then the outcome is Err holding "boom"
    And the action saw "boom"
