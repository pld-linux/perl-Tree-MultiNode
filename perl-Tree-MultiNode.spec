%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	MultiNode
Summary:	Tree::MultiNode perl module
Summary(pl):	Modu³ perla Tree::MultiNode
Name:		perl-Tree-MultiNode
Version:	1.0.8
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tree::MultiNode perl module.

%description -l pl
Modu³ perla Tree::MultiNode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README test.pl
%{perl_sitelib}/Tree/MultiNode.pm
%{_mandir}/man3/*
