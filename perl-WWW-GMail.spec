#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	GMail
Summary:	WWW::GMail - Perl extension for accessing Google Mail (gmail)
Summary(pl.UTF-8):	WWW::GMail - Rozszerzenie Perla do obsługi poczty Google (gmail)
Name:		perl-WWW-GMail
Version:	0.07
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	405c7d85d35fc594cc52ea4e2f0e7eac
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl extension allows allows retrieval of message lists, and raw
messages from Google Mail (GMail) account.

%description -l pl.UTF-8
To rozszerzenie Perla pozwala na pobranie listy wiadomości oraz treści
poszczególnych listów z konta Google Mail (GMail).

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
