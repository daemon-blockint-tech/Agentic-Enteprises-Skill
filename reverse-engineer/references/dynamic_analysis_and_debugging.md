# Dynamic analysis and debugging

## Table of contents

1. [Lab setup](#lab-setup)
2. [Execution workflow](#execution-workflow)
3. [Debugger practices](#debugger-practices)
4. [Instrumentation](#instrumentation)
5. [Platform notes](#platform-notes)
6. [Safety stops](#safety-stops)

## Lab setup

1. Use **dedicated VMs** or hardware lab VLAN with no route to production
2. Snapshot VM **before** each run; revert after session
3. Disable shared folders and clipboard unless required; use controlled sample transfer
4. For malware: **air-gapped or egress-filtered** network per policy; fake DNS/INetSim as approved
5. Log **who** ran **which** sample **when** for audit trail

Never execute unknown binaries on corporate endpoints or CI runners.

## Execution workflow

```
baseline → run under monitor → capture artifacts → correlate with static → document
```

- Record command line, working directory, and environment variables
- Capture **process tree**, loaded modules, handles, and exit code
- Collect **file system** and **registry** (Windows) or **plist** (macOS) deltas
- Log **network** (pcap, proxy) with timestamps aligned to debugger events
- Compare multiple runs if anti-analysis or timing checks exist

## Debugger practices

- Set breakpoints on **API hooks** (kernel32, ntdll, libc) after reaching interesting code
- Use **hardware breakpoints** on memory when software breakpoints alter packed code
- Step **out** of library noise; focus on module under analysis
- Dump **memory regions** when unpacking stages; re-base in static tool for stage-2
- Document **register and stack** context for crash reproduction in vuln writeups

For firmware: use JTAG/SWD only when hardware and authorization allow; document interface protections.

## Instrumentation

| Layer | Examples | Use when |
|---|---|---|
| API hooking | Frida, DynamoRIO | Trace arguments/returns quickly |
| Sandbox | Cuckoo, CAPE | Unattended behavior baseline |
| Emulation | QEMU, Unicorn | Snippet or algorithm isolation |
| Syscall trace | strace, ETW, Procmon | Low-level behavior proof |

Correlate traces back to **static addresses** after ASLR rebasing notes.

## Platform notes

- **Windows:** prefer x64dbg/WinDbg for user mode; note WOW64 and service contexts
- **Linux:** gdb + pwndbg/gef; respect ASLR, check seccomp/AppArmor
- **macOS:** lldb; SIP and notarization may limit attachment—stay authorized
- **Android/iOS:** use approved device images; respect MDM and legal constraints
- **Embedded:** serial console + gdbserver when available; otherwise emulate

## Safety stops

Stop and escalate when:

- Sample attempts **lateral movement** or encryption of lab shares
- C2 connects to **non-sinkhole** infrastructure without approval
- Analysis target is **production** system or customer tenant without scope
- User requests **live** debugging on employee machine without HR/legal clearance

Hand off containment to `incident-responder`; preservation to `digital-forensics-analyst` when legal-grade artifacts are needed.
