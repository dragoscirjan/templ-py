#! /bin/bash
set -xe

uname -a | grep darwin && SCRIPT=$(readlink -n $0)
uname -a | grep darwin || SCRIPT=$(readlink -f $0)
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH/..

pwd

cat Makefile

make test
