SUBDIRS = src

EXTRA_DIST = LICENSE README.rst autogen.sh will-crash.spec.in

RPM_DIRS = --define "_sourcedir `pwd`" \
           --define "_rpmdir `pwd`/build" \
           --define "_specdir `pwd`" \
           --define "_builddir `pwd`/build" \
           --define "_srcrpmdir `pwd`/build"

rpm: dist will-crash.spec
	rpmbuild $(RPM_DIRS) -ba will-crash.spec
srpm: dist will-crash.spec
	rpmbuild $(RPM_DIRS) -bs will-crash.spec
