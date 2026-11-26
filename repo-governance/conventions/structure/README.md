---
description: >-
  Indexes the structure conventions: how files, directories, and multi-document sets are shaped and named, how
  governance and plans are organized, and how repositories relate.
when_to_use: >-
  Use when naming a file, laying out a directory or repository, splitting a document, or shaping a plan.
---

# Structure Conventions

Structure conventions answer where something goes and what it is called, so a reader, human or agent, can predict a path
before opening it and a validator can check that prediction mechanically.

| Convention                                                  | Governs                                                                                  |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [Artifact Metadata](artifact-metadata.md)                   | frontmatter every governed artifact family carries                                       |
| [File Naming](file-naming.md)                               | naming files and directories, and splitting a document                                   |
| [Repository Configuration](repository-configuration.md)     | what a repository is and what must pass before a change lands                            |
| [Plans](plans.md)                                           | the plan system: lifecycle, documents, delivery, archival                                |
| [Plan Specification Changes](plan-specification-changes.md) | a plan's specification and architecture delta                                            |
| [Plan Migrations](plan-migrations.md)                       | preserving data and structure through a planned transition                               |
| [Plan UI Design](plan-ui-design.md)                         | a plan's interface exploration, assets, and device proof                                 |
| [Plan Content Corpora](plan-content-corpora.md)             | who may change a plan-authored content corpus, and where it ends up                      |
| [Capability Naming](capability-naming.md)                   | the scope-first grammar for agent and workflow names                                     |
| [CI Workflow File Naming](ci-workflow-file-naming.md)       | deriving a CI workflow's filename from its declared name                                 |
| [Command-Line Interface](command-line-interface.md)         | exit vocabulary, streams, and output a tool owes callers                                 |
| [Coordination Repository](coordination-repository.md)       | routing work to owning repositories without transferring ownership                       |
| [Directory Indexes](directory-indexes.md)                   | the README index of every indexed directory                                              |
| [Document Word Budget](document-word-budget.md)             | the instruction and governance document word ceiling, and repair                         |
| [Documentation Architecture](documentation-architecture.md) | where documentation lives and the one mode each page serves                              |
| [Governance Layers](governance-layers.md)                   | what each governance level answers and which wins a conflict                             |
| [Licensing](licensing.md)                                   | the root licensing model, exceptions, and dependency-license decisions                   |
| [Monorepo Layout](monorepo-layout.md)                       | dependency direction and project boundaries inside a monorepo                            |
| [Principle Traceability](principle-traceability.md)         | how each rule traces to the principles it implements                                     |
| [Project READMEs](project-readmes.md)                       | what a project's root README covers and leaves to its specification                      |
| [Related Repositories](related-repositories.md)             | parity, consumption, and knowledge-sharing relationships                                 |
| [Specification Tree](specification-tree.md)                 | one specification corpus per logical owner, fully specified for Gherkin, C4, and OpenAPI |
| [Stack Packs](stack-packs.md)                               | stack standard and skill paths, stack IDs, the inventory, and the repository adapter     |
| [Temporary Files](temporary-files.md)                       | where scratch files and reports go, and their naming and writing                         |
| [Workflow Pattern](workflow-pattern.md)                     | the contract, steps, checkpoints, and composition of a workflow document                 |

## Directory Map

- [Artifact Metadata](artifact-metadata.md)
- [Artifact Metadata Modules](artifact-metadata/README.md) — schemas by path, shared value rules, portable tiers and
  capabilities
- [File Naming](file-naming.md)
- [File Naming Modules](file-naming/README.md) — portable characters, dated and numbered names, and source filenames
- [Repository Configuration](repository-configuration.md)
- [Repository Configuration Modules](repository-configuration/README.md) — top-level schema, gate entries, surfaces and
  mutation, governance categories
- [Plans Convention](plans.md)
- [Plans Convention Modules](plans/README.md) — the modules, from lifecycle and required documents to the bug-fix plan
- [Plan Validator Contract](plan-validator-contract.md) — frozen inputs, rule identifiers, messages, and exit classes of
  plan-structure validation
- [Plan Validator Contract Modules](plan-validator-contract/README.md) — inputs and exits, rule identifiers, fixture
  corpus, exclusions
- [Plan Specification Changes](plan-specification-changes.md)
- [Plan Migrations](plan-migrations.md)
- [Plan Migrations Modules](plan-migrations/README.md) — source inventory and contracts, transition, and recovery
- [Plan UI Design](plan-ui-design.md)
- [Plan Content Corpora](plan-content-corpora.md)
- [Capability Naming](capability-naming.md)
- [CI Workflow File Naming](ci-workflow-file-naming.md)
- [Command-Line Interface](command-line-interface.md)
- [Command-Line Interface Modules](command-line-interface-details/README.md) — the seven interface modules
- [Coordination Repository](coordination-repository.md)
- [Directory Indexes](directory-indexes.md)
- [Document Word Budget](document-word-budget.md)
- [Documentation Architecture](documentation-architecture.md)
- [Governance Layers](governance-layers.md)
- [Licensing](licensing.md)
- [Licensing Modules](licensing/README.md) — the repository licensing model and dependency-license decisions
- [Monorepo Layout](monorepo-layout.md)
- [Principle Traceability](principle-traceability.md)
- [Project READMEs](project-readmes.md)
- [Related Repositories](related-repositories.md)
- [Specification Tree](specification-tree.md)
- [Stack Packs](stack-packs.md)
- [Stack Packs Modules](stack-packs/README.md) — the repository adapter template and inventory extension
- [Temporary Files](temporary-files.md)
- [Workflow Pattern](workflow-pattern.md)
- [Workflow Pattern Modules](workflow-pattern/README.md) — document contract, steps and state, checkpoints, composition,
  and execution
