# Download

## Install a release

The [latest stable release](https://github.com/calypr/funnel/releases/latest) includes binaries for Linux and macOS on amd64 and arm64. Each release provides SHA-256 checksums.

Install the latest release:

```sh
curl -fsSL https://calypr.org/tools/funnel/install.sh | bash
```

The default destination is `$HOME/.local/bin`. To install a specific version, pass its tag:

```sh
curl -fsSL https://calypr.org/tools/funnel/install.sh | bash -s -- v0.12.3
```

See [all releases and release notes](https://github.com/calypr/funnel/releases).
Before replacing an existing deployment, read the [upgrade guide](upgrading.md).

## Container images

Images for both amd64 and arm64 are published to [Quay](https://quay.io/repository/ohsu-comp-bio/funnel?tab=tags).
Use a version tag for a fixed release:

```sh
docker pull quay.io/ohsu-comp-bio/funnel:v0.12.3
```

Stable releases also update `latest`. Start a server with Docker:

```sh
docker run --rm -p 8000:8000 quay.io/ohsu-comp-bio/funnel:latest server run
```

Configure persistent task storage before using this temporary container for an existing deployment. See [deployment configuration](compute/deployment.md).
