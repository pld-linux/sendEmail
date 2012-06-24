Summary:	Utility to send e-mail written in perl
Summary(pl):	Narz�dzie do wysy�ania poczty napisane w perlu
Name:		sendEmail
Version:	1.33
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
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

%prep
%setup -q -n %{name}-v%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install sendEmail $RPM_BUILD_ROOT%{_sbindir}/sendEmail

gzip -9nf CHANGELOG README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
