Summary:	Programming interface to the 1394 AV/C specification
Summary(pl):	Interfejs programistyczny do specyfikacji 1394 AV/C
Name:		libavc1394
Version:	0.4.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libavc1394/%{name}-%{version}.tar.gz
# Source0-md5:	cca44f87bda7d5572473290dec7cd81e
Patch0:		%{name}-link.patch
URL:		http://sourceforge.net/projects/libavc1394/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libraw1394-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libavc1394 is a programming interface to the AV/C specification from
the 1394 Trade Association. AV/C stands for Audio/Video Control.
Currently, applications use the library to control the tape transport
mechanism on DV camcorders. However, there are many devices and
functions of devices that can be controlled via AV/C. Eventually, the
library will be expanded to implement more of the specification and to
provide high level interfaces to various devices.

%description -l pl
libavc1394 to interfejs programistyczny do specyfikacji AV/C
opracowanej przez 1394 Trade Association. AV/C oznacza Audio/Video
Control (czyli sterowanie Audio/Video). Aktualnie aplikacje u¿ywaj±
tej biblioteki do kontroli mechanizmu przesuwu ta¶my w kamerach DV,
lecz wiele urz±dzeñ i ich funkcji mo¿na kontrolowaæ poprzez AV/C. Byæ
mo¿e biblioteka zostanie rozszerzona, by obs³ugiwaæ wiêksz± czê¶æ
specyfikacji i zapewniaæ interfejsy wysokiego poziomu do ró¿nych
urz±dzeñ.

%package devel
Summary:	libavc1394 header files
Summary(pl):	Pliki nag³ówkowe libavc1394
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libraw1394-devel

%description devel
libavc1394 header files.

%description devel -l pl
Pliki nag³ówkowe libavc1394.

%package static
Summary:	Static libavc1394 library
Summary(pl):	Statyczna biblioteka libavc1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libavc1394 library.

%description static -l pl
Statyczna biblioteka libavc1394.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
