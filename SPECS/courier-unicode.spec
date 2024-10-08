Summary: Courier Unicode Library
Name: courier-unicode
Epoch: 2
Version: 2.1.2
Release: 1%{?dist}%{?courier_release}
License: GPLv3
Group: System Environment/Libraries
URL: http://www.courier-mta.org/unicode/
Source: http://download.sourceforge.net/courier/courier-unicode-2.1.2.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl
BuildRequires: gcc-c++

%package devel
Summary: Courier Unicode Library development files
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description
This library implements several algorithms related to the Unicode
Standard.

This package installs only the run-time libraries needed by applications that
use this library. Install the "courier-unicode-devel" package if you want
to develop new applications using this library.

%description devel
This package contains development files for the Courier Unicode Library.
Install this package if you want to develop applications that uses this
unicode library.

%prep
%setup -q
%configure
%build
%{__make} -s %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog AUTHORS
%{_libdir}/*.so.*

%files devel
%{_mandir}/*/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/aclocal/*.m4

%changelog
* Sun Jan 12 2014 Sam Varshavchik <mrsam@octopus.email-scan.com> - 1.0
- Initial build.
