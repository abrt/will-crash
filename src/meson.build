libwillcrash = shared_library('willcrash', 'libwillcrash.c',
  install: true,
  install_dir: join_paths(libdir, meson.project_name()),
)
shared_library('willjavasegfault', 'will_java_segfault.c',
  c_args: [
    '-I@0@'.format(join_paths(get_option('_java_home'), 'include')),
    '-I@0@'.format(join_paths(get_option('_java_home'), 'include', 'linux')),
  ],
  install: true,
  soversion: '0',
)

executable('will_segfault', 'will_segfault.c',
  link_with: libwillcrash,
  install: true,
  install_rpath: join_paths(prefix, privlibdir),
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

jars = [
  {
    'name': 'willremoteloader',
    'main_class': 'WontCatchRemoteException',
  },
  {
    'name': 'willsuppressed',
    'main_class': 'WontCatchSuppressedException',
  },
  {
    'name': 'willuncaught',
    'main_class': 'WontCatchNullPointerException',
  },
]

foreach _jar : jars
  jar(_jar.get('name'), '@0@.java'.format(_jar.get('main_class')),
    main_class: _jar.get('main_class'),
    install: true,
    install_dir: join_paths(javadir, jardir)
  )
endforeach

java_configuration = configuration_data()
java_configuration.set_quoted('JAVADIR', javadir)

java_configuration_will_throw = configuration_data()
java_configuration_will_throw.set_quoted('JAR', join_paths(jardir, 'willuncaught.jar'))

java_configuration_will_throw_remote = configuration_data()
java_configuration_will_throw_remote.set_quoted('JAR', join_paths(jardir, 'willremoteloader.jar'))
java_configuration_will_throw_remote.set_quoted('JARUNCAUGHT', join_paths(javadir, jardir, 'willuncaught.jar'))

java_configuration_will_throw_suppressed = configuration_data()
java_configuration_will_throw_suppressed.set_quoted('JAR', join_paths(jardir, 'willsuppressed.jar'))

kmod_configuration = configuration_data()
kmod_configuration.set_quoted('KMODSRC', join_paths(prefix, kmoddir))

generated_scripts = [
  {
    'script': 'will_java_segfault',
    'configuration': java_configuration,
  },
  {
    'script': 'will_java_throw',
    'configuration': java_configuration_will_throw,
  },
  {
    'script': 'will_java_throw_remote',
    'configuration': java_configuration_will_throw_remote,
  },
  {
    'script': 'will_java_throw_suppressed',
    'configuration': java_configuration_will_throw_suppressed,
  },
  {
    'script': 'will_oops',
    'configuration': kmod_configuration,
  },
]

foreach script : generated_scripts
  configure_file(
    configuration: script.get('configuration'),
    input: '@0@.in'.format(script.get('script')),
    output: script.get('script'),
    install: true,
    install_dir: bindir,
    install_mode: 'rwxr-xr-x',
  )
endforeach

scripts = [
  'will_perl_sigsegv',
  'will_python3_raise',
  'will_python3_sigsegv',
  'will_ruby_raise',
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
