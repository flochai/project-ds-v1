<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/efd45723-a41b-42a2-aaf7-b57fe2250286" />


Project DS V1 
-------------

Project DS V1 is the first working version of my end-of-degree DevSecOps pipeline project. Built over four days, it demonstrates a CI/CD workflow that integrates security scanning and GitOps-style deployment, laying the foundation for a production-ready DevSecOps platform.

⸻

🔹 Architecture Overview
	•	CI/CD: GitHub Actions
	•	Containerization: Docker
	•	Registry: Harbor (self-hosted on AWS EC2, deployed via Helm)
	•	Cluster: k3s running on AWS EC2
	•	Security: Trivy image scanning
	•	GitOps: Argo CD + secondary repo (argo-anchor)
	•	Config updates: Automated with yq

⸻

🔹 Pipeline Workflow
	1.	Checkout Code → GitHub Actions pulls the repository.
	2.	Build & Test → Docker image build + unit tests.
	3.	Scan with Trivy → Detects CVEs and vulnerabilities.
	4.	Push to Harbor → Secure image storage in private registry.
	5.	Update Deployment Repo → yq updates the image tag in argo-anchor.
	6.	Argo CD Sync → Argo CD deploys the updated image to the k3s cluster.

Average pipeline runtime: ~2 minutes.

⸻

🔹 Setup & Usage

Prerequisites
	•	AWS EC2 instances (t3.medium for Harbor, any small instance for k3s)
	•	Helm installed on your local machine
	•	Kubernetes CLI (kubectl)
	•	GitHub repository with GitHub Actions enabled
	•	Trivy scanner installed or used via GitHub Action

Deployment Steps

1.	Deploy Harbor with Helm on a t3.medium EC2:

```
  helm repo add harbor https://helm.goharbor.io
  helm install harbor harbor/harbor -f values.yaml
```

2.	Set up a k3s cluster on EC2:

```
curl -sfL https://get.k3s.io | sh -
```

3.	Configure GitHub Actions secrets:

- HARBOR_USERNAME
- HARBOR_PASSWORD
- HARBOR_URL
- GITHUB_TOKEN (for pushing updates to argo-anchor)

4.	Push code changes → pipeline runs automatically.

---

🔹 Roadmap

Project DS will evolve into a full DevSecOps pipeline in the coming months. Planned features include:
	•	Kubescape → Kubernetes posture and compliance scanning
	•	Kyverno → Cluster-wide policy enforcement
	•	Cilium → Advanced networking and observability
	•	Vault → Secrets management and dynamic credentials

⸻

🔹 Status

✅ Proof of concept (V1) complete
🚧 Next steps: expand to production-grade DevSecOps pipeline

