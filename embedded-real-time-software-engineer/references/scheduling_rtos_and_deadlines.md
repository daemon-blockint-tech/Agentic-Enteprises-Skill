# Scheduling, RTOS, and deadlines

## Table of contents

1. [Task model](#task-model)
2. [Priorities and policies](#priorities-and-policies)
3. [Periods, deadlines, jitter](#periods-deadlines-jitter)
4. [Synchronization](#synchronization)
5. [Schedulability sketch](#schedulability-sketch)

## Task model

For each task/thread document:

| Field | Purpose |
|---|---|
| Name | Stable identifier in traces |
| Priority | Numeric order; tie-break rules |
| Period / activation | Periodic, sporadic, or event-driven |
| Deadline | Relative or absolute; hard vs soft |
| WCET budget | Upper bound used in analysis |
| Stack size | Measured + margin |
| Shared resources | Mutexes, buses, DMA channels |

Keep **ISR work** out of task tables—reference IRQ budget separately.

## Priorities and policies

- Assign **rate-monotonic** or **deadline-monotonic** baselines for periodic tasks; justify exceptions
- Reserve **highest** priority for shortest-deadline control loops only when measured necessary
- Avoid **priority inversion** by design—document every cross-priority lock
- Use **time-slicing** sparingly on hard RT paths; prefer cooperative or dedicated cores
- On SMP: pin tasks, isolate shared caches, or partition peripherals per core

RTOS pattern notes (not API-specific):

- **FreeRTOS**: priority inheritance on mutexes; config `configMAX_PRIORITIES`, tickless idle impacts jitter
- **Zephyr**: preemptive threads, work queues, k_mutex priority ceiling; device init levels affect boot order

## Periods, deadlines, jitter

| Term | Definition |
|---|---|
| **Period** | Time between activations |
| **Deadline** | Latest acceptable completion |
| **Jitter** | Variation in start or finish time |
| **Slack** | Deadline − (release + WCET) |

Capture **end-to-end chains** (sensor → filter → actuate) with budget per segment.

For soft RT: define degraded mode when slack exhausted (drop frames, reduce rate).

## Synchronization

| Mechanism | Use when | Caution |
|---|---|---|
| Mutex + PI | Protect shared structured state | Hold time must be bounded |
| Semaphore | Signaling, counting resources | Not for mutual exclusion alone |
| Message queue | Task-to-task data transfer | Copy cost, depth sizing |
| Event flags | Lightweight wake | Thundering herd |
| Lock-free ring | ISR → task streaming | Requires memory ordering proof |

**Never** block inside ISR except documented RTOS FromISR APIs with bounded time.

## Schedulability sketch

For periodic task set (simplified RMS check):

1. List tasks sorted by period ascending
2. Assign priorities accordingly unless safety overrides
3. For each task \(i\), compute utilization \(U_i = C_i / T_i\)
4. Sum \(U = \sum U_i\); compare to RMS bound or use response-time analysis for shared resources
5. Add **interrupt load** and **driver DMA** as equivalent utilization or blocking terms

Document **unverified** segments explicitly; schedule measurement before claiming hard guarantees.
