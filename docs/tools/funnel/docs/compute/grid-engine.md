---
title: Grid Engine
menu:
  main:
    parent: Compute
    weight: 20
---
# Grid Engine

Funnel can be configured to submit workers to [Grid Engine][ge] by making calls
to `qsub`.

The Funnel server needs to run on a submission node.
Configure Funnel to use Grid Engine by including the following config:

It is recommended to update the submit file template so that the
`funnel worker run` command takes a config file as an argument
(e.g. `funnel worker run --config /opt/funnel_config.yml --taskID {{.TaskId}}`)

```YAML
Compute: gridengine

GridEngine:
  Template: |
    #!/bin/bash
    #$ -N {{.TaskId}}
    #$ -o {{.WorkDir}}/funnel-stdout
    #$ -e {{.WorkDir}}/funnel-stderr
    {{if ne .Cpus 0 -}}
    {{printf "#$ -pe mpi %d" .Cpus}}
    {{- end}}
    {{if ne .RamGb 0.0 -}}
    {{printf "#$ -l h_vmem=%.0fG" .RamGb}}
    {{- end}}
    {{if ne .DiskGb 0.0 -}}
    {{printf "#$ -l h_fsize=%.0fG" .DiskGb}}
    {{- end}}

    funnel worker run --taskID {{.TaskId}}
```
The following variables are available for use in the template:

| Variable    |  Description |
|:------------|:-------------|
|TaskId       | funnel task id |
|WorkDir      | funnel working directory |
|Cpus         | requested cpu cores |
|RamGb        | requested ram |
|DiskGb       | requested free disk space |
|Zone         | requested zone (could be used for queue name) |

See https://golang.org/pkg/text/template for information on creating templates.

[ge]: http://gridscheduler.sourceforge.net/documentation.html
