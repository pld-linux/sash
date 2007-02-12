Summary:	A statically linked shell, including some built-in basic commands
Summary(es.UTF-8):   Interpretador de Comandos conectado estáticamente con algunos comandos básicos
Summary(pl.UTF-8):   Skonsolidowana statycznie powłoka z wbudowanymi podstawowymi poleceniami
Summary(pt_BR.UTF-8):   nterpretador de Comandos ligado estaticamente com alguns comandos básicos
Summary(ru.UTF-8):   Статически собранный shell со встроенными базовыми командами
Summary(uk.UTF-8):   Статично зібраний shell із вбудованими базовими командами
Name:		sash
Version:	3.7
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.tip.net.au/~dbell/programs/%{name}-%{version}.tar.gz
# Source0-md5:	ee7c7ed5aad76599974d016a6f201ef4
Patch0:		%{name}-misc.patch
Patch1:		%{name}-losetup.patch
BuildRequires:	glibc-static
BuildRequires:	zlib-static >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_sbindir	/sbin

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip. Sash is
statically linked so that it can work without shared libraries, so it
is particularly useful for recovering from certain types of system
failures. Sash can also be used to safely upgrade to new versions of
shared libraries.

%description -l es.UTF-8
Sash es un interpretador de comandos sencillos encendido
estáticamente. Incluye versiones simplificadas de comandos como ls, dd
y gzip. Sash puede ser útil en situaciones de recuperación del
sistema.

%description -l pl.UTF-8
Sash jest prostą, samodzielną, skonsolidowaną statycznie powłoką,
która ma wbudowane uproszczone wersje poleceń takich jak ls, dd czy
gzip. Ze względu na statyczną konsolidację Sash może pracować bez
bibliotek współdzielonych, co jest przydatne do ratowania systemu po
awarii. Sash może być także używany do bezpiecznego uaktualniania
bibliotek dzielonych do nowszych wersji.

%description -l pt_BR.UTF-8
O Sash é um interpretador de comandos simples ligado estaticamente.
Inclui versões simplificadas de comandos como ls, dd e gzip. O Sash
pode ser útil em situações de recuperação do sistema.

%description -l ru.UTF-8
Sash - это простой, статически собранный shell, включающий в себя
упрощенные встроенные версии команд типа ls, dd и gzip. Независимость
от динамических библиотек особенно полезна для "спасательных работ"
после системных сбоев и для безопасного апгрейда системных
динамических библиотек.

%description -l uk.UTF-8
Sash - це простий, статично зібраний shell, що включає вбудовані
спрощені версії таких команд як ls, dd та gzip. Незалежність від
динамічних бібліотек особливо корисна для "рятувальних робіт" після
системних збоїв та для безпечного апгрейду системних динамічних
бібліотек.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8}

install sash $RPM_BUILD_ROOT%{_sbindir}
install sash.1 $RPM_BUILD_ROOT%{_mandir}/man8/sash.8
ln -sf %{_sbindir}/sash $RPM_BUILD_ROOT%{_bindir}/sash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sash
%attr(755,root,root) %{_sbindir}/sash
%{_mandir}/man8/*
