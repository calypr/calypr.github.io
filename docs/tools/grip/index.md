---
title: GRIP
---

GRIP (Graph Resource Integration Platform) is a powerful framework for building and managing distributed data processing systems. Key features include:

- **Distributed Computing**: Scalable processing across multiple nodes.
- **Database Integration**: Built-in support for MongoDB, PostgreSQL, and SQL databases.
- **API Endpoints**: RESTful APIs for managing data workflows and monitoring.
- **Flexible Query Language**: GRIPQL for complex data queries and transformations.
- **Job Management**: Schedule, monitor, and manage data processing jobs in real-time.


<!-- termynal -->
```
# Start server
$ grip server --config grip.yml

# List all graphs
$ grip list

# Create a graph
$ grip create example

# Drop a graph
$ grip drop example

# Load data into a graph
$ grip load example --edge edges.txt --vertex vertices.txt

# Query a graph
$ grip query example 'V().hasLabel("users")'

#Get vertex/edge counts for a graph
$ grip info example

# Get the schema for a graph
$ grip schema get example

# Dump vertices/edges from a graph
$ grip dump example --vertex
```