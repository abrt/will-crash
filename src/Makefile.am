bin_PROGRAMS = will_segfault will_abort will_cpp_segfault
lib_LTLIBRARIES = libwilljavasegfault.la libwillcrash.la

will_segfault_SOURCES = will_segfault.c
will_segfault_LDADD = libwillcrash.la
will_segfault_CFLAGS = -fno-optimize-sibling-calls
will_abort_SOURCES = will_abort.c
will_cpp_segfault_SOURCES = will_cpp_segfault.cc

WillJavaClassesdir = $(JAVADIR)
WillJavaClasses_JAVA = WillRaiseSigSegv.java WontCatchNullPointerException.java

kmoddir = $(datarootdir)/@PACKAGE@/will_oops_kmod/
kmod_DATA = will_oops_kmod/Makefile will_oops_kmod/will_oops.c

libwilljavasegfault_la_SOURCES = will_java_segfault.c
libwilljavasegfault_la_CPPFLAGS = -I$(javahome)/include -I$(javahome)/include/linux

libwillcrash_la_SOURCES = libwillcrash.c

bin_SCRIPTS = will_python_raise will_python3_raise will_ruby_raise will_python_sigsegv will_java_segfault will_oops will_java_throw

will_java_segfault: will_java_segfault.in
	sed -e s,\@JAVADIR\@,\"$(JAVADIR)\",g \
		will_java_segfault.in >will_java_segfault && chmod +x will_java_segfault

will_java_throw: will_java_throw.in
	sed -e s,\@JAVADIR\@,\"$(JAVADIR)\",g \
		will_java_throw.in >will_java_throw && chmod +x will_java_throw

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
	$(kmod_DATA) \
	libwillcrash.h \
	WontCatchNullPointerException.java
