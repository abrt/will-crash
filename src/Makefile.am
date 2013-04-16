bin_PROGRAMS = will_segfault will_abort
lib_LTLIBRARIES = libwilljavasegfault.la

will_segfault_SOURCES = will_segfault.c
will_abort_SOURCES = will_abort.c

WillRaiseSigSegvdir = $(JAVADIR)
WillRaiseSigSegv_JAVA = WillRaiseSigSegv.java

kmoddir = $(datarootdir)/@PACKAGE@/will_oops_kmod/
kmod_DATA = will_oops_kmod/Makefile will_oops_kmod/will_oops.c

libwilljavasegfault_la_SOURCES = will_java_segfault.c
libwilljavasegfault_la_CPPFLAGS = -I$(javahome)/include -I$(javahome)/include/linux

bin_SCRIPTS = will_python_raise will_python3_raise will_ruby_raise will_python_sigsegv will_java_segfault will_oops

will_java_segfault: will_java_segfault.in
	sed -e s,\@JAVADIR\@,\"$(JAVADIR)\",g \
		will_java_segfault.in >will_java_segfault && chmod +x will_java_segfault

will_oops: will_oops.in
	sed -e s,\@KMODSRC\@,\"$(kmoddir)\",g \
		will_oops.in >will_oops && chmod +x will_oops

all-local: will_java_segfault will_oops

clean-local: clean-local-check
.PHONY: clean-local-check
clean-local-check:
	rm -rf will_java_segfault

EXTRA_DIST = \
	will_python_raise \
	will_python3_raise \
	will_ruby_raise \
	will_python_sigsegv \
	will_java_segfault.in \
	WillRaiseSigSegv.java \
	will_oops.in \
	$(kmod_DATA)
