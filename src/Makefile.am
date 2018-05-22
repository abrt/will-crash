bin_PROGRAMS = will_segfault \
       will_segfault_in_new_pid \
       will_segfault_threads \
       will_abort \
       will_cpp_segfault \
       will_stackoverflow

lib_LTLIBRARIES = libwilljavasegfault.la libwillcrash.la

will_segfault_SOURCES = will_segfault.c
will_segfault_LDADD = libwillcrash.la
will_segfault_CFLAGS = -fno-optimize-sibling-calls
will_segfault_threads_SOURCES = will_segfault_threads.c
will_segfault_threads_CFLAGS = -pthread
will_segfault_in_new_pid_SOURCES = will_segfault_in_new_pid.c
will_abort_SOURCES = will_abort.c
will_cpp_segfault_SOURCES = will_cpp_segfault.cc
will_stackoverflow_SOURCES = will_stackoverflow.c
will_stackoverflow_CFLAGS = -fno-optimize-sibling-calls -fno-inline

WillJavaClassesdir = $(JAVADIR)
WillJavaClasses_DATA = WillRaiseSigSegv.class

WillJavaJarsdir = $(JARDIR)
WillJavaJars_DATA = willremoteloader.jar willuncaught.jar

if JAVA_SUPPORTS_SUPPRESSED
WillJavaJars_DATA += willsuppressed.jar
endif

kmoddir = $(datarootdir)/@PACKAGE@/will_oops_kmod/
kmod_DATA = will_oops_kmod/Makefile will_oops_kmod/will_oops.c

rubylibdir = $(RUBYLIBDIR)
rubylib_DATA = will_crash.rb

libwilljavasegfault_la_SOURCES = will_java_segfault.c
libwilljavasegfault_la_CPPFLAGS = -I$(javahome)/include -I$(javahome)/include/linux

libwillcrash_la_SOURCES = libwillcrash.c

bin_SCRIPTS = will_python3_raise \
			  will_ruby_raise \
			  will_java_segfault \
			  will_oops \
			  will_java_throw \
			  will_java_throw_remote

if BUILD_PYTHON2
bin_SCRIPTS += will_python_sigsegv
bin_SCRIPTS += will_python_raise
endif

if JAVA_SUPPORTS_SUPPRESSED
bin_SCRIPTS += will_java_throw_suppressed
endif

will_java_segfault: will_java_segfault.in
	sed -e s,\@JAVADIR\@,\"$(JAVADIR)\",g \
		will_java_segfault.in >will_java_segfault && chmod +x will_java_segfault

will_java_throw: will_java_throw.in
	sed -e s,\@JAR\@,\"`basename $(JARDIR)`/willuncaught.jar\",g \
		will_java_throw.in >will_java_throw && chmod +x will_java_throw

will_java_throw_remote: will_java_throw_remote.in
	sed -e s,\@JAR\@,\"`basename $(JARDIR)`/willremoteloader.jar\",g \
		-e s,\@JARUNCAUGHT\@,\"$(JARDIR)/willuncaught.jar\",g \
		will_java_throw_remote.in >will_java_throw_remote && chmod +x will_java_throw_remote

if JAVA_SUPPORTS_SUPPRESSED
will_java_throw_suppressed: will_java_throw_suppressed.in
	sed -e s,\@JAR\@,\"`basename $(JARDIR)`/willsuppressed.jar\",g \
		will_java_throw_suppressed.in >will_java_throw_suppressed && chmod +x will_java_throw_suppressed
endif

.java.class:
	$(JAVAC) -Xlint:unchecked $<

willremoteloader.jar: WontCatchRemoteException.class
	$(JAR) $(JARFLAGS) $@ $^ JarGetter.class && rm -rf $^ JarGetter.class

willuncaught.jar: WontCatchNullPointerException.class
	$(JAR) $(JARFLAGS) $@ $^ && rm -rf $^

if JAVA_SUPPORTS_SUPPRESSED
willsuppressed.jar: WontCatchSuppressedException.class
	$(JAR) $(JARFLAGS) $@ $^ && rm -rf $^
endif

will_oops: will_oops.in
	sed -e s,\@KMODSRC\@,\"$(kmoddir)\",g \
		will_oops.in >will_oops && chmod +x will_oops

ALL_TARGETS=will_java_segfault will_oops will_java_throw will_java_throw_remote

if JAVA_SUPPORTS_SUPPRESSED
ALL_TARGETS += will_java_throw_suppressed
endif

all-local: $(ALL_TARGETS)

clean-local: clean-local-check
.PHONY: clean-local-check
clean-local-check:
	rm -rf $(ALL_TARGETS) *.class *.jar

EXTRA_DIST = \
	will_python3_raise \
	will_ruby_raise \
	will_crash.rb \
	will_java_segfault.in \
	WillRaiseSigSegv.java \
	will_oops.in \
	$(kmod_DATA) \
	libwillcrash.h \
	will_java_throw.in \
	WontCatchNullPointerException.java \
	will_java_throw_remote.in \
	WontCatchRemoteException.java

if JAVA_SUPPORTS_SUPPRESSED
EXTRA_DIST += will_java_throw_suppressed.in
EXTRA_DIST += WontCatchSuppressedException.java
endif

if BUILD_PYTHON2
EXTRA_DIST += will_python_sigsegv
EXTRA_DIST += will_python_raise
endif
