Summary: A statically linked shell, including some built-in basic commands.
Name: sash
Version: 2.1
Release: 4
Copyright: GPL
Group: System Environment/Shells
Source0: http://www.tip.net.au/~dbell/sash-2.1.tar.gz
Patch0: sash-2.1-misc.patch
Buildroot: /var/tmp/sash-root

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip.  Sash
is statically linked so that it can work without shared libraries, so
it is particularly useful for recovering from certain types of system
failures.  Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch0 -p1 -b ".misc"

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

install -s -m755 sash $RPM_BUILD_ROOT/sbin
install -m644 sash.1 $RPM_BUILD_ROOT/usr/man/man8/sash.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/sash
/usr/man/man8/sash.8
