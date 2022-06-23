%define dist_name    splunkforwarder
Name:           splunkforwarder
SUNW_BaseDir:   /opt
Version:        9.0.0
SUNW_Desc:      Splunk> The platform for machine data.
Vendor:         Splunk Inc.
Source0:        http://download.splunk.com/products/universalforwarder/releases/9.0.0/solaris/splunkforwarder-9.0.0-6818ac46f2ec-SunOS-sparc.tar.Z

%description
Legacy build of %{dist_name}

%prep
%setup -q -n %{dist_name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/splunkforwarder
cp -R * $RPM_BUILD_ROOT/opt/splunkforwarder

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,sys,-)
/opt/splunkforwarder/*
