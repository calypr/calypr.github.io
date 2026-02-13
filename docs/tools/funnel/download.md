---
title: Download
menu:
  main:
    weight: -2000
---

## Releases

See the [Releases](https://github.com/ohsu-comp-bio/funnel/releases)  page for release history.

<!-- Release table -->
--8<-- "docs/tools/funnel/_releases.md"

## Homebrew

```sh
brew tap ohsu-comp-bio/formula
brew install funnel@0.11
```

## Build the lastest development version

In order to build the latest code, run:
```shell
$ git clone https://github.com/ohsu-comp-bio/funnel.git
$ cd funnel
$ make
```

Funnel requires Go 1.21+. Check out the [development docs][dev] for more detail.


[dev]: ./docs/development/developers.md
[docker]: https://docker.io
