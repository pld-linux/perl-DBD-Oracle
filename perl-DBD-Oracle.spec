%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Oracle
Summary:	DBD::Oracle perl module
Summary(pl):	Modu³ perla DBD::Oracle
Name:		perl-DBD-Oracle
Version:	1.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-DBI >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Oracle - an Oracle 7 and Oracle 8 interface for Perl 5.

%description -l pl
DBD::Oracle - interfejs Oracle 7 i Oracle 8 do Perla 5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL

%{?oracledir:ORACLE_HOME="%{oracledir}"; export ORACLE_HOME}
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Oracle.ex/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.[cels]* README.help Todo
#%%{perl_sitearch}/???
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
