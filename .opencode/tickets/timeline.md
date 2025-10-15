# Emukit Ticket Timeline

Date: 2025-10-14

## Overview
This timeline tracks progress on optional dependency refactoring, test gating efforts, and newly discovered compatibility issues.

## Tickets

### Ticket 023 – DoE Dependencies Consolidation
- Status: Completed.
- Outcome: Moved PyDOE & sobol_seq to mandatory core requirements; removed from extras to simplify installation and avoid conditional failures.

### Ticket 022 – Marker Expansion (sklearn & Notebooks)
- Status: Completed.
- Outcome: Added `sklearn` and `notebooks` markers to setup.cfg. Annotated sklearn integration tests with `pytestmark = pytest.mark.sklearn` while retaining existing `pytest.importorskip("sklearn")`. Added `pytestmark = pytest.mark.notebooks` to notebook execution test and de-duplicated redundant `importorskip` calls. Timeline & gating summary updated.


### Ticket 001 – Optional Dependency Extras
- Status: Completed.
- Outcome: Extras defined (`gpy`, `examples`, `docs`, `tests`, `full`); benchmarking extra removed.

### Ticket 002 – GPy Import Gating
- Status: Completed.
- Outcome: Core import works without GPy; placeholders added; informative errors preserved.

### Ticket 003 – Test Gating (GPy)
- Status: Completed.
- Outcome: All GPy-dependent unit tests now uniformly use `pytest.importorskip("GPy")` plus `pytestmark = pytest.mark.gpy`. No remaining ungated GPy imports found. Non-GPy test (mean plugin EI) confirmed does not require GPy and stays unmarked.

### Ticket 007 – BenchmarkPlot Matplotlib Handling
- Status: Completed.
- Outcome: Added guarded matplotlib import with `_HAS_MPL` flag, placeholder `BenchmarkPlot` raising informative ImportError when matplotlib absent, fixed `save_plot` to use `fig_handle.savefig(file_name)` and corrected error message, tests now skipped if matplotlib not installed.

### Ticket 014 – GPy Marker Introduction & Integration Stability
- Status: Completed.
- Outcome: Established `gpy` marker taxonomy and applied consistently across GPy tests. Extended marker framework (`pybnn`, `sklearn`, `notebooks`) and removed now-unnecessary `mpl` marker after promoting matplotlib to mandatory dependency.

### Ticket 021 – NumPy 2.0 Compatibility
- Status: Completed.
- Outcome: Replaced deprecated aliases (`np.product` -> `np.prod`; removed legacy `np.int` -> `int` in examples). Verified absence of `np.NaN`, `np.PINF`, `np.NINF`, `np.row_stack`. Adjusted test mocking to avoid NumPy 2.x recursion.

## Dependency Gating Summary
- Implemented: GPy (marker), matplotlib (mandatory), pybnn (marker), sklearn (marker), notebooks (marker for nbformat/nbconvert execution), nbformat, nbconvert.
- Pending: Review whether to convert notebooks execution to a slower test group marker or leave as is.


## Next Action Plan
1. Run pytest to confirm marker-based skips in minimal env.
2. Document marker usage in CONTRIBUTING and optionally CHANGELOG.
3. Evaluate need for a slow/extended marker to group notebook execution.

## Risks
- Leaving NumPy 2.0 issues blocks future CI matrix updates targeting modern environments.
- Missing matplotlib import hides plotting capability and creates failing tests.

## Open Decisions
- Marker taxonomy breadth.

## Milestones
- 2025-10-14: Discovered NumPy 2.0 incompatibilities and benchmark plot import issue; timeline & Ticket 021 created.

---
End of timeline update.
