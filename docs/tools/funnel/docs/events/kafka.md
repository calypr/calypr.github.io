---
title: Kafka
menu:
  main:
lead: "Funnel supports writing task events to a Kafka topic."
personas:
  - platform-engineer
  - workflow-engineer
solutions:
  - manage-compute
related_tools:
  - funnel
---

# Kafka

Funnel supports writing task events to a Kafka topic. To use this, add an event
writer to the config:

```yaml
EventWriters:
  - kafka
  - log

Kafka:
  Servers:
    - localhost:9092
  Topic: funnel-events
```
