---
description: >-
  Requires a repository to declare one working language for everything it authors, attaches exceptions to specific text
  rather than files, and leaves the language and spelling variant to the adopter.
when_to_use: >-
  Use when choosing the language of authored text, localizing content, quoting another language, or settling a spelling
  variant in identifiers and prose.
---

# Working Language

A repository declares one working language, and everything it authors is written in it.

## What It Covers

Governance and contributor instructions, documentation, plans, specifications, source identifiers, comments and
docstrings, commit messages, pull-request titles and bodies, test names and descriptions, configuration labels, log and
error messages, and the output of the repository's own tools.

Contributors may converse in any language; agents answer in the language addressed. An English agent reply uses clear,
simple, natural words readers who learned English later can understand. Authored artifacts use the repository's working
language.

The line falls there because the audiences differ. A conversation has participants who chose its language. A committed
file has every future reader — maintainers years later, contributors who joined since, every agent that loads it as
context — and none of them chose.

## Why One

A second language anywhere in the authored corpus splits its readership: part of it can no longer review, search, or
maintain that part. The split hurts most where it is least visible, in a comment or an error message, because the reader
who needs it is holding a failing build rather than a translator.

## Exceptions Attach to Text

Another language is used only where observable context makes the text one of these:

| Exception               | Identified by                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| localized content       | a locale path, locale metadata, or an explicit audience declaration in its index              |
| user-facing translation | translation resources, locale fixtures, and test assertions quoting those strings             |
| language as the subject | a fixture proving other-language input is handled, or a term being defined                    |
| material wording        | a faithful quotation, a proper name, or regulated or domain terminology whose wording matters |
| third-party material    | vendored, imported, or generated content, or an external interface that dictates its strings  |
| extracted material      | notes or excerpts citing a source in another language, kept in that source's language         |

The exception belongs to the text, not to its file. A test asserting a translated string keeps its name, comments, and
surrounding explanation in the working language; only the quoted string is exempt. Where readers need it, quoted text
carries working-language context or a translation beside it.

Neither a contributor's preference nor a topic associated with a country or language is an exception. Documentation
about a regional regulation is written in the working language, even where it quotes the regulation.

## Translations

A translated document is deliberate: requested, kept current by someone committed to it, and never an automatic mirror,
which drifts from its original unnoticed. Original and translation link to each other.

## Two Adopter Decisions

### The Language

Most repositories choose English, and the reason is reach rather than preference: the dependencies, toolchains, error
messages, and issue trackers most contributors meet already use it, so it adds no language a contributor must learn. A
repository whose whole audience shares another language may choose that one, at the cost of excluding outside
contributors and any tooling that assumes English.

### The Spelling Variant

A language with regional spellings — `behaviour` or `behavior`, `colour` or `color` — either declares one variant for
the words the repository authors, or declares none.

| Option       | Gains                                                                         | Costs                                                                                   |
| ------------ | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| declare one  | a consistent, searchable corpus; identifiers and paths match without guessing | contributors who write the other variant are corrected in review                        |
| declare none | nothing to correct                                                            | a mixed corpus: a search for one spelling misses the other, and identifiers can diverge |

A declared variant governs only what the repository owns. A third-party identifier or API, a quotation, a URL, and a
proper name keep their own spelling.

## Enforcement

Language is checked in review, because a mechanical language detector misclassifies identifiers, names, quotations, and
deliberately localized text. A declared spelling variant is narrower, and an adopter can enforce it with its own word
check over the surfaces it maintains, exempting the categories above.
