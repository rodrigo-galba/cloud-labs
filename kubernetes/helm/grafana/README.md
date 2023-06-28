# Grafana Stack

> Grafana LGTM stack (Loki for logs, Grafana for visualization, Tempo for traces, Mimir for metrics). 

# Dashboards

- [Node Exporter](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)
- [thanos](https://grafana.com/grafana/dashboards/12937-thanos-overview-public/)
- [Minio](https://grafana.com/grafana/dashboards/13502-minio-dashboard/)
- [Kubernetes](https://grafana.com/grafana/dashboards/6417-kubernetes-cluster-prometheus/)

# Grafana Helm Chart

* Installs the web dashboarding system [Grafana](http://grafana.org/)

## Get Repo Info

```console
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

## Installing the Chart

To install the chart with the release name `my-release`:

```console
helm install my-release grafana/grafana
```

## Uninstalling the Chart

To uninstall/delete the my-release deployment:

```console
helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.
