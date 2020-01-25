Summary:	Utility to send e-mail written in Perl
Summary(pl.UTF-8):	Narzędzie do wysyłania poczty napisane w Perlu
Name:		sendEmail
Version:	1.56
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://caspian.dotconf.net/menu/Software/SendEmail/%{name}-v%{version}.tar.gz
# Source0-md5:	a8ee889b18356694546d3c1b2254e78c
Patch0:		%{name}-get_hostname.patch
URL:		http://caspian.dotconf.net/menu/Software/SendEmail/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SendEmail is a lightweight tool written in Perl for sending SMTP email
from the console. It was designed to be used in bash scripts, Perl
programs, and Web pages. It requires no special modules, and has a
simple interface, making it very easy to install and use. It should
work on any platform that has Perl and supports Unix sockets, but was
designed for Linux.

%description -l pl.UTF-8
SendEmail to małe narzędzie napisane w Perlu, służące do wysyłania
poczty po SMTP z terminala. Zostało opracowane do użytku w skryptach
powłoki, programach w Perlu i stronach WWW. Nie wymaga żadnych
specjalnych modułów i ma prosty interfejs, co sprawia, że jest łatwy
do zainstalowania i użytku. Powinien działać na każdej platformie,
która ma Perla i obsługuje gniazda uniksowe, ale został stworzony dla
Linuksa.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -D sendEmail $RPM_BUILD_ROOT%{_sbindir}/sendEmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/*
