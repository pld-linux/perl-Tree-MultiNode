#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tree
%define		pnam	MultiNode
%include	/usr/lib/rpm/macros.perl
Summary:	Tree::MultiNode Perl module - a multi node tree object
Summary(pl.UTF-8):	Moduł Perla Tree::MultiNode - obiekt drzewa wielowęzłowego
Name:		perl-Tree-MultiNode
Version:	1.0.10
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5616a11ec829742fc53d34e46782ae5a
URL:		http://search.cpan.org/dist/Tree-MultiNode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tree::MultiNode, Tree::MultiNode::Node, and Tree::MultiNode::Handle
are objects modeled after C++ classes that I had written to help me
model hierarchical information as datastructures (such as the
relationships between records in an RDBMS). The tree is basically a
list of lists type data structure, where each node has a key, a value,
and a list of children. The tree has no internal sorting, though all
operations perserve the order of the child nodes.

%description -l pl.UTF-8
Tree::MultiNode, Tree::MultiNode::Node i Tree::MultiNode::Handle to
obiekty stworzone na podstawie klas C++ napisanych dla ułatwienia
opracowania modelu hierarchicznej informacji jako struktur danych
(takich jak relacje pomiędzy rekordami w relacyjnej bazie danych).
Drzewo jest zasadniczo strukturą danych typu lista list, gdzie każdy
węzeł ma klucz, wartość i listę potomków. Drzewo nie ma wewnętrznego
sortowania, ale wszystkie operacje zachowują kolejność węzłów
potomnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README test.pl
%{perl_vendorlib}/Tree/MultiNode.pm
%{_mandir}/man3/*
