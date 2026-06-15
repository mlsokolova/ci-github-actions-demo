# ci-github-actions-demo
## Install Github Actions Self-Hosted Runner
```
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.335.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.335.1/actions-runner-linux-x64-2.335.1.tar.gz
echo "4ef2f25285f0ae4477f1fe1e346db76d2f3ebf03824e2ddd1973a2819bf6c8cf  actions-runner-linux-x64-2.335.1.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.335.1.tar.gz
```
## Install dependencies (WSL)
 `sudo ./bin/installdependencies.sh`

## Configure runner
`./config.sh --url https://github.com/mlsokolova/ci-github-actions-demo --name myrunner --runnergroup  Default  --labels self-hosted --work  _work --token you_token`


## Run the runner
, expect output like this:
```
√ Connected to GitHub

Current runner version: '2.335.1'
2026-06-15 14:04:47Z: Listening for Jobs

```
## Set the runner for a workflow job
use the label in the Github Actions workflow to run jobs on self-hosted runner:
`runs-on: self-hosted`
