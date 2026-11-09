# Funnel

Funnel runs batch tasks through the GA4GH Task Execution Service API. Tasks describe their input files, container commands, output destinations, and resource requirements.

Funnel supports local Docker, Kubernetes, cloud batch services, and HPC schedulers. Supported deployments can also request GPUs. Operators choose the compute and storage backends; clients submit tasks through the same task API.

## Get started

- [Download and installation](docs/download.md)
- [Overview](docs/docs.md)
- [Tasks](docs/tasks.md)
- [GPU tasks](docs/compute/gpus.md)
- [Upgrade an existing deployment](docs/upgrading.md)
- [Latest release and release notes](https://github.com/calypr/funnel/releases/latest)
