Summary:	A statically linked shell, including some built-in basic commands.
Name:		sash
Version:	2.1
Release:	4
Copyright:	GPL
Group:		System Environment/Shells
Source0:	http://www.tip.net.au/~dbell/%{name}-%{version}.tar.gz
Patch0:		sash-2.1-misc.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip.  Sash
is statically linked so that it can work without shared libraries, so
it is particularly useful for recovering from certain types of system
failures.  Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch0 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

install -s sash $RPM_BUILD_ROOT/sbin
install sash.1 $RPM_BUILD_ROOT%{_mandir}/man8/sash.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/sash.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/sash
%{_mandir}/man8/sash.8.gz
