# http://fedoraproject.org/wiki/Packaging:Guidelines#PIE
# http://fedoraproject.org/wiki/Hardened_Packages
%global _hardened_build 1

Name:           will-crash
Version:        0.13.1
Release:        1%{?dist}
Summary:        Set of crashing executables written in various languages

Group:          Development/Tools
License:        GPLv3
URL:            https://github.com/abrt/will-crash
Source0:        https://github.com/abrt/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  ruby-devel

Requires:       java-headless >= 1.7.0.0
Requires:       javapackages-tools
Requires:       perl
Requires:       python3
Requires:       ruby

%description
The main purpose of this project is to provide sample
executables for testing crash/exception handling tools
like ABRT.

%prep
%setup -q

%build
%meson \
    -Djavadir=%{_javadir} \
    -D_java_home=%{java_home} \
    %{nil}
%meson_build

%install
%meson_install

%files
%doc README.rst
%doc LICENSE
%{_bindir}/will_segfault
%{_bindir}/will_segfault_in_new_pid
%{_bindir}/will_segfault_threads
%{_bindir}/will_abort
%{_bindir}/will_perl_sigsegv
%{_bindir}/will_python3_sigsegv
%{_bindir}/will_python3_raise
%{_bindir}/will_ruby_raise
%{_bindir}/will_java_segfault
%{_bindir}/will_java_throw
%{_bindir}/will_java_throw_remote
%{_bindir}/will_java_throw_suppressed
%{_bindir}/will_cpp_segfault
%{_bindir}/will_stackoverflow
%{_bindir}/will_oops
%{_datadir}/java/WillRaiseSigSegv.class
%{_datadir}/java/willcrash/willremoteloader.jar
%{_datadir}/java/willcrash/willsuppressed.jar
%{_datadir}/java/willcrash/willuncaught.jar
%{_datadir}/will-crash/*
%{_libdir}/%{name}/libwillcrash.so
# There’s no way to set the rpath in Java, so it will either look in whatever
# path it does or we have to use System.load(), which takes a path to a library,
# but then you need to guess the extension, which is not portable (though doesn’t
# matter here per se, it’s still not desirable to write hacks).
%{_libdir}/libwilljavasegfault.so*
%{ruby_vendorlibdir}/will_crash.rb

%changelog
