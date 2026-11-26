---
description: >-
  Bounds the exception for proceeding without a pipeline result when the pipeline itself is unavailable, and fixes how
  toolchain drift across a runner pool is found and closed in the shared setup.
when_to_use: >-
  Use when continuous integration did not run, was cancelled, or failed identically everywhere, when one runner fails a
  job the other runners pass, or before adding a runner to a pool.
---

# Pipeline Availability

The rule governs a failure the pipeline reports. A pipeline that is unavailable reports nothing about the change, and a
narrow exception covers that case. It is not a licence to proceed on a red or missing result, and every use satisfies
all of the following.

1. **Establish the signature; never assume it.** Typical shapes: a run cancelled midway with its retry stuck waiting; no
   run created at all for the commit, consistent with an event-delivery outage; one generic failure across many
   unrelated jobs, traced to a shared setup step the change did not touch, in a workflow that passed recently on the
   same branch.
2. **Verify the external cause live, every time.** Check the provider's status source or the runner pool's health
   immediately before deciding. An outage seen an hour earlier may be over, and a pool healthy an hour earlier may not
   be; a conclusion from an earlier check is never reused.
3. **Confirm the higher-value review still happened.** The exception replaces only the pipeline confirmation. Review of
   the change is a separate layer, and it is never skipped to work around the first.
4. **Bypass no enforced required check.** Where branch protection requires the pipeline result, the exception does not
   apply. Overriding that protection is a separate administrative decision with its own authority.
5. **Record the instance.** The signature, the live verification performed, and why the decision holds this time. Each
   use is its own decision, never a standing policy inferred from an earlier one.

## Persistent Is Not Operational

A runner or provisioning failure that persists across unrelated changes, instead of clearing by itself, stops being
covered once it is seen to persist. It becomes an ordinary infrastructure defect: filed, owned, fixed, and not bypassed
again.

## Toolchain Drift Across a Runner Pool

Pipeline runners that share one setup can pass every job while that setup is incomplete, because each existing runner
already has, from some earlier manual install, a tool the setup never provides. The gap surfaces only when a job lands
on a runner without that history.

- **Adding a runner to a pool exercises the shared setup.** A job that then fails on the new runner has found a gap in
  the setup, not a broken runner.
- **A missing tool is added to the shared setup.** Installing it inside one job or directly on one runner keeps the
  runners unequal and moves the failure to whichever runner is provisioned next.
- **Pipeline health is checked for each named runner.** A pool-wide total can read healthy while one runner cannot
  build.
- **A target satisfied from a cache has not run.** A long green history can reflect a warm cache. When a failure appears
  that the change could not have caused, confirm whether that job had been replaying cached results.
