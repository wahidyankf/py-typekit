Feature: Pipe
  Pipe applies its functions from left to right, each one to the result of the one before.

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_pipeline.py
  @integration-exempt
  # Behaviour: PT-B11
  Scenario: pipe runs nine stages from left to right
    Given the text "start"
    When I pipe the text through nine stages that each add one letter
    Then the outcome is "startabcdefghi"
