{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "class101-server" -}}
{{- default .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "class101-server.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "class101-server.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "class101-server.labels" -}}
helm.sh/chart: {{ include "class101-server.chart" . }}
{{ include "class101-server.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "class101-server.selectorLabels" -}}
app.kubernetes.io/name: {{ include "class101-server" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Create the name of the service account to use
*/}}
{{- define "class101-server.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
    {{ default (include "class101-server.fullname" .) .Values.serviceAccount.name }}
{{- else -}}
    {{ default "default" .Values.serviceAccount.name }}
{{- end -}}
{{- end -}}


{{/*
Datadog labels
*/}}
{{- define "class101-server.apm.labels" -}}
tags.datadoghq.com/{{.Release.Name}}.env: {{ .Values.container.activeProfile }}
tags.datadoghq.com/{{.Release.Name}}.service: {{ .Release.Name }}
tags.datadoghq.com/{{.Release.Name}}.version: {{ .Values.image.versionTag }}
{{- end -}}

{{/*
Datadog annotations
*/}}
{{- define "class101-server.apm.annotations" -}}
tags.datadoghq.com/{{.Release.Name}}.check_names: {{ .Values.container.activeProfile }}
tags.datadoghq.com/{{.Release.Name}}.init_configs: {{ .Release.Name }}
tags.datadoghq.com/{{.Release.Name}}.instances: |
    [
      {
        "host": "%%host%%"
      }
    ]

{{- end -}}