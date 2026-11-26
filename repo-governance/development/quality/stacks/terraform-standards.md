---
description: >-
  Fixes the Terraform baseline: format, validate, and lint gates; typed, described variables; pinned versions and a
  committed lock file; no state or secret variable files in history; native tests plus plan review.
when_to_use: >-
  Use when creating, configuring, or reviewing a Terraform module or root configuration, or deciding how to verify an
  infrastructure change before apply.
---

# Terraform Standards

Canonical for the choices Terraform leaves open; a Terraform skill defers here per rule. Infrastructure and hosts only:
development environments follow [Native-First Toolchain](../../workflow/native-first-toolchain.md), never Terraform.

It implements [Reproducibility](../../../principles/reproducibility.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Fail Closed](../../../principles/fail-closed.md), and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Gates

- **Formatting:** `terraform fmt -check -recursive` fails on any file it would rewrite.
- **Validation:** `terraform validate` over every root and module proves only syntax and consistency, never correctness
  ([validate](https://developer.hashicorp.com/terraform/cli/commands/validate)).
- **Lint:** Terraform ships none, so a third-party linter with provider rule sets, such as TFLint, runs at the
  [Lint Strictness](../checks/lint-strictness.md) threshold
  ([style guide](https://developer.hashicorp.com/terraform/language/style)).

## Type and Boundary Safety

Terraform's mapping of [Type and Boundary Safety](../code/type-and-boundary-safety.md):

- Every variable declares `type` and `description`; `type = any` carries an inline reason.
- A variable narrower than its type has a `validation` block whose error message states the rule
  ([variables](https://developer.hashicorp.com/terraform/language/values/variables)).
- Resource and data source assumptions are a `precondition` or `postcondition`. A `check` block only warns, so never use
  it where the run must stop ([validate configuration](https://developer.hashicorp.com/terraform/language/validate)).

They run at plan time, so never present them as static-type guarantees.

## Versions and State

- `required_version` bounds the binary, `required_providers` pins each provider's source and version, and module calls
  pin versions. Commit `.terraform.lock.hcl`; upgrades follow
  [Dependency Bump Policy](../../workflow/dependency-bump-policy.md).
- Never commit state files or backups, `.terraform`, or secret-holding variable files; state lives in the adopter's
  recorded backend.
- State stores `sensitive` values in plaintext, hiding them only from output, so reading state is secret access. A value
  that must never persist is declared ephemeral.
- Secrets, hosts, and addresses follow
  [No Secrets in Tracked Files](../../../conventions/security/no-secrets-in-tracked-files.md) and
  [No Machine-Specific Values](../../../conventions/security/no-machine-specific-values.md).

## Code Shape

- A renamed or relocated resource declares `moved`, so the plan shows a move, not destroy and create
  ([refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring)).
- A reusable module takes environment values as variables; only root configurations hold them.

## Tests

[Test-Driven Development](../testing/test-driven-development.md) applies without exemption, through native
[tests](https://developer.hashicorp.com/terraform/language/tests):

- Module behaviour (input validation, conditional resources, outputs) starts from a failing `terraform test` run block.
  A `command = plan` run with mocked providers is the unit layer; a default run, which applies then destroys real
  resources, is the integration layer.
- Each rejected input has a run block naming it in `expect_failures`.
- Plan review verifies a root configuration change: expected changes are written first, the saved plan must show exactly
  those (an unexpected replacement or destruction fails), and that reviewed plan file is applied.

Layers and gates follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Per
[Meaningful Coverage](../testing/meaningful-coverage.md), Terraform has no numeric coverage: no instrument measures its
declarative code ([discussion](https://github.com/hashicorp/terraform/issues/37605)). Never report a surrogate such as
the share of resources with a test.

## Documentation

Every variable and output has a description; a module README states its inputs, outputs, and required providers. A
module interface change is a contract change under [Public Contract](../architecture/public-contract.md) and
[Specification Maintenance](../evidence/specification-maintenance.md).

## Adopter Decision

The [Stack Packs](../../../conventions/structure/stack-packs.md) repository adapter records whether integration runs
exist, against a dedicated test account, or verification stops at mocked plan-mode runs and plan review. Real runs prove
provider behaviour but cost spend, credentials, and failed-run cleanup.

## Enforcement

Adopters enforce format, validate, lint, and plan-mode tests in the pull-request gate, keeping apply-mode tests out of
every hook. Applying a plan is a deployment, never a gate side effect. Review covers typing, version pins, state and
secret handling, and plan review.
