%include	/usr/lib/rpm/macros.perl
Summary:	Utility to send e-mail written in perl
Summary(pl):	Narzêdzie do wysy³ania poczty napisane w perlu
Name:		sendEmail
Version:	1.40
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://caspian.dotconf.net/menu/Software/SendEmail/%{name}-v%{version}.tar.gz
URL:		http://marvin.criadvantage.com/caspian/
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SendEmail is a lightweight tool written in Perl for sending SMTP email
from the console. It was designed to be used in bash scripts, Perl
programs, and Web pages. It requires no special modules, and has a
simple interface, making it very easy to install and use. It should
work on any platform that has Perl and supports Unix sockets, but was
designed for Linux.

%description -l pl
SendEmail to ma³e narzêdzie napisane w Perlu, s³u¿±ce do wysy³ania
poczty po SMTP z terminala. Zosta³o opracowane do u¿ytku w skryptach
pow³oki, programach w Perlu i stronach WWW. Nie wymaga ¿adnych
specjalnych modu³ów i ma prosty interfejs, co sprawia, ¿e jest ³atwy
do zainstalowania i u¿ytku. Powinien dzia³aæ na ka¿dej platformie,
która ma Perla i obs³uguje gniazda uniksowe, ale zosta³ stworzony dla
Linuksa.

%prep
%setup -q -n %{name}-v%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install sendEmail $RPM_BUILD_ROOT%{_sbindir}/sendEmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_sbindir}/*
