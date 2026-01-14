#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Set
%define		pnam	CrossProduct
Summary:	Set::CrossProduct Perl module - work with the cross product of two or more sets
Summary(pl.UTF-8):	Moduł Perla Set::CrossProduct - ułatwienie pracy z iloczynem kartezjańskim zbiorów
Name:		perl-Set-CrossProduct
Version:	1.95
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cdebe89c6c1b0790011eaea47e22af8b
URL:		http://search.cpan.org/dist/Set-CrossProduct/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given sets S(1), S(2), ..., S(k), each of cardinality n(1), n(2), ...,
n(k) respectively, the cross product of the sets is the set CP of
ordered tuples such that { <s1, s2, ..., sk> | s1 => S(1), s2 => S(2),
... sk => S(k). }

%description -l pl.UTF-8
Dane są zbiory S(1), S(2), ... S(k), każdy o liczności odpowiednio
n(1), n(2), ... n(k). Iloczynem kartezjańskim (produktem) tych zbiorów
jest zbiór CP uporządkowanych krotek, takich że { <s1, s2, ... sk> |
s1 => S(1), s2 => S(2), ... sk => S(k). }.

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
%attr(755,root,root) %{_bindir}/cross
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man?/*
