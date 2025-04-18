Here are all the setup commands for Minikube in markdown format:

```markdown
# Minikube Setup Commands for SonarQube

### Start Minikube
```bash
minikube start --driver=docker --cpus=2 --memory=4096MB --kubernetes-version=stable
```

### Fix minikube for the connection error
```bash
   minikube ssh
   sudo sysctl -w vm.max_map_count=262144
   exit
```


### Verify Minikube is running
```bash
minikube status
kubectl cluster-info
```

## SonarQube Namespace and Storage

### Create namespace for SonarQube
```bash
kubectl create namespace sonarqube
```

### Create persistent volume claim
cd /workspaces/SonarQube/6_Symbols/2_minikube

### If All Files are there
kubectl apply -f /workspaces/SonarQube/6_Symbols/2_minikube


```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: sonarqube-data
  namespace: sonarqube
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
EOF
```

## Database Configuration

### Create database credentials
```bash
kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=$(openssl rand -base64 12) \
  --from-literal=POSTGRES_DB=sonar
```

### Deploy PostgreSQL
```bash
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sonarqube-db
  namespace: sonarqube
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sonarqube-db
  template:
    metadata:
      labels:
        app: sonarqube-db
    spec:
      containers:
      - name: postgres
        image: postgres:13
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: sonar-db-credentials
              key: POSTGRES_USER
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: sonar-db-credentials
              key: POSTGRES_PASSWORD
        - name: POSTGRES_DB
          valueFrom:
            secretKeyRef:
              name: sonar-db-credentials
              key: POSTGRES_DB
        volumeMounts:
        - name: postgres-data
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-data
        persistentVolumeClaim:
          claimName: sonarqube-data
---
apiVersion: v1
kind: Service
metadata:
  name: sonarqube-db
  namespace: sonarqube
spec:
  selector:
    app: sonarqube-db
  ports:
  - port: 5432
    targetPort: 5432
EOF
```

## SonarQube Deployment

### Deploy SonarQube server
```bash
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sonarqube
  namespace: sonarqube
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sonarqube
  template:
    metadata:
      labels:
        app: sonarqube
    spec:
      containers:
      - name: sonarqube
        image: sonarqube:9.9-community
        ports:
        - containerPort: 9000
        env:
        - name: SONAR_JDBC_URL
          value: jdbc:postgresql://sonarqube-db:5432/sonar
        - name: SONAR_JDBC_USERNAME
          valueFrom:
            secretKeyRef:
              name: sonar-db-credentials
              key: POSTGRES_USER
        - name: SONAR_JDBC_PASSWORD
          valueFrom:
            secretKeyRef:
              name: sonar-db-credentials
              key: POSTGRES_PASSWORD
        resources:
          limits:
            memory: "2Gi"
            cpu: "1"
          requests:
            memory: "1Gi"
            cpu: "500m"
        readinessProbe:
          httpGet:
            path: /
            port: 9000
          initialDelaySeconds: 60
          periodSeconds: 30
        livenessProbe:
          httpGet:
            path: /
            port: 9000
          initialDelaySeconds: 120
          periodSeconds: 30
EOF
```

### Create SonarQube service
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: sonarqube
  namespace: sonarqube
spec:
  type: NodePort
  selector:
    app: sonarqube
  ports:
  - port: 9000
    targetPort: 9000
    nodePort: 30900
EOF
```

## Access Configuration

### Check deployment status
```bash
kubectl get all -n sonarqube
```

### Port forward to access SonarQube UI
```bash
kubectl port-forward -n sonarqube svc/sonarqube 9000:9000 
```



### Access SonarQube in browser
```
http://localhost:9000
```

## Cleanup Commands

### Delete namespace (removes all resources)
```bash
kubectl delete namespace sonarqube
```

### Stop Minikube
```bash
minikube stop
```

### Delete Minikube cluster when done
```bash
minikube delete
```
```

This markdown document provides all the necessary commands to set up Minikube and deploy SonarQube with PostgreSQL in a structured, easy-to-follow format. The commands are organized into logical sections that follow the deployment process step by step.