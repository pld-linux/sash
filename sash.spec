Summary:	A statically linked shell, including some built-in basic commands
Name:		sash
Version:	3.4
Release:	9
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Source0:	http://www.tip.net.au/~dbell/%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
Patch1:		%{name}-scriptarg.patch
Patch2:		%{name}-losetup.patch
BuildRequires:	zlib-static
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip. Sash is
statically linked so that it can work without shared libraries, so it
is particularly useful for recovering from certain types of system
failures. Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install sash $RPM_BUILD_ROOT%{_sbindir}
install sash.1 $RPM_BUILD_ROOT%{_mandir}/man8/sash.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sash
%{_mandir}/man8/*
