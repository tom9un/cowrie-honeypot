#!/bin/bash

apt-get install python-dev git-core && \
pip install supervisor && \
pushd /tmp && \
rm -Rf 814fd0d0f7020e918a95 && \
git clone https://gist.github.com/814fd0d0f7020e918a95.git && \
cd 814fd0d0f7020e918a95 && \
./install.sh && \
rm -Rf /tmp/814fd0d0f7020e918a95 && \
popd && \
echo "Finished..."
