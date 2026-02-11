---
title: Kubernetes
menu:
  main:
    parent: Compute
    weight: 20
---

> Funnel on Kubernetes is in active development and may involve frequent updates

# Quick Start

## 1. Deploying with Helm

```sh
helm repo add ohsu https://ohsu-comp-bio.github.io/helm-charts
helm repo update
helm upgrade --install ohsu funnel
```

# 2. Proxy the Service for local testing

```sh
kubectl port-forward service/funnel 8000:8000
```

Now the funnel server can be accessed as if it were running locally. This can be verified by listing all tasks, which will return an empty JSON list:

```sh
funnel task list
# {}
```

A task can then be submitted following the [standard workflow](../tasks.md):

```sh
funnel examples hello-world > hello-world.json

funnel task create hello-world.json
# <Task ID>
```

# Storage Architecture

![Kubernetes Storage Architecture](./k8s-pvc.png)

# Additional Resources 📚

- [Helm Repo](https://ohsu-comp-bio.github.io/helm-charts)

- [Helm Repo Source](https://github.com/ohsu-comp-bio/helm-charts)

- [Helm Charts](https://github.com/ohsu-comp-bio/helm-charts/tree/main/charts/funnel)

- [Helm Chart Best Practices Guide](https://helm.sh/docs/chart_best_practices/)
