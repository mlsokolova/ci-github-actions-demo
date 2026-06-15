# Continuous Integration and GitHub Actions
## Files

| File name | Description |
| --- | --- |
| `main.py` | Python script that collects runtime and platform details (Python version, OS, architecture, kernel, user, IP addresses) and prints them. |
| `test_main.py` | Unit tests for `main.py`; verifies that `get_platform_runtime_info()` returns all expected keys. |
| `.gitignore` | Excludes `__pycache__` directories and `.env` files from version control. |
| `.github/workflows/1-main-push.yaml` | CI workflow triggered on push to `main`; checks out the repo on a self-hosted runner and prints a hello message. |
| `.github/workflows/2-run-test copy.yaml` | CI workflow triggered on push to `main`; runs unit tests on `ubuntu-latest` with Python 3.9. |
| `.github/workflows/3-cron-scheduling.yaml` | Workflow triggered manually or on an hourly cron schedule; checks out the repo on `ubuntu-latest` and prints a success message. |
| `.github/workflows/4-matrix.yaml` | CI workflow triggered on push to `main`; runs unit tests across a matrix of Python versions (3.7, 3.8, 3.9) on `ubuntu-22.04`. |

## Self-hosted runner
### Install a GitHub Actions self-hosted runner
```
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.335.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.335.1/actions-runner-linux-x64-2.335.1.tar.gz
echo "4ef2f25285f0ae4477f1fe1e346db76d2f3ebf03824e2ddd1973a2819bf6c8cf  actions-runner-linux-x64-2.335.1.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.335.1.tar.gz
```
### Install dependencies (WSL)

Run:

`sudo ./bin/installdependencies.sh`

### Configure runner
`./config.sh --url https://github.com/mlsokolova/ci-github-actions-demo --name myrunner --runnergroup  Default  --labels self-hosted --work  _work --token you_token`

### Run the runner
`./run.sh`  
Expect output like this:

```
√ Connected to GitHub

Current runner version: '2.335.1'
2026-06-15 14:04:47Z: Listening for Jobs

```
### Use the runner in a workflow job

Use the label in the GitHub Actions workflow to run jobs on a self-hosted runner:

`runs-on: self-hosted`
