Name:           RPG
Version:        0.0.1
Release:        1%{?snapshot}%{?dist}
Summary:        RPM Package Generator
License:        GPLv2
URL:            https://github.com/rh-lab-q/rpg
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildArch:      noarch

Requires:       python3 >= 3.4
Requires:       python3-qt5
Requires:       qt5-qtbase-gui
Requires:       coreutils
Requires:       file
Requires:       makedepend
Requires:       rpmdevtools
Recommends:     python3-argcomplete
Recommends:     python3-dnf
Recommends:     copr-cli

%description
RPG is tool, that guides people through the creation of a RPM
package. RPG makes packaging much easier due to the automatic analysis of
packaged files. Beginners can get familiar with packaging process or the
advanced users can use our tool for a quick creation of a package.

%prep
%autosetup

%build
%cmake .

%post
activate-global-python-argcomplete
exec bash

%install
make install DESTDIR=%{RPM_BUILD_ROOT}
%make_install

%check
make test

%files
%{_bindir}/rpg
%{python3_sitelib}/rpg/

%changelog
