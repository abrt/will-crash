AC_INIT([will-crash],
        m4_esyscmd([tr -d '\n' < VERSION]),
        [rmarko@redhat.com])

AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign -Wall -Werror])
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

AC_DISABLE_STATIC
AC_PROG_LIBTOOL

AC_PROG_CC
AM_PROG_CC_C_O
AC_PROG_CXX

AC_CHECK_HEADERS([stdlib.h])

AC_CONFIG_FILES([Makefile src/Makefile will-crash.spec])

AC_ARG_WITH([javahome],
        AS_HELP_STRING([--with-javahome=JAVA SDK Home],
            [Specify location of top directory of JAVA SDK i.e. where the bin, lib and include directories live]),
            [], [with_javahome="/etc/alternatives/java_sdk"])
AC_SUBST([javahome], [$with_javahome])

AC_MSG_NOTICE([Java SDK home is $javahome])

AC_ARG_WITH([javaroot],
        AS_HELP_STRING([--with-javaroot=DIR],
            [The value of this variable is passed to the -d option to javac]),
            [], [with_javaroot=./])
AC_SUBST([JAVAROOT], [$with_javaroot])

AC_ARG_WITH([javadir],
        AS_HELP_STRING([--with-javadir=DIR],
            [Directory for java files]),
            [], [with_javadir=${datadir}/java])
AC_SUBST([JAVADIR], [$with_javadir])
AC_SUBST([JARDIR], [$with_javadir/willcrash])

AC_MSG_NOTICE([Directory for java files is $JAVADIR])

AC_ARG_WITH([rubylibdir],
        AS_HELP_STRING([--with-rubydir=DIR],
            [Directory for ruby libraries]),
            [], [with_rubylibdir="/usr/share/ruby/vendor_ruby"])
AC_SUBST([RUBYLIBDIR], [$with_rubylibdir])

AC_PATH_PROGS(JAVAC,javac,,[$javahome/bin])
AC_PATH_PROGS(JAVA,java,,[$javahome/bin])
AC_PATH_PROGS(JAR,jar,,[$javahome/bin])

JARFLAGS=cvf
AC_SUBST(JARFLAGS)

AC_OUTPUT
