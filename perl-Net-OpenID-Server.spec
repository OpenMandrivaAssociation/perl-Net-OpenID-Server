%define upstream_name    Net-OpenID-Server
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Library for building your own OpenID server
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::DH)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(URI)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 653607
- rebuild for updated spec-helper

* Wed Aug 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 573359
- import perl-Net-OpenID-Server

