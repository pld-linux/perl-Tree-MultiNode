%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	MultiNode
Summary:	MultiNode.pm -- a multi node tree object.
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
Tree::MultiNode, Tree::MultiNode::Node, and MultiNode::Handle are objects
modeled after C++ classes that I had written to help me model heirarchical
information as datastructures (such as the relationships between records
in an RDBMS).  The tree is basicly a list of lists type data structure,
where each node has a key, a value, and a list of children.  The tree
has no internal sorting, though all operations perserve the order of
the child nodes.

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
