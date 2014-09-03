#!/bin/bash
mkdir $PWD/CodeBase
cd CodeBase
for i in {1..30}
do
	wget -U Mozilla https://api.github.com/orgs/mozilla/repos?page=$i
done
