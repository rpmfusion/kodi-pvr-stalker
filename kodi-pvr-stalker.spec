%global commit d01bf4b66d50b9cd8261700ee9f2cc483cfd8faf
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170708

%global kodi_addon pvr.stalker
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        2.8.8
Release:        3%{?dist}
Summary:        A PVR client that connects Kodi to Stalker Middleware

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# Fix jsoncpp library detection
Patch0:         %{name}-2.8.5-jsoncpp.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  libxml2-devel
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
PVR Client to connect Kodi to Stalker Middleware.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Fix wrong end-of-lines encoding
sed "s/\r//" README.md >README.md.new
touch -r README.md README.md.new
mv README.md.new README.md


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
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
