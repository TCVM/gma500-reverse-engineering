# GMA500 RE Agent

## Context

Reverse engineering EMGD driver (Intel GMA500 / PowerVR SGX545) for modern Linux.
Read `docs/00-project-overview.md` at session start.
Read `logs/session-active.md` if it exists and summarize pending items.
Ask the user the session objective before starting.

## Signal Protocol

Emit signals on their own line before responding:

@@ESCALATE — needs Claude (complex architecture, undocumented hardware behavior)
@@CHECKPOINT — context degrading or session is long
@@DOCUMENT — important finding just occurred
@@CONFIRM — about to do something irreversible
@@UNKNOWN — cannot determine with available information

## Confidence Tags

Always tag claims about binaries or hardware:
[CONFIRMED] [INFERRED] [SPECULATIVE] [UNKNOWN]

## Key Files

- Kernel module: `~/intel-binaries-linux/drm/emgd.ko`
- Xorg driver: `/usr/lib/xorg/modules/drivers/emgd_drv.so`
- Active log: `logs/session-active.md`
- Glossary: `docs/03-glossary.md`

## Session Continuity

Each OpenCode session belongs to one working context.
When @@CHECKPOINT is emitted, the controller saves state to:
`logs/context-checkpoint-HHMM.md`

To continue in a new session:

1. Close this OpenCode session
2. Run `start.bat` again
3. Tell the new session: "lee logs/context-checkpoint-HHMM.md y continuá"

The controller automatically tags all logs with the session start time
so findings are always traceable to their session.
