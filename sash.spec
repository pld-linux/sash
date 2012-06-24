Summary:	A statically linked shell, including some built-in basic commands
Summary(es):	Interpretador de Comandos conectado est�ticamente con algunos comandos b�sicos
Summary(pl):	Skonsolidowana statycznie pow�oka z wbudowanymi podstawowymi poleceniami
Summary(pt_BR):	nterpretador de Comandos ligado estaticamente com alguns comandos b�sicos
Summary(ru):	���������� ��������� shell �� ����������� �������� ���������
Summary(uk):	�������� ڦ������ shell �� ����������� �������� ���������
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
est�ticamente. Incluye versiones simplificadas de comandos como ls, dd
y gzip. Sash puede ser �til en situaciones de recuperaci�n del
sistema.

%description -l pl
Sash jest prost�, samodzieln�, skonsolidowan� statycznie pow�ok�,
kt�ra ma wbudowane uproszczone wersje polece� takich jak ls, dd czy
gzip. Ze wzgl�du na statyczn� konsolidacj� Sash mo�e pracowa� bez
bibliotek wsp�dzielonych, co jest przydatne do ratowania systemu po
awarii. Sash mo�e by� tak�e u�ywany do bezpiecznego uaktualniania
bibliotek dzielonych do nowszych wersji.

%description -l pt_BR
O Sash � um interpretador de comandos simples ligado estaticamente.
Inclui vers�es simplificadas de comandos como ls, dd e gzip. O Sash
pode ser �til em situa��es de recupera��o do sistema.

%description -l ru
Sash - ��� �������, ���������� ��������� shell, ���������� � ����
���������� ���������� ������ ������ ���� ls, dd � gzip. �������������
�� ������������ ��������� �������� ������� ��� "������������ �����"
����� ��������� ����� � ��� ����������� �������� ���������
������������ ���������.

%description -l uk
Sash - �� �������, �������� ڦ������ shell, �� ������� �������Φ
������Φ ���Ӧ� ����� ������ �� ls, dd �� gzip. �������Φ��� צ�
����ͦ���� ¦�̦���� �������� ������� ��� "����������� ��¦�" Ц���
��������� ��ϧ� �� ��� ���������� �������� ��������� ����ͦ����
¦�̦����.

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
