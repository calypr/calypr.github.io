---
title: Prometheus
menu:
  main:
lead: "[Prometheus][prom] is a monitoring and metrics collection service."
personas:
  - platform-engineer
  - workflow-engineer
solutions:
  - manage-compute
related_tools:
  - funnel
---

# Prometheus

[Prometheus][prom] is a monitoring and metrics collection service. It pulls metrics
from various "exporters", collects them in a time-series database, provides
a query langauge for access that data, and integrates closely with tools
such as [Grafana][graf] for visualization and dashboard building.

Funnel exports these metrics:

- `funnel_tasks_state_count`: the number of tasks
  in each state (queued, running, etc).
- `funnel_nodes_state_count`: the number of nodes
  in each state (alive, dead, draining, etc).
- `funnel_nodes_total_cpus`: the total number
  of CPUs available by all nodes.
- `funnel_nodes_total_ram_bytes`: the total number
  of bytes of RAM available by all nodes.
- `funnel_nodes_total_disk_bytes`: the total number
  of bytes of disk space available by all nodes.
- `funnel_nodes_available_cpus`: the available number
  of CPUs available by all nodes.
- `funnel_nodes_available_ram_bytes`: the available number
  of bytes of RAM available by all nodes.
- `funnel_nodes_available_disk_bytes`: the available number
  of bytes of disk space available by all nodes.

[prom]: https://prometheus.io/
[graf]: https://grafana.com/
