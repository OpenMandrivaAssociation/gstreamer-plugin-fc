%define version 0.2
%define release %mkrel 3

Name: gstreamer-plugin-fc
Summary: Future Composer plugin for GStreamer
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Sound
URL: http://xmms-fc.sourceforge.net/
Source:	http://prdownloads.sourceforge.net/xmms-fc/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gstreamer0.10-devel
BuildRequires: libfc14audiodecoder-devel
Requires: xmms

%description
This is an input plugin for GStreamer which can play back Future Composer
music files from AMIGA.

%package -n gstreamer0.10-fc
Summary: Future Composer plugin for GStreamer
Group: Sound

%description -n gstreamer0.10-fc
This is an input plugin for GStreamer which can play back Future Composer
music files from AMIGA.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%{_libdir}/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n gstreamer0.10-fc
%defattr(-,root,root)
%doc README ChangeLog
%{_libdir}/gstreamer-0.10/libgstfcdec.so




%changelog
* Sat Nov 05 2011 Götz Waschk <waschk@mandriva.org> 0.2-3mdv2012.0
+ Revision: 718899
- rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.2-2mdv2011.0
+ Revision: 593559
- rebuild for gstreamer provides

* Tue Jul 27 2010 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2011.0
+ Revision: 561326
- import gstreamer-plugin-fc


