# Kubernetes reference templates

These files are historical reference material. Funnel does not embed them or use them as runtime defaults. Configure Kubernetes templates through the deployment's Helm chart.

The reference files originated in the [Funnel Helm chart](https://github.com/ohsu-comp-bio/helm-charts/tree/funnel-0.1.60/charts/funnel/files).

Templates used by Go tests live beside their tests:

- [worker job](https://github.com/calypr/funnel/blob/738ab75a7056321d82cf57d9781d0af5a4433da6/internal/compute/kubernetes/testdata/worker-job.yaml)
- [service account](https://github.com/calypr/funnel/blob/738ab75a7056321d82cf57d9781d0af5a4433da6/internal/compute/kubernetes/resources/testdata/serviceaccount.yaml)
- [executor job](https://github.com/calypr/funnel/blob/738ab75a7056321d82cf57d9781d0af5a4433da6/internal/worker/testdata/executor-job.yaml)
