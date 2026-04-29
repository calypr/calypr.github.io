---
title: Overview
menu:
  main:
    identifier: docs
    weight: -1000
---

# Overview

Funnel makes distributed batch processing easier by providing a simple task API and a set of
components which can easily adapted to a vareity of platforms.

### Task

A task defines a unit of work: metadata, input files to download, a sequence of Docker containers + commands to run,
output files to upload, state, and logs. The API allows you to create, get, list, and cancel tasks.

Tasks are accessed via the `funnel task` command. Additionally the HTTP API is based on a standarized GA4GH
protocol, and any client the is compatible with that API will work with Funnel.

There's a lot more you can do with the task API. See the [tasks docs](./tasks.md) for more.

### Server

The server serves the task API, web dashboard, and optionally runs a task scheduler.
It serves both HTTP/JSON and gRPC/Protobuf.

### Storage

Storage provides access to file systems such as S3, Google Storage, and local filesystems.
Tasks define locations where files should be downloaded from and uploaded to. Workers handle
the downloading/uploading.

See the [storage docs](./storage/index.md) for more information on configuring storage backends.

### Worker

A worker is reponsible for executing a task. There is one worker per task. A worker:

- downloads the inputs
- runs the sequence of executors (usually via Docker)
- uploads the outputs

Along the way, the worker writes logs to event streams and databases:

- start/end time
- state changes (initializing, running, error, etc)
- executor start/end times
- executor exit codes
- executor stdout/err logs
- a list of output files uploaded, with sizes
- system logs, such as host name, docker command, system error messages, etc.

The worker is accessible via the `funnel worker` command.

### Node Scheduler

A node is a service that stays online and manages a pool of task workers. A Funnel cluster
runs a node on each VM. Nodes communicate with a Funnel scheduler, which assigns tasks
to nodes based on available resources. Nodes handle starting workers when for each assigned
task.

Nodes aren't always required. In some cases it often makes sense to rely on an existing,
external system for scheduling tasks and managing cluster resources, such as AWS Batch
or HPC systems like HTCondor, Slurm, Grid Engine, etc. Funnel provides integration with
these services that doesn't include nodes or scheduling by Funnel.

See [Deploying a cluster](./compute/deployment.md) for more information about running a cluster of nodes.

The node is accessible via the `funnel node` command.