Feature: Option
  An absent value is None and a present value is Some. Option functions act on a Some and pass absence through.

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_option.py
  @integration-exempt
  # Behaviour: PT-B06
  Scenario: from_optional keeps absence and wraps a value
    Given the raw value is missing
    When I wrap the raw value with from_optional
    Then the outcome is absent
    Given the raw value is 0
    When I wrap the raw value with from_optional
    Then the outcome is Some holding 0

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_option.py
  @integration-exempt
  # Behaviour: PT-B07
  Scenario: option.map and option.flat_map act only on a Some
    Given a Some holding 2
    When I map it with option.map and a function that adds 1
    Then the outcome is Some holding 3
    Given a Some holding 2
    When I flat map it with option.flat_map and a step that doubles into a Some
    Then the outcome is Some holding 4
    Given an absent option
    When I map it with option.map and a function that adds 1
    Then the outcome is absent

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_option.py
  @integration-exempt
  # Behaviour: PT-B08
  Scenario: ok_or turns a Some into Ok and absence into Err
    Given a Some holding 2
    When I apply option.ok_or with the error "missing"
    Then the outcome is Ok holding 2
    Given an absent option
    When I apply option.ok_or with the error "missing"
    Then the outcome is Err holding "missing"
