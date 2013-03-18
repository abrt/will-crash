bin_PROGRAMS = will_segfault will_abort
lib_LTLIBRARIES = libwilljavasegfault.la

will_segfault_SOURCES = will_segfault.c
will_abort_SOURCES = will_abort.c

WillRaiseSigSegvdir = $(JAVADIR)
WillRaiseSigSegv_JAVA = WillRaiseSigSegv.java

libwilljavasegfault_la_SOURCES = will_java_segfault.c
libwilljavasegfault_la_CPPFLAGS = -I$(javahome)/include -I$(javahome)/include/linux

bin_SCRIPTS = will_python_raise will_python3_raise will_ruby_raise will_python_sigsegv will_java_segfault

will_java_segfault: will_java_segfault.in
	sed -e s,\@JAVADIR\@,\"$(JAVADIR)\",g \
		will_java_segfault.in >will_java_segfault && chmod +x will_java_segfault

all-local: will_java_segfault

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
	WillRaiseSigSegv.java
