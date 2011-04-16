%define upstream_name    Net-OpenID-Server
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Library for building your own OpenID server
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Crypt::DH)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This is the Perl API for (the server half of) OpenID, a distributed
identity system based on proving you own a URL, which is then your
identity. More information is available at:

  http://openid.net/

As of version 1.01 this module has support for both OpenID 1.1 and 2.0.
Prior to this, only 1.1 was supported.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


