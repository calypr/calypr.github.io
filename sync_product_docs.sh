#!/bin/bash

git clone https://github.com/bmeg/grip.git products/grip
git clone https://github.com/ohsu-comp-bio/funnel.git products/funnel
git clone https://github.com/calypr/git-drs.git products/git-drs

rsync -av products/grip/website/content/docs/ ./docs/tools/grip
rsync -av products/funnel/website/content/ ./docs/tools/funnel
rsync -av products/git-drs/docs/ ./docs/tools/git-drs