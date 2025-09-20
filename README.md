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
  minikube image load focker.ir/projectnessie/nessie:0.105.1 && minikube image load focker.ir/postgres:17.2-bookworm && minikube image load focker.ir/minio/minio:RELEASE.2025-01-20T14-49-07Z && minikube image load focker.ir/trinodb/trino:476
```

## Apply PostgreSQL configurations
#### postgres
```bash
  kubectl apply -f postgres-nessie.yaml
```
```bash
  kubectl port-forward svc/postgres-nessie 5432:5432
```

#### minio
```bash
  kubectl apply -f minio.yaml
```
```bash
  kubectl port-forward svc/minio 9001:9001
```

### secrets

```bash
  kubectl create secret generic postgres-secrets --from-env-file=postgres-secrets
  kubectl create secret generic minio-secrets --from-env-file=minio-secrets
```

### Run
#### nessie

```bash
  helm upgrade --install nessie nessie/nessie --values nessie-values.yaml --timeout 10m
```
```bash
  kubectl port-forward svc/nessie 19120:19120 
```

#### trino

```bash
  helm upgrade --install trino-cluster trino/trino --values trino-values.yaml --timeout 10m
```

```bash
  kubectl port-forward svc/trino-cluster-trino-stage 8080:8080 
```
