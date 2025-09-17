## One time commands

```bash
  helm repo add nessie https://charts.projectnessie.org/
```

```bash
   helm repo update
```

## Start Minikube with sufficient resources

```bash
  minikube start --memory=8192 --cpus=4
```

## Load images into Minikube

```bash
  minikube image load ghcr.io/projectnessie/nessie:0.105.1 && minikube image load postgres:17.2-bookworm && minikube image load minio/minio:RELEASE.2025-01-20T14-49-07Z && minikube image load trinodb/trino:476
```

## Apply PostgreSQL configurations

```bash
  kubectl apply -f postgres-nessie.yaml
```

```bash
  kubectl apply -f minio.yaml
```

### secrets

```bash
  kubectl create secret generic postgres-secrets --from-env-file=postgres-secrets
  kubectl create secret generic minio-secrets --from-env-file=minio-secrets
```

### Run

```bash
  helm upgrade --install nessie nessie/nessie --values nessie-values.yaml --timeout 10m
```

```bash
  helm upgrade --install trino-cluster trino/trino --values trino-values.yaml --timeout 10m
```