# http://fedoraproject.org/wiki/Packaging:Guidelines#PIE
# http://fedoraproject.org/wiki/Hardened_Packages
%global _hardened_build 1

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name:           will-crash
Version:        0.13.5
Release:        1%{?dist}
Summary:        Set of crashing executables written in various languages

Group:          Development/Tools
License:        GPLv3
URL:            https://github.com/abrt/will-crash
Source0:        https://github.com/abrt/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

%if %{JAVA}
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
%endif
BuildRequires:  meson >= 0.50.0
BuildRequires:  gcc-c++
BuildRequires:  ruby-devel

%if %{JAVA}
Requires:       java-headless >= 1.7.0.0
Requires:       javapackages-tools
%endif
Requires:       perl-interpreter
Requires:       python3
Requires:       ruby
Recommends:     kernel-devel

%description
The main purpose of this project is to provide sample
executables for testing crash/exception handling tools
like ABRT.

%prep
%setup -q

%build
%if %{JAVA}
%meson \
    -Djavadir=%{_javadir} \
    -D_java_home=%{java_home} \
    %{nil}
%else
mv meson.build-nojava meson.build
mv src/meson.build-nojava src/meson.build
rm meson_options.txt
%meson \
    %{nil}
%endif
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
%{_bindir}/will_cpp_segfault
%{_bindir}/will_stackoverflow
%{_bindir}/will_oops
%if %{JAVA}
%{_bindir}/will_java_segfault
%{_bindir}/will_java_throw
%{_bindir}/will_java_throw_remote
%{_bindir}/will_java_throw_suppressed
%{_datadir}/java/WillRaiseSigSegv.class
%{_datadir}/java/willcrash/willremoteloader.jar
%{_datadir}/java/willcrash/willsuppressed.jar
%{_datadir}/java/willcrash/willuncaught.jar
%endif
%{_datadir}/will-crash/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libwillcrash.so
# There’s no way to set the rpath in Java, so it will either look in whatever
# path it does or we have to use System.load(), which takes a path to a library,
# but then you need to guess the extension, which is not portable (though doesn’t
# matter here per se, it’s still not desirable to write hacks).
%if %{JAVA}
%{_libdir}/libwilljavasegfault.so*
%endif
%{ruby_vendorlibdir}/will_crash.rb

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.13.3-6
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Michal Fabik <mfabik@redhat.com> - 0.13.3-2
- spec: Correct Source0

* Tue Dec 01 2020 Michal Fabik <mfabik@redhat.com> - 0.13.3-1
- will_stackoverflow: Disable optimizations
- Drop libtool dependency
- Fix KMODSRC substitution
- Require perl-interpreter

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.13.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Feb 21 2020 Ernestas Kulik <ekulik@redhat.com> - 0.13.2-1
- new upstream release: 0.13.2

* Thu Feb 20 2020 Ernestas Kulik <ekulik@redhat.com> - 0.13.1-1
- new upstream release: 0.13.1

* Thu Feb 20 2020 Ernestas Kulik <ekulik@redhat.com> - 0.13.1-1
- new upstream release: 0.13.1

* Thu Feb 20 2020 Ernestas Kulik <ekulik@redhat.com> - 0.13-1
- new upstream release: 0.13

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Ernestas Kulik <ekulik@redhat.com> - 0.12-1
- Update upstream URIs
- Enable PIEs
- Remove RHEL 6/7-specific content
- Update to 0.12

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10-3
- Rebuild for Python 3.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 13 2015 Richard Marko <rmarko@fedoraproject.org> - 0.10-1
- Version bump
- fix will_python_sigsegv for s390x
- Make it possible to run will_oops.in multiple times in row
- will_ruby_raise: fancy stacktrace
- Add --help to will_abort

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 24 2014 Richard Marko <rmarko@fedoraproject.org> - 0.9-2
- fix will_java_throw_suppressed availability on RHEL6

* Thu Oct 30 2014 Jakub Filak <jfilak@redhat.com> - 0.9-1
- port to javapackages-utils

* Wed Sep 10 2014 Richard Marko <rmarko@fedoraproject.org> - 0.8-1
- add will_segfault --break-link-map

* Wed Aug 27 2014 Martin Milata <mmilata@redhat.com> - 0.7-5
- added will_stackoverflow

* Mon Aug 18 2014 Richard Marko <rmarko@fedoraproject.org> - 0.7-4
- support OpenJDK8

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 2 2014 Richard Marko  <rmarko@fedoraproject.org> - 0.7-1
- Version bump
- added will_abort --random
- added will_java_throw_remote

* Tue Jan 14 2014 Richard Marko  <rmarko@fedoraproject.org> - 0.6-1
- Version bump
- added will_cpp_segfault
- reworked will_segfault to produce more stack frames

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Jiri Moskovcak <jmoskovc@redhat.com> 0.5-1
- new upstream release - 0.5
- added will_oops

* Mon Mar 18 2013 Richard Marko  <rmarko@fedoraproject.org> - 0.4-1
- Version bump, added will_java_segfault

* Thu Feb 21 2013 Richard Marko <rmarko@fedoraproject.org> - 0.3-1
- Version bump

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Richard Marko <rmarko@redhat.com> - 0.2-2
- Don't require python3 for el6

* Wed Jul 25 2012 Richard Marko <rmarko@redhat.com> - 0.2-1
- Version bump

* Mon Jul 23 2012 Richard Marko <rmarko@redhat.com> - 0.1-2
- Added missing automake build requirement

* Fri Jul 20 2012 Richard Marko <rmarko@redhat.com> - 0.1-1
- Initial packaging attempt
