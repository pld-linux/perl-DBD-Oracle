%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Oracle
Summary:	DBD::Oracle perl module
Summary(pl):	Modu³ perla DBD::Oracle
Name:		perl-DBD-Oracle
Version:	1.14
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec364509df5dfd57a4c05e2c410f358f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-Fields
BuildRequires:	perl-DBI >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Oracle - an Oracle 7/8/9 interface for Perl 5.

%description -l pl
DBD::Oracle - interfejs Oracle 7/8/9 do Perla 5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{?oracledir:ORACLE_HOME="%{oracledir}"; export ORACLE_HOME}
%{__make} \
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

%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.bs
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.h

%{_mandir}/man1/ora_explain.1*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
