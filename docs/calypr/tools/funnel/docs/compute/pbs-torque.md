---
title: PBS/Torque
menu:
  main:
    parent: Compute
    weight: 20
---
# PBS/Torque

Funnel can be configured to submit workers to [PBS/Torque][pbs] by making calls
to `qsub`.

The Funnel server needs to run on a submission node.
Configure Funnel to use PBS by including the following config:

It is recommended to update the submit file template so that the
`funnel worker run` command takes a config file as an argument 
(e.g. `funnel worker run --config /opt/funnel_config.yml --taskID {% raw %}{{.TaskId}}{% endraw %}`)

```YAML
Compute: pbs

PBS:
    Template: |
    #!/bin/bash
    #PBS -N {{.TaskId}}
    #PBS -o {{.WorkDir}}/funnel-stdout
    #PBS -e {{.WorkDir}}/funnel-stderr
    {{if ne .Cpus 0 -}}
    {{printf "#PBS -l nodes=1:ppn=%d" .Cpus}}
    {{- end}}
    {{if ne .RamGb 0.0 -}}
    {{printf "#PBS -l mem=%.0fgb" .RamGb}}
    {{- end}}
    {{if ne .DiskGb 0.0 -}}
    {{printf "#PBS -l file=%.0fgb" .DiskGb}}
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

[pbs]: http://www.adaptivecomputing.com/products/open-source/torque/
