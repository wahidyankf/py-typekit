---
description: >-
  Requires honoured reduced-motion preferences, text or shape alongside colour for every state, meaningful image
  alternatives, link text that names its destination, and live announcements for dynamic content.
when_to_use: >-
  Use when adding an animation, a status indicator, an image, a link, or content that changes without a page load.
---

# Content, Motion, and Announcements

## Honour Reduced Motion

When a user's system requests reduced motion, remove or simplify animations and transitions. Slowing them is not enough,
because slow motion is still motion. People set that preference because movement on screen makes them unwell, and
ignoring it does real harm.

Never convey information by motion alone. Whatever an animation communicates is also available in a static form.

## State Is Never Colour Alone

Status, error, warning, and success states carry a text label or a distinct shape as well as colour. A coloured dot or
red text alone reaches some readers as nothing at all. A status badge pairs its colour with a label or an icon.

## Images Say What They Mean

- An informative image has a text alternative stating what it conveys, including any text inside the image that the
  surrounding content does not already give.
- A decorative image has an empty alternative so a screen reader skips it; the attribute is never simply left out.
- A complex chart or diagram has a text summary placed beside it or referenced from it.

## Links Name Their Destination

Link text says where the link goes, not that it can be clicked. A reader moving from link to link hears "View invoice
2025-001" and knows what it opens; "click here" repeated down a page tells them nothing.

## Dynamic Content Is Announced

Content that changes without a page load, such as a notification, a validation result, a progress update, or a set of
search results, sits in a live region so a screen reader announces the change.

Use a polite announcement for status that can wait until the user pauses. Reserve an assertive announcement, or an alert
role, for something that needs attention immediately, such as an error that blocks the current task. Announcing every
update assertively interrupts the user constantly, and they stop listening.
