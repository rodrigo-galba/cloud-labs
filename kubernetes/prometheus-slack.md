# Prometheus + Alertmanager 

## Customize observability addon

Create custom values file:
```yaml
## Configuration for alertmanager
## ref: https://prometheus.io/docs/alerting/alertmanager/
##
alertmanager:
  ## Alertmanager configuration directives
  ## ref: https://prometheus.io/docs/alerting/configuration/#configuration-file
  ##      https://prometheus.io/webtools/alerting/routing-tree-editor/
  ##
  config:
    global:
      resolve_timeout: 5m
      slack_api_url: "slack.com"
    inhibit_rules:
      - source_matchers:
          - 'severity = critical'
        target_matchers:
          - 'severity =~ warning|info'
        equal:
          - 'namespace'
          - 'alertname'
      - source_matchers:
          - 'severity = warning'
        target_matchers:
          - 'severity = info'
        equal:
          - 'namespace'
          - 'alertname'
      - source_matchers:
          - 'alertname = InfoInhibitor'
        target_matchers:
          - 'severity = info'
        equal:
          - 'namespace'
    route:
      group_by: ['namespace']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 12h
      receiver: 'null'
      routes:
      - match:
          alertname: Watchdog
        receiver: 'null'
      - receiver: 'slack-notifications'
        continue: true
    receivers:
    - name: 'null'
    - name: 'slack-notifications'
      slack_configs:
      - channel: "#alerts"
        title: '[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}] Test Alertmanager'
        text: >-
          {{ range .Alerts }}
            *Alert:* {{ .Annotations.summary }} - `{{ .Labels.severity }}`
          {{ end }}
        send_resolved: true
    templates:
    - '/etc/alertmanager/config/*.tmpl'

```


```
$ microk8s enable observability --kube-prometheus-stack-values=obs-values.yml
Infer repository core for addon observability
Addon core/dns is already enabled
Addon core/helm3 is already enabled
Addon core/hostpath-storage is already enabled
Enabling observability
Release "kube-prom-stack" does not exist. Installing it now.
```

```
helm get values -n observability kube-prom-stack > prom-values.yaml
```


-----
References
- https://grafana.com/pt-br/blog/2020/02/25/guia-passo-a-passo-para-configurar-o-alertmanager-do-prometheus-com-o-slack-pagerduty-e-gmail/
- https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml
- https://github.com/canonical/microk8s-core-addons/blob/main/addons/observability/enable
- https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml