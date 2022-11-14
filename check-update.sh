#!/bin/sh
git ls-remote --tags https://invent.kde.org/education/labplot.git 2>/dev/null |awk '{ print $2; }'  |grep -v '\^{}' |sed -e 's,refs/tags/,,' |grep -vE -- '-(alpha|beta|rc)' |sort -V |tail -n1
