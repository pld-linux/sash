Summary:	A statically linked shell, including some built-in basic commands
Summary(es):	Interpretador de Comandos conectado estАticamente con algunos comandos bАsicos
Summary(pl):	Skonsolidowana statycznie powЁoka z wbudowanymi podstawowymi poleceniami
Summary(pt_BR):	nterpretador de Comandos ligado estaticamente com alguns comandos bАsicos
Summary(ru):	Статически собранный shell со встроенными базовыми командами
Summary(uk):	Статично з╕браний shell ╕з вбудованими базовими командами
Name:		sash
Version:	3.6
Release:	2
License:	GPL
Group:		Applications/Shells
Source0:	http://www.tip.net.au/~dbell/programs/%{name}-%{version}.tar.gz
# Source0-md5:	56dd73d91374e1f0c59b9860b2855119
Patch0:		%{name}-misc.patch
Patch1:		%{name}-losetup.patch
BuildRequires:	zlib-static >= 1.1.4
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

%description -l es
Sash es un interpretador de comandos sencillos encendido
estАticamente. Incluye versiones simplificadas de comandos como ls, dd
y gzip. Sash puede ser Зtil en situaciones de recuperaciСn del
sistema.

%description -l pl
Sash jest prost╠, samodzieln╠, skonsolidowan╠ statycznie powЁok╠,
ktСra ma wbudowane uproszczone wersje poleceЯ takich jak ls, dd czy
gzip. Ze wzglЙdu na statyczn╠ konsolidacjЙ Sash mo©e pracowaФ bez
bibliotek wspСЁdzielonych, co jest przydatne do ratowania systemu po
awarii. Sash mo©e byФ tak©e u©ywany do bezpiecznego uaktualniania
bibliotek dzielonych do nowszych wersji.

%description -l pt_BR
O Sash И um interpretador de comandos simples ligado estaticamente.
Inclui versУes simplificadas de comandos como ls, dd e gzip. O Sash
pode ser Зtil em situaГУes de recuperaГЦo do sistema.

%description -l ru
Sash - это простой, статически собранный shell, включающий в себя
упрощенные встроенные версии команд типа ls, dd и gzip. Независимость
от динамических библиотек особенно полезна для "спасательных работ"
после системных сбоев и для безопасного апгрейда системных
динамических библиотек.

%description -l uk
Sash - це простий, статично з╕браний shell, що включа╓ вбудован╕
спрощен╕ верс╕╖ таких команд як ls, dd та gzip. Незалежн╕сть в╕д
динам╕чних б╕бл╕отек особливо корисна для "рятувальних роб╕т" п╕сля
системних збо╖в та для безпечного апгрейду системних динам╕чних
б╕бл╕отек.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CC="%{__cc}" COPT_FLAGS="%{rpmcflags}"

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
