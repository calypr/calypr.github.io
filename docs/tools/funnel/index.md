---
title: Funnel
---

## Funnel Tool Documentation

The Funnel tool is designed to streamline data processing workflows, enabling efficient data transformation and analysis. Key features include:

- **S3 Integration**: Seamlessly add and manage files from Amazon S3.
- **Data Transformation**: Predefined pipelines for common data processing tasks.
- **Automation**: Schedule and automate repetitive data workflows.
- **Monitoring**: Track the status and performance of data jobs in real-time.
- **Workflow engine compatibile**: Compatible with Nextflow

## Simple API
A task describes metadata, state, input/output files, resource requests, commands, and logs.

The task API has four actions: create, get, list, and cancel.

Funnel serves both HTTP/JSON and gRPC/Protobuf.

##Standards based

The Task API is developed via an open standard effort.

## Workers
Given a task, Funnel will queue it, schedule it to a worker, and track its state and logs.

A worker will download input files, run a sequence of Docker containers, upload output files, and emits events and logs along the way.

## Cross platform
We use Funnel on AWS, Google Cloud, OpenStack, and the good ol' university HPC cluster.

## Adaptable

A wide variety of options make Funnel easily adaptable:

 - BoltDB
 - Elasticsearch
 - MongoDB
 - AWS Batch, S3, DynamoDB
 - OpenStack Swift
 - Google Cloud Storage, Datastore
 - Kafka
 - HPC support: HTCondor, Slurm, etc.
 - and more

 ---

# Define a task

A task describes metadata, state, input/output files, resource requests, commands, and logs.

For a full description of the task fields, see the task API docs and the the task schema.

<!-- termynal -->
```
$ funnel examples hello-world
{
  "name": "Hello world",
  "description": "Demonstrates the most basic echo task.",
  "executors": [
    {
      "image": "alpine",
      "command": ["echo", "hello world"],
    }
  ]
}
```

---

# Start a Funnel server

localhost:8000 is the HTTP API and web dashboard.
localhost:9090 is the gRPC API (for internal communication)

<!-- termynal -->
```
$ funnel server run
server               Server listening
httpPort             8000
rpcAddress           :9090
```


---

# Create a task

The output is the task ID.

This example uses the development server, which will run the task locally via Docker.

<!-- termynal -->
```
$ funnel examples hello-world > hello-world.json
$ funnel task create hello-world.json
b8581farl6qjjnvdhqn0
```

---

# Get the task

The output is the task with state and logs.

By default, the CLI returns the "full" task view, which includes all logs plus stdout/err content.

<!-- termynal -->
```
$ funnel task get b8581farl6qjjnvdhqn0
{
  "id": "b8581farl6qjjnvdhqn0",
  "state": "COMPLETE",
  "name": "Hello world",
  "description": "Demonstrates the most basic echo task.",
  "executors": [
    {
      "image": "alpine",
      "command": [
        "echo",
        "hello world"
      ],
    }
  ],
  "logs": [
    {
      "logs": [
        {
          "startTime": "2017-11-13T21:35:57.548592769-08:00",
          "endTime": "2017-11-13T21:36:01.871905687-08:00",
          "stdout": "hello world\n"
        }
      ],
      "startTime": "2017-11-13T21:35:57.547408797-08:00",
      "endTime": "2017-11-13T21:36:01.87496482-08:00"
    }
  ],
  "creationTime": "2017-11-13T21:35:57.543528992-08:00"
}
```

---

List the tasks

<!-- termynal -->
```
$ funnel task list --view MINIMAL
{
  "tasks": [
    {
      "id": "b8581farl6qjjnvdhqn0",
      "state": "COMPLETE"
    },
    ...
  ]
}
```

---

# Quickly create tasks

The "run" command makes it easy to quickly create a task. By default, commands are wrapped in "sh -c" and run in the "alpine" container.

Use the "--print" flag to print the task instead of running it immediately.

<!-- termynal -->
```
$ funnel run 'md5sum $src' --in src=~/src.txt --print
{
  "name": "sh -c 'md5sum $src'",
  "inputs": [
    {
      "name": "src",
      "url": "file:///Users/buchanae/src.txt",
      "path": "/inputs/Users/buchanae/src.txt"
    }
  ],
  "executors": [
    {
      "image": "alpine",
      "command": [
        "sh",
        "-c",
        "md5sum $src"
      ],
      "env": {
        "src": "/inputs/Users/buchanae/src.txt"
      }
    }
  ],
}

```
