%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	Oracle
Summary:	DBD::Oracle - an Oracle interface for Perl
Summary(pl.UTF-8):	DBD::Oracle - interfejs Oracle'a dla Perla
Name:		perl-DBD-Oracle
Version:	1.16
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9711550ed0ebfc743920a6a357ed717c
URL:		http://search.cpan.org/dist/DBD-Oracle/
BuildRequires:	perl-Class-Fields
BuildRequires:	perl-DBI >= 1.20
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _preserve_env %_preserve_env_base ORACLE_HOME

%description
DBD::Oracle is a Perl module which works with the DBI module to
provide access to Oracle 7/8/9 databases.

%description -l pl.UTF-8
DBD::Oracle jest modułem Perla umożliwiającym dostęp do baz Oracle'a
7/8/9 za pośrednictwem modułu DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{?oracledir:ORACLE_HOME="%{oracledir}"; export ORACLE_HOME}
#" vim
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Oracle.ex/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.[cels]* README.help Todo
%attr(755,root,root) %{_bindir}/ora_explain
%{perl_vendorarch}/DBD/Oracle.pm
%{perl_vendorarch}/DBD/Oracle
%dir %{perl_vendorarch}/auto/DBD/Oracle
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Oracle/Oracle.so
%{perl_vendorarch}/auto/DBD/Oracle/Oracle.bs
%{perl_vendorarch}/auto/DBD/Oracle/Oracle.h
%{_mandir}/man1/ora_explain.1*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
