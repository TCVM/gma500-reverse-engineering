# GMA500 RE Agent

## Context

Reverse engineering EMGD driver (Intel GMA500 / PowerVR SGX545) for modern Linux.
Read `docs/00-project-overview.md` at session start.
Read `logs/session-active.md` if it exists and summarize pending items.
Ask the user the session objective before starting.

## Signal Protocol

Emit signals on their own line before responding.
Always follow the signal with a plain language explanation of what triggered it.

@@ESCALATE:CRITICAL — needs Claude, stop and wait for response
@@ESCALATE:QUESTION — needs Claude, continue working while waiting
@@CHECKPOINT:AUTO — context degraded, save state and request new session
@@CHECKPOINT:MANUAL — session is long, suggest checkpoint to user
@@DOCUMENT — important finding, log it and continue
@@CONFIRM — about to do something irreversible, stop and wait
@@UNKNOWN:ANALYSIS — don't know what something is, log it and continue
@@UNKNOWN:ACTION — don't know if action is safe, stop immediately

## Unknown Action Rule

If you are about to modify, execute, or write anything and are not certain
it is safe: emit @@UNKNOWN:ACTION and stop. Do not proceed under any circumstance.
Wait for explicit user confirmation.

## Confidence Tags

Always tag claims: [CONFIRMED] [INFERRED] [SPECULATIVE] [UNKNOWN]

## Session Continuity

When @@CHECKPOINT:AUTO is emitted, the controller saves state to:
`logs/context-checkpoint-HHMM.md`
To continue: close session, run `start.bat`, load the checkpoint file.

## Key Files

- Kernel module: `~/intel-binaries-linux/drm/emgd.ko`
- Xorg driver: `/usr/lib/xorg/modules/drivers/emgd_drv.so`
- Active log: `logs/session-active.md`
- Glossary: `docs/03-glossary.md`
