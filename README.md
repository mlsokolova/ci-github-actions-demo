# ci-github-actions-demo
## Install and configure Github Actions Self-Hosted Runner
```
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.335.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.335.1/actions-runner-linux-x64-2.335.1.tar.gz
echo "4ef2f25285f0ae4477f1fe1e346db76d2f3ebf03824e2ddd1973a2819bf6c8cf  actions-runner-linux-x64-2.335.1.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.335.1.tar.gz
./config.sh --url https://github.com/mlsokolova/ci-github-actions-demo --token <you token>
```
, enter the following parameters (or just press Enter for default values):
- the name of the runner group
- any additional labels
- name of work folder
## Run the runner
`./run.sh`
, expect output like this:
```
√ Connected to GitHub

Current runner version: '2.335.1'
2026-06-15 14:04:47Z: Listening for Jobs

```


## TODO:
- check what does it mean  
```
Warning: Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v3. Actions will be forced to run with Node.js 24 by default starting June 16th, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```