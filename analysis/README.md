# Analysis

This directory contains reverse engineering analysis of EMGD binary components.

## Structure

- `emgd_drv/` — Xorg driver analysis (`/usr/lib/xorg/modules/drivers/emgd_drv.so`)
- `emgd_ko/` — Kernel module analysis (`~/intel-binaries-linux/drm/emgd.ko`)
- `mmio_traces/` — Hardware register traces captured from Windows driver

## Methodology

Each binary gets its own subdirectory with:

- `functions.md` — identified functions with offsets, inferred names, confidence level
- `structures.md` — identified data structures
- `notes.md` — general observations and hypotheses
- Ghidra project files (`.gpr`)

## Confidence Tagging

All findings use explicit confidence tags:

- **[CONFIRMED]** — verified by multiple sources
- **[INFERRED]** — logical conclusion from evidence
- **[SPECULATIVE]** — educated guess, needs verification
- **[UNKNOWN]** — insufficient information
