VER="0.$(( $( cat VERSION | cut -d\. -f 2 ) + 1 ))"
echo "Releasing ${VER}"

echo ${VER} > VERSION
git add VERSION
git commit -m "version ${VER}"
git tag v${VER}
git clean -fdx -e releasing

git archive --format tar \
  --prefix will-crash-${VER}/ \
  --output will-crash-${VER}.tar.gz HEAD
