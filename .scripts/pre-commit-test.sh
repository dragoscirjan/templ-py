#! /bin/bash
set -xe

if [[ $(uname -s) == "Darwin" ]]; then
  SCRIPT=$(readlink -n $0)
else
  SCRIPT=$(readlink -f $0)
fi
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH/..

pwd

cat Makefile

make test
