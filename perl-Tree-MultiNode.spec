%include	/usr/lib/rpm/macros.perl
Summary:	Tree-MultiNode perl module
Summary(pl):	Modu³ perla Tree-MultiNode
Name:		perl-Tree-MultiNode
Version:	1.0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tree/Tree-MultiNode-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tree-MultiNode perl module. 

%description -l pl
Modu³ perla Tree-MultiNode.

%prep
%setup -q -n Tree-MultiNode-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tree/MultiNode
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz test.pl

%{perl_sitelib}/Tree/MultiNode.pm
%{perl_sitearch}/auto/Tree/MultiNode

%{_mandir}/man3/*
