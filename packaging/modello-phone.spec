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

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build

make wgtPkg

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/Modello_Phone.wgt
/opt/usr/apps/_common/icons/Phone_icon.png