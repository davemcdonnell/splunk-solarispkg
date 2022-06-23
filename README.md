# splunk-solarispkg
As root:
pkg install package/pkgbuild

As build user:

pkgtool --download --interactive build splunk.spec

pkgtrans -s ~/packages/PKGS/ splunkforwarder-9.0.0-6818ac46f2ec-solaris-8-sparc.pkg splunkforwarder
