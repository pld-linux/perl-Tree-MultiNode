%include	/usr/lib/rpm/macros.perl
Summary:	Tree-MultiNode perl module
Summary(pl):	Modu� perla Tree-MultiNode
Name:		perl-Tree-MultiNode
Version:	1.0.7
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tree/Tree-MultiNode-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tree-MultiNode perl module.

%description -l pl
Modu� perla Tree-MultiNode.

%prep
%setup -q -n Tree-MultiNode-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test.pl
%{perl_sitelib}/Tree/MultiNode.pm
%{_mandir}/man3/*
