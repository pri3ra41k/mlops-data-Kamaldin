mkdir -p .devcontainer
cat > .devcontainer/devcontainer.json <<'EOF'
{
  "name": "mlops-data",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
  "postCreateCommand": "pip install poetry"
}
EOF
