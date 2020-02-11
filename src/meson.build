libwillcrash = shared_library('willcrash', 'libwillcrash.c',
  install: true,
)
libwill_java_segfault = shared_library('willjavasegfault', 'will_java_segfault.c',
  c_args: [
    '-I@0@'.format(join_paths(get_option('_java_home'), 'include')),
    '-I@0@'.format(join_paths(get_option('_java_home'), 'include', 'linux')),
  ],
  install: true,
)

executable('will_segfault', 'will_segfault.c',
  link_with: libwillcrash,
  install: true,
)
executable('will_segfault_in_new_pid', 'will_segfault_in_new_pid.c',
  c_args: cc.get_supported_arguments([
    '-Wno-nonnull',
  ]),
  install: true,
)
executable('will_segfault_threads', 'will_segfault_threads.c',
  c_args: cc.get_supported_arguments([
    '-Wno-nonnull',
    '-Wno-return-type',
  ]),
  dependencies: threads,
  install: true,
)
executable('will_abort', 'will_abort.c',
  install: true,
)
executable('will_cpp_segfault', 'will_cpp_segfault.cc',
  install: true,
)
executable('will_stackoverflow', 'will_stackoverflow.c',
  install: true,
)

jar('willremoteloader', 'WontCatchRemoteException.java',
  main_class: 'WontCatchRemoteException',
  install: true,
  install_dir: join_paths(javadir, jardir),
)
jar('willsuppressed', 'WontCatchSuppressedException.java',
  main_class: 'WontCatchSuppressedException',
  install: true,
  install_dir: join_paths(javadir, jardir),
)
jar('willuncaught', 'WontCatchNullPointerException.java',
  main_class: 'WontCatchNullPointerException',
  install: true,
  install_dir: join_paths(javadir, jardir),
)

java_configuration = configuration_data()
java_configuration.set_quoted('JAVADIR', javadir)

java_configuration_will_throw = configuration_data()
java_configuration_will_throw.set_quoted('JAR', join_paths(jardir, 'willuncaught.jar'))

java_configuration_will_throw_remote = configuration_data()
java_configuration_will_throw_remote.set_quoted('JAR', join_paths(jardir, 'willremoteloader.jar'))
java_configuration_will_throw_remote.set_quoted('JARUNCAUGHT', join_paths(javadir, jardir, 'willuncaught.jar'))

java_configuration_will_throw_suppressed = configuration_data()
java_configuration_will_throw_suppressed.set_quoted('JAR', join_paths(jardir, 'willsuppressed.jar'))

scripts = [
  'will_perl_sigsegv',
  'will_python3_raise',
  'will_python3_sigsegv',
  'will_ruby_raise',
  configure_file(
    configuration: java_configuration,
    input: 'will_java_segfault.in',
    output: 'will_java_segfault',
    install: true,
    install_dir: bindir,
  ),
  configure_file(
    configuration: java_configuration_will_throw,
    input: 'will_java_throw.in',
    output: 'will_java_throw',
    install: true,
    install_dir: bindir,
  ),
  configure_file(
    configuration: java_configuration_will_throw_remote,
    input: 'will_java_throw_remote.in',
    output: 'will_java_throw_remote',
    install: true,
    install_dir: bindir,
  ),
  configure_file(
    configuration: java_configuration_will_throw_suppressed,
    input: 'will_java_throw_suppressed.in',
    output: 'will_java_throw_suppressed',
    install: true,
    install_dir: bindir,
  ),
]
install_data(scripts,
  install_dir: get_option('bindir'),
)

custom_target('class_files',
  command: [
    javac,
    '-d', '@OUTDIR@',
    '@INPUT@',
  ],
  input: [
    'WillRaiseSigSegv.java',
  ],
  install: true,
  install_dir: javadir,
  output: [
    'WillRaiseSigSegv.class',
  ],
)

install_data('will_crash.rb',
  install_dir: vendordir,
)

install_subdir('will_oops_kmod',
  install_dir: kmoddir,
  strip_directory: true,
)

kmod_configuration = configuration_data()
kmod_configuration.set_quoted('KMODSRC', kmoddir)

configure_file(
  configuration: kmod_configuration,
  input: 'will_oops.in',
  output: 'will_oops',
  install: true,
  install_dir: bindir,
)
