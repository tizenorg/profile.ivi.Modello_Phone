Name:       Modello_Phone
Summary:    A proof of concept pure html5 UI
Version:    0.0.2
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  zip
Requires:   Modello_Common
Requires:   phoned
BuildRequires: pkgconfig(libtzplatform-config)

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{TZ_SYS_APP_PREINSTALL}
mkdir -p %{buildroot}%{_datadir}/Modello/Common/icons
zip -r %{buildroot}%{TZ_SYS_APP_PREINSTALL}/%{name}.wgt config.xml css data Phone_icon.png index.html js templates
install -m 0644 Phone_icon.png %{buildroot}%{_datadir}/Modello/Common/icons

%files
%defattr(-,root,root,-)
%{TZ_SYS_APP_PREINSTALL}/Modello_Phone.wgt
%{_datadir}/Modello/Common/icons/Phone_icon.png
