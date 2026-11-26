Feature: Exports
  The typekit package lists its public names in __all__.

  # Exemption(integration): the library has no local resource; alternative-proof: tests/test_behaviour_exports.py
  @integration-exempt
  # Behaviour: PT-B12
  Scenario: the package exports exactly ten names
    Given the typekit package is imported
    Then the package lists exactly the ten public names
    And option and result are reached as modules
