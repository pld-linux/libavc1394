#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Programming interface to the 1394 AV/C specification
Summary(pl.UTF-8):	Interfejs programistyczny do specyfikacji 1394 AV/C
Name:		libavc1394
Version:	0.5.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libavc1394/%{name}-%{version}.tar.gz
# Source0-md5:	09e30b1fb5ae455b6d8407e457a711a3
URL:		http://sourceforge.net/projects/libavc1394/
BuildRequires:	autoconf
BuildRequires:	automake
# pkgconfig calls this 1.0.0
BuildRequires:	libraw1394-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libavc1394 is a programming interface to the AV/C specification from
the 1394 Trade Association. AV/C stands for Audio/Video Control.
Currently, applications use the library to control the tape transport
mechanism on DV camcorders. However, there are many devices and
functions of devices that can be controlled via AV/C. Eventually, the
library will be expanded to implement more of the specification and to
provide high level interfaces to various devices.

%description -l pl.UTF-8
libavc1394 to interfejs programistyczny do specyfikacji AV/C
opracowanej przez 1394 Trade Association. AV/C oznacza Audio/Video
Control (czyli sterowanie Audio/Video). Aktualnie aplikacje używają
tej biblioteki do kontroli mechanizmu przesuwu taśmy w kamerach DV,
lecz wiele urządzeń i ich funkcji można kontrolować poprzez AV/C. Być
może biblioteka zostanie rozszerzona, by obsługiwać większą część
specyfikacji i zapewniać interfejsy wysokiego poziomu do różnych
urządzeń.

%package devel
Summary:	libavc1394 header files
Summary(pl.UTF-8):	Pliki nagłówkowe libavc1394
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw1394-devel >= 1.2.0

%description devel
libavc1394 header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libavc1394.

%package static
Summary:	Static libavc1394 library
Summary(pl.UTF-8):	Statyczna biblioteka libavc1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libavc1394 library.

%description static -l pl.UTF-8
Statyczna biblioteka libavc1394.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libavc1394
%{_pkgconfigdir}/libavc1394.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
