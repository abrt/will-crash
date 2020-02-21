project(
  'will-crash',
  ['c', 'cpp', 'java'],
  license : 'GPL3+',
  version : '0.13.2'
)

cc = meson.get_compiler('c')

ruby = dependency('ruby')
threads = dependency('threads')

javac = find_program('javac')

bindir = get_option('bindir')
datadir = get_option('datadir')
jardir = 'willcrash'
javadir = get_option('javadir')
kmoddir = join_paths(datadir, meson.project_name())
libdir = get_option('libdir')
prefix = get_option('prefix')
privlibdir = join_paths(libdir, meson.project_name())
vendordir = ruby.get_pkgconfig_variable('vendordir')

tito = find_program('tito',
  required: false,
  disabler: true,
)

subdir('src')

# This will, naturally, fail if the build directory is outside the git repo,
# since Tito does not provide a way to specify the working directory or the spec
# file using the CLI.
run_target('rpm',
  command: [
    tito,
    'build',
    '--offline',
    '--output=@0@/rpm'.format(meson.current_build_dir()),
    '--rpm',
    '--test'
  ],
)
run_target('srpm',
  command: [
    tito,
    'build',
    '--offline',
    '--output=@0@/rpm'.format(meson.current_build_dir()),
    '--srpm',
    '--test'
  ],
)
