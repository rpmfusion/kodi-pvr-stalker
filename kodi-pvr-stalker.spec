%global commit 2eb66d11f8f90040824067d41919cf53f6267228
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180825

%global kodi_addon pvr.stalker
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        3.4.5
Release:        1%{?dist}
Summary:        Stalker PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64 aarch64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Fix wrong end-of-lines encoding
sed "s/\r//" README.md >README.md.new
touch -r README.md README.md.new
mv README.md.new README.md


%build
# https://gitlab.kitware.com/cmake/cmake/issues/17555#note_355574
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.4.5-1
- Update to 3.4.5
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.2-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8.8-2
- Drop kodi-pvr-stalker-2.8.5-build.patch (merged upstream)

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8.8-1
- Update to 2.8.8

* Thu Apr 27 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 2.8.5-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.12-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.3-1
- Initial RPM release
