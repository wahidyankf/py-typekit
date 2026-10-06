---
name: applying-diataxis-framework
description: >-
  Guides classifying a documentation page by the reader need it serves, recognizing content that drifted in from another
  mode, and splitting a mixed page into one primary page linked to the others.
when_to_use: >-
  Use when deciding which documentation mode a new page belongs to, or when an existing page seems to teach, instruct,
  describe, and explain at once.
compatibility: Requires read access to the documentation tree and its indexes.
---

# Applying the Diátaxis Framework

[Documentation Architecture][documentation-architecture] owns the four modes, the rule of one mode per page, and where
each mode lives. This skill covers the judgement of placing a real page, whose content seldom announces its mode.

## Ask What the Reader Is Doing

Classify by the reader's situation at the moment of reading, never by topic and never by what the author found
interesting. Two questions place most pages:

1. Is the reader **studying**, away from a task and building capability or understanding, or **working**, in the middle
   of a task and needing something now?
2. Does the reader need to **act**, or to **know**?

| Reader is | Needs to act | Needs to know |
| --------- | ------------ | ------------- |
| studying  | tutorial     | explanation   |
| working   | how-to guide | reference     |

When different sections of one page give different answers, the page is mixed.

Classification is per page. A directory named for a mode can still hold misfiled pages, so the directory is not evidence
of a page's mode.

## Signs of Drift

Read for passages that answer another quadrant's question:

- **tutorial** — Passage that does not belong: an aside offering a different route to another goal; Where it goes: a
  how-to guide, since it serves a reader's own goal
- **tutorial** — Passage that does not belong: a complete table of every available option; Where it goes: reference,
  linked from the step that uses one
- **how-to guide** — Passage that does not belong: several paragraphs on why the design has its shape; Where it goes:
  explanation, linked once
- **reference** — Passage that does not belong: a recommended order of steps; Where it goes: a how-to guide that links
  back to the entries used
- **explanation** — Passage that does not belong: numbered commands to run; Where it goes: a how-to guide or a tutorial

One stray sentence is a local edit. A section of them is a second page.

## Tutorials and How-To Guides Are Confused Most

Both contain steps, so steps prove nothing either way. The difference is who chose the goal. A tutorial's author chose
it in order to teach, and the learner follows without deciding anything. A how-to guide's reader arrives with a goal
already and wants the shortest reliable route to it.

To test a page, imagine every explanation removed. If the page still serves its reader, it is a how-to guide. If the
reader could now repeat the steps but never adapt them, it was a tutorial. [Tutorial Structure][tutorial-structure]
draws the same boundary for learning documents.

## Reference and Explanation Are Confused Next

Both describe. Reference describes the machinery exactly and neutrally, in a structure that mirrors the thing described,
so a reader can find one entry without reading the rest. Explanation describes it from a point of view: reasons,
history, alternatives, and consequences. A reference entry that argues is drifting toward explanation; an explanation
that lists every field is drifting the other way.

## Splitting a Mixed Page

Name the primary reader first: the one whose need the title and the inbound links promise. That mode's content stays.
Each passage serving another mode moves whole into a page of that mode, or into an existing page that already covers it,
and leaves behind a one-line link at the point where a reader would want it. Every directory that gains a page gets its
index updated.

Moving, not deleting, is what [Content Preservation][content-preservation] requires, and it also says how to show that
nothing was lost in the move.

## When No Mode Fits

A page that fits no mode is usually one of two things. It may be content whose canonical home lies outside
documentation, such as a governance rule or a project README, and the page should link there instead. Or it is notes
that are not yet a page. Neither earns a fifth mode.

[documentation-architecture]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/documentation-architecture.md
[tutorial-structure]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/tutorial-structure.md
[content-preservation]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/evidence/content-preservation.md
