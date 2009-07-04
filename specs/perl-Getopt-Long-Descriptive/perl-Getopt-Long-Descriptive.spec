# $Id$
# Authority: cmr
# Upstream: Hans Dieter Pearcey <hdp$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Long-Descriptive

Summary: Getopt::Long with usage text
Name: perl-Getopt-Long-Descriptive
Version: 0.074
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Long-Descriptive/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Long-Descriptive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Getopt::Long with usage text.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Getopt::Long::Descriptive.3pm*
%dir %{perl_vendorlib}/Getopt/
%dir %{perl_vendorlib}/Getopt/Long/
#%{perl_vendorlib}/Getopt/Long/Descriptive/
%{perl_vendorlib}/Getopt/Long/Descriptive.pm

%changelog
* Sat Jul 04 2009 Unknown - 0.074-1
- Initial package. (using DAR)