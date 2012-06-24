#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	CrossProduct
Summary:	Set::CrossProduct - work with the cross product of two or more sets
Summary(pl):	Modu� Set::CrossProduct - u�atwiaj�cy prac� z iloczynem kartezja�skim zbior�w
Name:		perl-Set-CrossProduct
Version:	1.4
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given sets S(1), S(2), ..., S(k), each of cardinality n(1), n(2), ...,
n(k) respectively, the cross product of the sets is the set CP of
ordered tuples such that { <s1, s2, ..., sk> | s1 => S(1), s2 => S(2),
... sk => S(k). }

%description -l pl
Dane s� zbiory S(1), S(2), ... S(k), ka�dy  o liczno�ci odpowiednio
n(1), n(2), ... n(k). Iloczynem kartezja�skim (produktem) tych zbior�w
jest zbi�r CP uporz�dkowanych krotek, takich �e { <s1, s2, ... sk> |
s1 => S(1), s2 => S(2), ... sk => S(k). }.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
